from typing import Literal, Optional, Union

from cool.api import common, paginations


def find_recipients(
    session,
    base_url,
    endpoint: Literal['search', 'conversations'] = 'search',
    search: Optional[str] = None,
    context: Optional[str] = None,
    exclude=None,
    type: Optional[Literal['user', 'context']] = None,
    user_id: Optional[int] = None,
    from_conversation_id: Optional[int] = None,
    permissions=None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    Find recipients

    `GET /api/v1/conversations/find_recipients`

    `GET /api/v1/search/recipients`

    Find valid recipients (users, courses and groups) that the current user can send messages to. The /api/v1/search/recipients path is the preferred endpoint, /api/v1/conversations/find_recipients is deprecated.

    Pagination is supported.

    https://canvas.instructure.com/doc/api/search.html#method.search.recipients

    ```
    find_recipients(<session>, <base_url>, search='')
    ```
    """
    method = 'GET'
    if endpoint == 'search':
        url = '/api/v1/search/recipients'
    elif endpoint == 'conversations':
        url = '/api/v1/conversations/find_recipients'
    else:
        raise ValueError
    query = [
        ('search', search),
        ('context', context),
        ('exclude', exclude),
        ('type', type),
        ('user_id', user_id),
        ('from_conversation_id', from_conversation_id),
        ('permissions', permissions),
        ('page', page),
        ('per_page', per_page),
    ]
    return paginations.request_json_paginated(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        pagination=pagination,
        raise_for_error=raise_for_error,
    )


def construct_course_in_dict(value, **kwargs):
    if isinstance(value, dict) and 'course' in value:
        value['course'] = common.Course(value['course'], **kwargs)
    return value


def list_all_courses(
    session,
    base_url,
    search: Optional[str] = None,
    public_only: Optional[bool] = None,
    open_enrollment_only: Optional[bool] = None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List all courses

    `GET /api/v1/search/all_courses`

    A paginated list of all courses visible in the public index

    https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
    """
    method = 'GET'
    url = '/api/v1/search/all_courses'
    query = [
        ('search', search),
        ('public_only', public_only),
        ('open_enrollment_only', open_enrollment_only),
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
        constructor=construct_course_in_dict,
        constructor_kwargs=constructor_kwargs,
        pagination=pagination,
        raise_for_error=raise_for_error,
    )
