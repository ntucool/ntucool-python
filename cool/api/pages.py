from typing import Literal, Optional, Union

from cool import utils
from cool.api import objects, paginations


class Page(objects.Base):
    """
    https://canvas.instructure.com/doc/api/pages.html#Page
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('page_id', 'url', 'title')

    @property
    def url(self):
        """the unique locator for the page"""
        return self.getattr('url')

    @property
    def title(self):
        """the title of the page"""
        return self.getattr('title')

    @property
    def created_at(self):
        """the creation date for the page"""
        return self.getattr('created_at')

    @property
    def updated_at(self):
        """the date the page was last updated"""
        return self.getattr('updated_at')

    @property
    def hide_from_students(self):
        """
        (DEPRECATED) whether this page is hidden from students (note: this is always
        reflected as the inverse of the published value)
        """
        return self.getattr('hide_from_students')

    @property
    def editing_roles(self):
        """
        roles allowed to edit the page; comma-separated list comprising a combination
        of 'teachers', 'students', 'members', and/or 'public' if not supplied, course
        defaults are used
        """
        return self.getattr('editing_roles')

    @property
    def last_edited_by(self):
        """
        the User who last edited the page (this may not be present if the page was
        imported from another system)
        """
        return self.getattr('last_edited_by')

    @property
    def body(self):
        """
        the page content, in HTML (present when requesting a single page; omitted
        when listing pages)
        """
        return self.getattr('body')

    @property
    def published(self):
        """whether the page is published (true) or draft state (false)."""
        return self.getattr('published')

    @property
    def front_page(self):
        """whether this page is the front page for the wiki"""
        return self.getattr('front_page')

    @property
    def locked_for_user(self):
        """Whether or not this is locked for the user."""
        return self.getattr('locked_for_user')

    @property
    def lock_info(self):
        """
        (Optional) Information for the user about the lock. Present when
        locked_for_user is true.
        """
        return self.getattr('lock_info')

    @property
    def lock_explanation(self):
        """
        (Optional) An explanation of why this is locked for the user. Present when
        locked_for_user is true.
        """
        return self.getattr('lock_explanation')

    @property
    def page_id(self):
        return self.getattr('page_id')

    @property
    def html_url(self):
        return self.getattr('html_url')

    @property
    def todo_date(self):
        return self.getattr('todo_date')


class PageRevision(objects.Base):
    """
    https://canvas.instructure.com/doc/api/pages.html#PageRevision
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    @property
    def revision_id(self):
        """an identifier for this revision of the page"""
        return self.getattr('revision_id')

    @property
    def updated_at(self):
        """the time when this revision was saved"""
        return self.getattr('updated_at')

    @property
    def latest(self):
        """whether this is the latest revision or not"""
        return self.getattr('latest')

    @property
    def edited_by(self):
        """
        the User who saved this revision, if applicable (this may not be present if
        the page was imported from another system)
        """
        return self.getattr('edited_by')

    @property
    def url(self):
        """
        the following fields are not included in the index action and may be omitted
        from the show action via summary=1 the historic url of the page
        """
        return self.getattr('url')

    @property
    def title(self):
        """the historic page title"""
        return self.getattr('title')

    @property
    def body(self):
        """the historic page contents"""
        return self.getattr('body')


def show_front_page(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Show front page

    `GET /api/v1/courses/:course_id/front_page`

    `GET /api/v1/groups/:group_id/front_page`

    Retrieve the content of the front page

    https://canvas.instructure.com/doc/api/pages.html#method.wiki_pages_api.show_front_page

    Returns:
        a Page
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/front_page'.format(context=context, context_id=context_id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Page(data, session=session, base_url=base_url)


def duplicate_page(
    session,
    base_url,
    course_id,
    url,
    params=None,
    raise_for_error: bool = True,
):
    """
    Duplicate page

    `POST /api/v1/courses/:course_id/pages/:url/duplicate`

    Duplicate a wiki page

    https://canvas.instructure.com/doc/api/pages.html#method.wiki_pages_api.duplicate

    Returns:
        a Page
    """
    method = 'POST'
    _url = '/api/v1/courses/{course_id}/pages/{url}/duplicate'.format(course_id=course_id, url=url)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        _url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Page(data, session=session, base_url=base_url)


def update_or_create_front_page(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    wiki_page=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Update/create front page

    `PUT /api/v1/courses/:course_id/front_page`

    `PUT /api/v1/groups/:group_id/front_page`

    Update the title or contents of the front page

    https://canvas.instructure.com/doc/api/pages.html#method.wiki_pages_api.update_front_page

    Returns:
        a Page
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'PUT'
    url = '/api/v1/{context}/{context_id}/front_page'.format(context=context, context_id=context_id)
    query = [
        ('wiki_page', wiki_page),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Page(data, session=session, base_url=base_url)


def list_pages(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    sort: Optional[Literal['title', 'created_at', 'updated_at']] = None,
    order: Optional[Literal['asc', 'desc']] = None,
    search_term: Optional[str] = None,
    published: Optional[bool] = None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List pages

    `GET /api/v1/courses/:course_id/pages`

    `GET /api/v1/groups/:group_id/pages`

    A paginated list of the wiki pages associated with a course or group

    https://canvas.instructure.com/doc/api/pages.html#method.wiki_pages_api.index

    Returns:
        a list of Pages
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/pages'.format(context=context, context_id=context_id)
    query = [
        ('sort', sort),
        ('order', order),
        ('search_term', search_term),
        ('published', published),
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
        constructor=Page,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def create_page(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    wiki_page=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Create page

    `POST /api/v1/courses/:course_id/pages`

    `POST /api/v1/groups/:group_id/pages`

    Create a new wiki page

    https://canvas.instructure.com/doc/api/pages.html#method.wiki_pages_api.create

    Returns:
        a Page
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'POST'
    url = '/api/v1/{context}/{context_id}/front_page'.format(context=context, context_id=context_id)
    query = [
        ('wiki_page', wiki_page),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Page(data, session=session, base_url=base_url)


def show_page(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    url,
    params=None,
    raise_for_error: bool = True,
):
    """
    Show page

    `GET /api/v1/courses/:course_id/pages/:url`

    `GET /api/v1/groups/:group_id/pages/:url`

    Retrieve the content of a wiki page

    https://canvas.instructure.com/doc/api/pages.html#method.wiki_pages_api.show

    Returns:
        a Page
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'GET'
    _url = '/api/v1/{context}/{context_id}/pages/{url}'.format(context=context,
                                                               context_id=context_id,
                                                               url=url)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        _url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Page(data, session=session, base_url=base_url)


def update_or_create_page(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    url,
    wiki_page=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Update/create page

    `PUT /api/v1/courses/:course_id/pages/:url`

    `PUT /api/v1/groups/:group_id/pages/:url`

    Update the title or contents of a wiki page

    https://canvas.instructure.com/doc/api/pages.html#method.wiki_pages_api.update

    Returns:
        a Page
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'PUT'
    _url = '/api/v1/{context}/{context_id}/pages/{url}'.format(context=context,
                                                               context_id=context_id,
                                                               url=url)
    query = [
        ('wiki_page', wiki_page),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        _url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Page(data, session=session, base_url=base_url)


def delete_page(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    url,
    params=None,
    raise_for_error: bool = True,
):
    """
    Delete page

    `DELETE /api/v1/courses/:course_id/pages/:url`

    `DELETE /api/v1/groups/:group_id/pages/:url`

    Delete a wiki page

    https://canvas.instructure.com/doc/api/pages.html#method.wiki_pages_api.destroy

    Returns:
        a Page
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'DELETE'
    _url = '/api/v1/{context}/{context_id}/pages/{url}'.format(context=context,
                                                               context_id=context_id,
                                                               url=url)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        _url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Page(data, session=session, base_url=base_url)


def list_revisions():
    """
    List revisions

    `GET /api/v1/courses/:course_id/pages/:url/revisions`

    `GET /api/v1/groups/:group_id/pages/:url/revisions`

    A paginated list of the revisions of a page. Callers must have update rights on the page in order to see page history.

    https://canvas.instructure.com/doc/api/pages.html#method.wiki_pages_api.revisions

    Returns:
        a list of PageRevisions
    """
    raise NotImplementedError


def show_revision():
    """
    Show revision

    `GET /api/v1/courses/:course_id/pages/:url/revisions/latest`

    `GET /api/v1/groups/:group_id/pages/:url/revisions/latest`

    `GET /api/v1/courses/:course_id/pages/:url/revisions/:revision_id`

    `GET /api/v1/groups/:group_id/pages/:url/revisions/:revision_id`

    Retrieve the metadata and optionally content of a revision of the page. Note that retrieving historic versions of pages requires edit rights.

    https://canvas.instructure.com/doc/api/pages.html#method.wiki_pages_api.show_revision

    Returns:
        a PageRevision
    """
    raise NotImplementedError


def revert_to_revision():
    """
    Revert to revision

    `POST /api/v1/courses/:course_id/pages/:url/revisions/:revision_id`

    `POST /api/v1/groups/:group_id/pages/:url/revisions/:revision_id`

    Revert a page to a prior revision.

    https://canvas.instructure.com/doc/api/pages.html#method.wiki_pages_api.revert

    Returns:
        a PageRevision
    """
    raise NotImplementedError
