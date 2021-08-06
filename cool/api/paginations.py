import collections.abc
import pprint
import urllib.parse
import warnings

from typing import Generic, Literal, Optional, TypeVar, Union

import requests

from cool import utils

warnings.filterwarnings('always')

T = TypeVar('T')


class Pagination(Generic[T]):
    """https://canvas.instructure.com/doc/api/file.pagination.html"""

    def __init__(
        self,
        session: requests.Session,
        method: str,
        links: Union[str, dict[str, dict[str, str]]],
        constructor: Optional[collections.abc.Callable[..., T]] = None,
        constructor_kwargs: Optional[dict] = None,
        **kwargs,
    ) -> None:
        self.session = session
        if isinstance(links, str):
            links = {'next': {'url': links, 'rel': 'next'}}
        self.links = links
        self.method = method
        self.constructor = constructor
        self.constructor_kwargs = {} if constructor_kwargs is None else constructor_kwargs
        self.kwargs = kwargs
        self.values = []

    def __iter__(self) -> collections.abc.Iterator[T]:
        for value in self.values:
            yield value
        while 'next' in self.links:
            pprint.pprint(self.links)
            values = self.next()
            for value in values:
                yield value
        pprint.pprint(self.links)

    def __len__(self) -> int:
        list(iter(self))
        return len(self.values)

    def request(self, key) -> tuple[dict, list[T]]:
        url = self.links[key]
        url = url['url']
        values, response = utils.request_json(
            self.session,
            self.method,
            url,
            url=None,
            queries=None,
            raise_for_error=True,
            return_response=True,
            return_error=False,
            **self.kwargs,
        )
        if response.links == {}:
            message = '{} {} {} with response.links: {}'.format(self, self.method,
                                                                response.request.url,
                                                                response.links)
            warnings.warn(message, category=RuntimeWarning)
        if self.constructor is not None:
            values = [
                value if value is None else self.constructor(value, **self.constructor_kwargs)
                for value in values
            ]
        return response.links, values

    def current(self, update=True):
        links, values = self.request('current')
        if update is True:
            self.links = links
        return values

    def next(self, update=True):
        links, values = self.request('next')
        if update is True:
            self.links = links
            self.values.extend(values)
        return values

    def prev(self, update=True):
        links, values = self.request('prev')
        if update is True:
            self.links = links
            self.values[:0] = values
        return values

    def first(self, update=True):
        links, values = self.request('first')
        if update is True:
            self.links = links
        return values

    def last(self, update=True):
        links, values = self.request('last')
        if update is True:
            self.links = links
        return values

    def __repr__(self) -> str:
        if self.constructor is None:
            return super().__repr__()
        format_string = self.__class__.__name__
        info = []
        if isinstance(self.constructor, type) and hasattr(self.constructor, '__name__'):
            info.append(f'type={self.constructor.__name__}')
        else:
            info.append(f'constructor={self.constructor}')
        format_string += '(' + ', '.join(info) + ')'
        return format_string


def request_json_paginated(
    session: requests.Session,
    method: str,
    base: str,
    url: str,
    queries=None,
    pagination: Union[bool, Literal['current']] = 'current',
    constructor: Optional[collections.abc.Callable[..., T]] = None,
    constructor_kwargs: Optional[dict] = None,
    raise_for_error: bool = True,
    **kwargs,
):
    url = urllib.parse.urljoin(base, url)
    queries = [] if queries is None else queries
    query = utils.queryjoin(*queries)
    return _request_json_paginated(
        session,
        method,
        url,
        query=query,
        pagination=pagination,
        constructor=constructor,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
        **kwargs,
    )


def _request_json_paginated(
    session: requests.Session,
    method: str,
    url: str,
    query=None,
    pagination: Union[bool, Literal['current']] = 'current',
    constructor: Optional[collections.abc.Callable[..., T]] = None,
    constructor_kwargs: Optional[dict] = None,
    raise_for_error: bool = True,
    **kwargs,
) -> Union[Pagination[T], list[T]]:
    url = utils.geturl(url, query)
    constructor_kwargs = {} if constructor_kwargs is None else constructor_kwargs
    if pagination is True:
        return Pagination(
            session,
            method,
            url,
            constructor=constructor,
            constructor_kwargs=constructor_kwargs,
            **kwargs,
        )
    elif pagination is False:
        return list(
            Pagination(
                session,
                method,
                url,
                constructor=constructor,
                constructor_kwargs=constructor_kwargs,
                **kwargs,
            ))
    elif pagination == 'current':
        values, error = utils.request_json(
            session,
            method,
            url,
            url=None,
            queries=None,
            raise_for_error=raise_for_error,
            return_response=False,
            return_error=True,
            **kwargs,
        )
        if error is None and constructor is not None:
            values = [constructor(value, **constructor_kwargs) for value in values]
        return values
    else:
        raise ValueError
