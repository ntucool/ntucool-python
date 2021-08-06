from typing import Literal, Optional, Union

from cool.api import discussion_topics, paginations


def list_announcements(
    session,
    base_url,
    context_codes,
    start_date=None,
    end_date=None,
    active_only: bool = None,
    latest_only: bool = None,
    include=None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List announcements

    `GET /api/v1/announcements`

    Returns the paginated list of announcements for the given courses and date range. Note that a context_code field is added to the responses so you can tell which course each announcement belongs to.

    https://canvas.instructure.com/doc/api/announcements.html#method.announcements_api.index

    Returns:
        a list of DiscussionTopics
    """
    method = 'GET'
    url = '/api/v1/announcements'
    query = [
        ('context_codes', context_codes),
        ('start_date', start_date),
        ('end_date', end_date),
        ('active_only', active_only),
        ('latest_only', latest_only),
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
        constructor=discussion_topics.DiscussionTopic,
        constructor_kwargs=constructor_kwargs,
        pagination=pagination,
        raise_for_error=raise_for_error,
    )
