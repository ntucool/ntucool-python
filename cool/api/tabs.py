from typing import Literal, Optional, Union

from cool import utils
from cool.api import objects, paginations


class Tab(objects.Base):
    """
    https://canvas.instructure.com/doc/api/tabs.html#Tab
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('id', 'label')

    @property
    def html_url(self):
        return self.getattr('html_url')

    @property
    def id(self):
        return self.getattr('id')

    @property
    def label(self):
        return self.getattr('label')

    @property
    def type(self):
        return self.getattr('type')

    @property
    def hidden(self):
        """only included if true"""
        return self.getattr('hidden')

    @property
    def visibility(self):
        """possible values are: public, members, admins, and none"""
        return self.getattr('visibility')

    @property
    def position(self):
        """1 based"""
        return self.getattr('position')

    @property
    def full_url(self):
        """1 based"""
        return self.getattr('full_url')


def list_available_tabs_for_a_course_or_group(
    session,
    base_url,
    context: Literal['accounts', 'courses', 'groups', 'users'],
    context_id,
    include=None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List available tabs for a course or group

    `GET /api/v1/accounts/:account_id/tabs`

    `GET /api/v1/courses/:course_id/tabs`

    `GET /api/v1/groups/:group_id/tabs`

    `GET /api/v1/users/:user_id/tabs`

    Returns a paginated list of navigation tabs available in the current context.

    https://canvas.instructure.com/doc/api/tabs.html#method.tabs.index

    NTU COOL does not seem to support pagination.
    """
    if context not in ('accounts', 'courses', 'groups', 'users'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/tabs'.format(context=context, context_id=context_id)
    query = [
        ('include', include),
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
        constructor=Tab,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def update_a_tab_for_a_course(
    session,
    base_url,
    course_id,
    tab_id,
    position: Optional[int] = None,
    hidden: Optional[bool] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Update a tab for a course

    `PUT /api/v1/courses/:course_id/tabs/:tab_id`

    Home and Settings tabs are not manageable, and can't be hidden or moved

    Returns a tab object

    https://canvas.instructure.com/doc/api/tabs.html#method.tabs.update

    Returns:
        a Tab
    """
    method = 'PUT'
    url = '/api/v1/courses/{course_id}/tabs/{tab_id}'.format(course_id=course_id, tab_id=tab_id)
    query = [
        ('position', position),
        ('hidden', hidden),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Tab(data, session=session, base_url=base_url)
