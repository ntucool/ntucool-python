import collections.abc
import copy
import json
import urllib.parse
import warnings

from typing import Optional

import requests

from cool import exceptions

warnings.filterwarnings('always')


def request(
    session: requests.Session,
    method: str,
    base: str,
    url: Optional[str] = None,
    queries=None,
    raise_for_status: bool = True,
    **kwargs,
):
    if url is None:
        url = base
    else:
        url = urllib.parse.urljoin(base, url)

    if queries is None:
        query = None
    else:
        query = queryjoin(*queries)

    url = geturl(url, query)

    # debug
    print(urllib.parse.unquote_plus(url))

    headers = kwargs.pop('headers', {})
    if method in ('POST', 'PUT', 'DELETE'):
        headers['X-CSRF-Token'] = get_x_csrf_token(session, url)

    if isinstance(session, requests.Session):
        response = session.request(method, url, headers=headers, **kwargs)
    else:
        raise TypeError

    # debug
    qs = urllib.parse.parse_qs(urllib.parse.urlparse(response.request.url).query)
    if 'per_page' not in qs and 'page' not in qs:
        if response.links != {}:
            message = '{} {} with response.links: {}'.format(method, response.request.url,
                                                             response.links)
            warnings.warn(message, category=RuntimeWarning)

    error = check_status(response, raise_for_status=raise_for_status)

    return response, error


def request_json(
    session: requests.Session,
    method: str,
    base: str,
    url: Optional[str] = None,
    queries=None,
    raise_for_error: bool = True,
    return_response: bool = False,
    return_error: bool = False,
    **kwargs,
):
    response, error = request(
        session,
        method,
        base,
        url=url,
        queries=queries,
        raise_for_status=False,
        **kwargs,
    )
    data, error = get_json_from_response(response, error=error, raise_for_error=raise_for_error)
    if return_response:
        if return_error:
            return data, response, error
        else:
            return data, response
    else:
        if return_error:
            return data, error
        else:
            return data


def is_iterable_not_str_not_bytes(obj):
    if isinstance(obj, (str, bytes)):
        return False
    try:
        iter(obj)
    except TypeError:
        return False
    return True


def resolve_query(query, brackets=False):
    """
    Data are returned as a list of name, value pairs.
    Bools are converted to lowecase strings.
    """
    resolved = []
    query = copy.deepcopy(query)
    if isinstance(query, collections.abc.Mapping):
        for name, value in query.items():
            if brackets:
                name = '[{}]'.format(name)
            value = resolve_query(value, brackets=True)
            for n, v in value:
                resolved.append((name + n, v))
    elif is_iterable_not_str_not_bytes(query):
        for value in query:
            # a sequence of two-element tuples
            if (not isinstance(value, collections.abc.Mapping) and
                    is_iterable_not_str_not_bytes(value)):
                if len(value) != 2:
                    raise ValueError
                name = value[0]
                if brackets:
                    name = '[{}]'.format(name)
                value = resolve_query(value[1], brackets=True)
            else:
                name = '[]' if brackets else ''
                value = resolve_query(value, brackets=True)
            for n, v in value:
                resolved.append((name + n, v))
    elif query is None:
        pass
    else:
        if isinstance(query, bool):
            query = 'true' if query is True else 'false'
        resolved.append(('', query))
    return resolved


def queryjoin(*args):
    q = []
    for query in args:
        query = resolve_query(query)
        q.extend(query)
    return q


def geturl(url, query=None):
    if query is None:
        return url
    query = urllib.parse.urlencode(query)
    parse_result = urllib.parse.urlparse(url)
    url = urllib.parse.ParseResult(
        parse_result.scheme,
        parse_result.netloc,
        parse_result.path,
        parse_result.params,
        query,
        parse_result.fragment,
    ).geturl()
    return url


def get_x_csrf_token(session: requests.Session, api_url: str = None, **kwargs):
    """
    Returns a header dictionary containing `X-CSRF-Token`.

    Resources with methods: POST, PUT, etc. often requires a `X-CSRF-Token`
    header with the value from `_csrf_token` in cookies.
    """
    if isinstance(session, requests.Session):
        # TODO: possible CookieConflictError
        # restrict to domain, path by api_url?
        return urllib.parse.unquote(session.cookies.get('_csrf_token'))
    else:
        raise TypeError


def check_status(response: requests.Response, raise_for_status: bool = True):
    error = None
    if isinstance(response, requests.Response):
        if 400 <= response.status_code < 500:
            message = '{} Client Error: {} for url: {}'.format(response.status_code,
                                                               response.reason, response.url)
            if response.status_code == 401:
                if 'WWW-Authenticate' in response.headers:
                    error = exceptions.WWWAuthenticateError(message, response=response)
                else:
                    error = exceptions.HTTPError(message, response=response)
            else:
                error = exceptions.HTTPError(message, response=response)
        elif 500 <= response.status_code < 600:
            message = '{} Server Error: {} for url: {}'.format(response.status_code,
                                                               response.reason, response.url)
            error = exceptions.HTTPError(message, response=response)
        if raise_for_status and error is not None:
            raise error
    else:
        raise TypeError('check_status() response argument must be a {!r} object, not {!r}'.format(
            'requests.Response',
            type(response).__name__,
        ))
    return error


def get_json_from_response(
    response: requests.Response,
    error: Optional[exceptions.HTTPError] = None,
    raise_for_error: bool = True,
):
    data = None
    ok = False
    tmp_error = error
    if tmp_error is not None and not isinstance(tmp_error, exceptions.HTTPError):
        raise TypeError
    if isinstance(response, requests.Response):
        text = response.text.removeprefix('while(1);')
        try:
            data = json.loads(text)
            ok = True
        except json.JSONDecodeError as e:
            if tmp_error is None:
                tmp_error = exceptions.JSONDecodeError(e.msg, e.doc, e.pos)
        if tmp_error is not None:
            if ok:
                if len(tmp_error.args) == 1:
                    tmp_error.args = ('{}\ndata: {}'.format(tmp_error.args[0], data),)
                else:
                    tmp_error.args += (data,)
                tmp_error.data = data
            if raise_for_error:
                raise tmp_error
    else:
        raise TypeError
    return data, tmp_error
