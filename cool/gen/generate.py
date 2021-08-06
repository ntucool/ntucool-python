import copy
import dataclasses
import pathlib
import re
import typing
import urllib.parse

import lxml.html
import requests


@dataclasses.dataclass
class Scope:
    method: str
    url: str
    keys: tuple[str, ...]


@dataclasses.dataclass
class RequestParameter:
    parameter: str
    type: str
    description: tuple[str, ...]
    allowed_values: tuple[str, ...]
    required: bool
    deprecated: str


@dataclasses.dataclass
class APIResource:
    api_method_name: str
    url: str
    subtopic: str
    defined_in: tuple[str, str]
    beta: str
    scopes: tuple[Scope, ...]
    description: tuple[str, ...]
    request_parameters: tuple[RequestParameter, ...]
    returns: tuple[str, ...]
    paginated: bool

    def request(
        self,
        session,
        scope: int = 0,
        strict: bool = False,
        raise_for_status: bool = True,
        return_response: bool = False,
        **params,
    ):
        pass


def scope_string_to_scope(scope_string: str) -> Scope:
    m = re.fullmatch(r'url:(.+?)\|(.+)', scope_string)
    if m is None:
        raise ValueError('invalid scope string {!r}'.format(scope_string))
    groups = m.groups()
    if any(g is None for g in groups):
        raise RuntimeError('{!r} groups {}'.format(scope_string, groups))
    method, url = groups
    parse_result = urllib.parse.urlparse(url)
    parts = list(pathlib.Path(parse_result.path).parts)
    keys = []
    for i, part in enumerate(parts):
        if part.startswith(':'):
            part = part[1:]
            keys.append(part)
            parts[i] = '{' + part + '}'
    path = str(pathlib.Path(*parts))
    url = urllib.parse.ParseResult(
        parse_result.scheme,
        parse_result.netloc,
        path,
        parse_result.params,
        parse_result.query,
        parse_result.fragment,
    ).geturl()
    keys = tuple(keys)
    return Scope(method, url, keys)


def get_api_resources(html_path):
    html_path = pathlib.Path(html_path)

    text = html_path.read_text()

    url = 'https://canvas.instructure.com/doc/api/all_resources.html'

    # session = requests.Session()
    # response = session.get(url)
    # html_path.write_bytes(response.content)
    # text = response.text
    # url = response.url

    html: lxml.html.HtmlElement = lxml.html.document_fromstring(text)
    method_details = html.xpath('//*[@id="Services"]/div')
    resources = []
    for method_detail in method_details:
        api_method_name = method_detail.xpath('h2')
        assert len(api_method_name) == 1
        api_method_name = api_method_name[0]
        subtopic = api_method_name.get('data-subtopic').strip()
        a = api_method_name.xpath('a')
        assert len(a) == 1
        a = a[0]
        href = urllib.parse.urljoin(url, a.get('href'))
        defined_in = api_method_name.xpath('span')
        assert len(defined_in) in (0, 1)
        if len(defined_in) == 0:
            defined_in = None
        else:
            defined_in = defined_in[0]
            defined_in = defined_in.xpath('a')[0]
            defined_in = defined_in.text_content().strip(), defined_in.get('href')
        api_method_name = a.text_content().strip()
        scopes = method_detail.xpath('div/code')
        scopes = tuple(scope.text for scope in scopes)
        scopes = tuple(scope_string_to_scope(scope) for scope in scopes)
        beta = method_detail.xpath("h3[contains(@class, 'beta')]")
        if len(beta) == 0:
            beta = None
        else:
            assert len(beta) == 1
            beta = beta[0]
            assert beta.get('class') == 'beta'
            beta = beta.text_content().strip()
        paragraphs = method_detail.xpath('p')
        description = tuple(p.text_content() for p in paragraphs)
        returns = ()
        text = [text.strip() for text in method_detail.xpath('text()') if text.strip() != '']
        if len(text) > 0:
            assert len(text) == 1
            text = text[0]
            texts = [t.strip() for t in method_detail.itertext()]
            index = -texts[::-1].index(text) - 1
            text = ' '.join(texts[index:]).strip()
            assert text.startswith('Returns ')
            returns = (text[len('Returns '):],)
        paginated = False
        if any('paginat' in p.lower() for p in description):
            paginated = True
        request_parameters = None
        table = method_detail.xpath('table')
        if len(table) > 0:
            request_parameters = []
            assert len(table) == 1
            table = table[0]
            thead = table.xpath('thead')
            assert len(thead) == 1
            thead = thead[0]
            tr = thead.xpath('tr')
            assert len(tr) == 1
            tr = tr[0]
            th = tr.xpath('th')
            if len(th) == 4:
                assert [_.get('class') for _ in th
                       ] == ['param-name', 'param-req', 'param-type', 'param-desc']
                assert [_.text_content() for _ in th] == ['Parameter', '', 'Type', 'Description']
            elif len(th) == 5:
                assert [_.get('class') for _ in th] == [
                    'param-name',
                    'param-req',
                    'param-type',
                    'param-deprecated',
                    'param-desc',
                ]
                assert [_.text_content() for _ in th
                       ] == ['Parameter', '', 'Type', '', 'Description']
            else:
                assert False
            tbody = table.xpath('tbody')
            assert len(tbody) == 1
            tbody = tbody[0]
            tr = tbody.xpath('tr')
            assert len(tr) > 0
            trs = tr
            for tr in trs:
                tds = tr.xpath('td')
                assert len(tds) == len(th)
                parameter = tds[0].text_content()
                required = tds[1].text_content().strip()
                assert required in ('', 'Required')
                required = True if required == 'Required' else False
                type_ = tds[2].text_content().strip()
                assert type_ in (
                    'string',
                    'boolean',
                    'number',
                    'DateTime',
                    'integer',
                    'Date',
                    'Hash',
                    '[Integer]',
                    'array',
                    'Object',
                    'AssignmentOverride',
                    'Array',
                    'BlueprintRestriction',
                    'multiple BlueprintRestrictions',
                    'Assignment',
                    'File',
                    'Deprecated',
                    'SerializedHash',
                    'object',
                    'json',
                    '[Answer]',
                    'String[]',
                    'QuizSubmissionQuestion',
                    'Numeric',
                    'QuizUserConversation',
                    'RubricAssessment',
                    'URL',
                    'JSON',
                )
                deprecated = None
                if len(th) == 5:
                    deprecated = tds[3].text_content().strip()
                    deprecated = '\n'.join(
                        [_.strip() for _ in deprecated.split('\n') if _.strip() != ''])
                request_parameters.append(
                    RequestParameter(parameter, type_, None, None, required, deprecated))
        resource = APIResource(
            api_method_name,
            href,
            subtopic,
            defined_in,
            beta,
            scopes,
            description,
            request_parameters,
            returns,
            paginated,
        )
        import utils
        d = dataclasses.asdict(resource)
        d['function_name'] = utils.create_function_name(api_method_name)
        resources.append(d)
        # print(resource)
        # print(method_detail.xpath('text()[8]'))
        # print(list(method_detail.itertext()))
        # print([text.strip() for text in method_detail.xpath('text()') if text.strip() != ''])
        # exit()
    import json
    pathlib.Path('resources.json').write_text(json.dumps(resources))


scope = scope_string_to_scope(
    'url:GET|https://cool.ntu.edu.tw/api/v1/accounts/:account_id/courses/:id')

if __name__ == '__main__':
    html_path = 'all_resources.html'
    get_api_resources(html_path)
