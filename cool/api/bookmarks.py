from typing import Literal, Optional, Union

from cool import utils
from cool.api import objects, paginations


class Bookmark(objects.Base):
    """
    https://canvas.instructure.com/doc/api/bookmarks.html#Bookmark
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('id', 'name')

    @property
    def id(self):
        return self.getattr('id')

    @property
    def name(self):
        return self.getattr('name')

    @property
    def url(self):
        return self.getattr('url')

    @property
    def position(self):
        return self.getattr('position')

    @property
    def data(self):
        return self.getattr('data')


def list_bookmarks(
    session,
    base_url,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List bookmarks

    `GET /api/v1/users/self/bookmarks`

    Returns the paginated list of bookmarks.

    https://canvas.instructure.com/doc/api/bookmarks.html#method.bookmarks/bookmarks.index

    Returns:
        a list of Bookmarks
    """
    method = 'GET'
    url = '/api/v1/users/self/bookmarks'
    query = [
        ('page', page),
        ('per_page', per_page),
    ]
    constructor_kwargs = {
        'session': session,
        'base_url': base_url,
    }
    return paginations.request_json_paginated(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        pagination=pagination,
        constructor=Bookmark,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def create_bookmark(
    session,
    base_url,
    name: Optional[str] = None,
    url: Optional[str] = None,
    position: Optional[int] = None,
    data: Optional[str] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Create bookmark

    `POST /api/v1/users/self/bookmarks`

    Creates a bookmark.

    https://canvas.instructure.com/doc/api/bookmarks.html#method.bookmarks/bookmarks.create

    Returns:
        a Bookmark
    """
    method = 'GET'
    _url = '/api/v1/users/self/bookmarks'
    query = [
        ('name', name),
        ('url', url),
        ('position', position),
        ('data', data),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        _url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Bookmark(data, session=session, base_url=base_url)


def get_bookmark(
    session,
    base_url,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get bookmark

    `GET /api/v1/users/self/bookmarks/:id`

    Returns the details for a bookmark.

    https://canvas.instructure.com/doc/api/bookmarks.html#method.bookmarks/bookmarks.show

    Returns:
        a Bookmark
    """
    method = 'GET'
    url = '/api/v1/users/self/bookmarks/{id}'.format(id=id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Bookmark(data, session=session, base_url=base_url)


def update_bookmark(
    session,
    base_url,
    id,
    params=None,
    name: Optional[str] = None,
    url: Optional[str] = None,
    position: Optional[int] = None,
    data: Optional[str] = None,
    raise_for_error: bool = True,
):
    """
    Update bookmark

    `PUT /api/v1/users/self/bookmarks/:id`

    Updates a bookmark

    https://canvas.instructure.com/doc/api/bookmarks.html#method.bookmarks/bookmarks.update

    Returns:
        a Folder
    """
    method = 'PUT'
    _url = '/api/v1/users/self/bookmarks/{id}'.format(id=id)
    query = [
        ('name', name),
        ('url', url),
        ('position', position),
        ('data', data),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        _url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Bookmark(data, session=session, base_url=base_url)


def delete_bookmark(
    session,
    base_url,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Delete bookmark

    `DELETE /api/v1/users/self/bookmarks/:id`

    Deletes a bookmark

    https://canvas.instructure.com/doc/api/bookmarks.html#method.bookmarks/bookmarks.destroy
    """
    method = 'GET'
    url = '/api/v1/users/self/bookmarks/{id}'.format(id=id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return data
