from typing import Literal, Optional, Union

from cool.api import objects, paginations, usage_rights
from cool import utils


class File(objects.Base):
    """
    https://canvas.instructure.com/doc/api/files.html#File
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('id', 'display_name')

    @property
    def id(self):
        return self.getattr('id')

    @property
    def uuid(self):
        return self.getattr('uuid')

    @property
    def folder_id(self):
        return self.getattr('folder_id')

    @property
    def display_name(self):
        return self.getattr('display_name')

    @property
    def filename(self):
        return self.getattr('filename')

    @property
    def content_type(self):
        return self.getattr('content-type')

    @property
    def url(self):
        return self.getattr('url')

    @property
    def size(self):
        """file size in bytes"""
        return self.getattr('size')

    @property
    def created_at(self):
        return self.getattr('created_at')

    @property
    def updated_at(self):
        return self.getattr('updated_at')

    @property
    def unlock_at(self):
        return self.getattr('unlock_at')

    @property
    def locked(self):
        return self.getattr('locked')

    @property
    def hidden(self):
        return self.getattr('hidden')

    @property
    def lock_at(self):
        return self.getattr('lock_at')

    @property
    def hidden_for_user(self):
        return self.getattr('hidden_for_user')

    @property
    def thumbnail_url(self):
        return self.getattr('thumbnail_url')

    @property
    def modified_at(self):
        return self.getattr('modified_at')

    @property
    def mime_class(self):
        """simplified content-type mapping"""
        return self.getattr('mime_class')

    @property
    def media_entry_id(self):
        """identifier for file in third-party transcoding service"""
        return self.getattr('media_entry_id')

    @property
    def locked_for_user(self):
        return self.getattr('locked_for_user')

    @property
    def lock_info(self):
        return self.getattr('lock_info')

    @property
    def lock_explanation(self):
        return self.getattr('lock_explanation')

    @property
    def preview_url(self):
        """
        optional: url to the document preview. This url is specific to the user
        making the api call. Only included in submission endpoints.
        """
        return self.getattr('preview_url')

    @property
    def upload_status(self):
        return self.getattr('upload_status')

    @property
    def user(self):
        """
        the user who uploaded the file or last edited its content

        https://canvas.instructure.com/doc/api/files.html#method.files.api_index
        """
        return self.getattr('user')

    @property
    def usage_rights(self):
        """
        copyright and license information for the file (see UsageRights)

        https://canvas.instructure.com/doc/api/files.html#method.files.api_index
        """
        return self.getattr('usage_rights', constructor=usage_rights.UsageRights)

    @property
    def canvadoc_session_url(self):
        return self.getattr('canvadoc_session_url')

    @property
    def crocodoc_session_url(self):
        return self.getattr('crocodoc_session_url')


def get_quota_information(
    session,
    base_url,
    context: Literal['courses', 'groups', 'users'],
    context_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get quota information

    `GET /api/v1/courses/:course_id/files/quota`

    `GET /api/v1/groups/:group_id/files/quota`

    `GET /api/v1/users/:user_id/files/quota`

    Returns the total and used storage quota for the course, group, or user.

    https://canvas.instructure.com/doc/api/files.html#method.files.api_quota
    """
    if context not in ('courses', 'groups', 'users'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/files/quota'.format(context=context,
                                                              context_id=context_id)
    query = []
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def list_files(
    session,
    base_url,
    context: Literal['courses', 'users', 'groups', 'folders'],
    context_id,
    content_types=None,
    exclude_content_types=None,
    search_term: Optional[str] = None,
    include=None,
    only=None,
    sort: Optional[str] = None,
    order: Optional[Literal['asc', 'desc']] = None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List files

    `GET /api/v1/courses/:course_id/files`

    `GET /api/v1/users/:user_id/files`

    `GET /api/v1/groups/:group_id/files`

    `GET /api/v1/folders/:id/files`

    Returns the paginated list of files for the folder or course.

    https://canvas.instructure.com/doc/api/files.html#method.files.api_index

    Returns:
        a list of Files
    """
    if context not in ('courses', 'users', 'groups', 'folders'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/files'.format(context=context, context_id=context_id)
    query = [
        ('content_types', content_types),
        ('exclude_content_types', exclude_content_types),
        ('search_term', search_term),
        ('include', include),
        ('only', only),
        ('sort', sort),
        ('order', order),
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
        constructor=File,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def get_file(
    session,
    base_url,
    context: Optional[Literal['courses', 'groups', 'users']],
    context_id,
    id,
    method: Literal['GET', 'POST'] = 'GET',
    include=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get file

    `GET /api/v1/files/:id`

    `POST /api/v1/files/:id`

    `GET /api/v1/courses/:course_id/files/:id`

    `GET /api/v1/groups/:group_id/files/:id`

    `GET /api/v1/users/:user_id/files/:id`

    Returns the standard attachment json object

    https://canvas.instructure.com/doc/api/files.html#method.files.api_show

    Returns:
        a File
    """
    if context is None:
        if method not in ('GET', 'POST'):
            raise ValueError
        url = '/api/v1/files/{id}'.format(id=id)
    elif context in ('courses', 'groups', 'users'):
        if method != 'GET':
            raise ValueError
        url = '/api/v1/{context}/{context_id}/files/{id}'.format(context=context,
                                                                 context_id=context_id,
                                                                 id=id)
    else:
        raise ValueError
    query = [
        ('include', include),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return File(data, session=session, base_url=base_url)


def update_file(
    session,
    base_url,
    id,
    name: Optional[str] = None,
    parent_folder_id: Optional[str] = None,
    on_duplicate: Optional[Literal['overwrite', 'rename']] = None,
    lock_at=None,
    unlock_at=None,
    locked: Optional[bool] = None,
    hidden: Optional[bool] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Update file

    `PUT /api/v1/files/:id`

    Update some settings on the specified file

    https://canvas.instructure.com/doc/api/files.html#method.files.api_update

    Returns:
        a File
    """
    method = 'PUT'
    url = '/api/v1/files/{id}'.format(id=id)
    query = [
        ('name', name),
        ('parent_folder_id', parent_folder_id),
        ('on_duplicate', on_duplicate),
        ('lock_at', lock_at),
        ('unlock_at', unlock_at),
        ('locked', locked),
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
    return File(data, session=session, base_url=base_url)


def delete_file(
    session,
    base_url,
    id,
    replace: Optional[bool] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Delete file

    `DELETE /api/v1/files/:id`

    Remove the specified file. Unlike most other DELETE endpoints, using this endpoint will result in comprehensive, irretrievable destruction of the file. It should be used with the `replace` parameter set to true in cases where the file preview also needs to be destroyed (such as to remove files that violate privacy laws).

    https://canvas.instructure.com/doc/api/files.html#method.files.destroy

    Returns:
        a File
    """
    method = 'DELETE'
    url = '/api/v1/files/{id}'.format(id=id)
    query = [
        ('replace', replace),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return File(data, session=session, base_url=base_url)


def reset_link_verifier(
    session,
    base_url,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Reset link verifier

    `POST /api/v1/files/:id/reset_verifier`

    Resets the link verifier. Any existing links to the file using the previous hard-coded "verifier" parameter will no longer automatically grant access.

    Must have manage files and become other users permissions

    https://canvas.instructure.com/doc/api/files.html#method.files.reset_verifier

    Returns:
        a File
    """
    method = 'POST'
    url = '/api/v1/files/{id}/reset_verifier'.format(id=id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return File(data, session=session, base_url=base_url)
