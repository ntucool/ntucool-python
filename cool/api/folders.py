from typing import Literal, Optional, Union

from cool.api import files, objects, paginations
from cool import utils


class Folder(objects.Base):
    """
    https://canvas.instructure.com/doc/api/files.html#Folder
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('id', 'name')

    @property
    def context_type(self):
        return self.getattr('context_type')

    @property
    def context_id(self):
        return self.getattr('context_id')

    @property
    def files_count(self):
        return self.getattr('files_count')

    @property
    def position(self):
        return self.getattr('position')

    @property
    def updated_at(self):
        return self.getattr('updated_at')

    @property
    def folders_url(self):
        return self.getattr('folders_url')

    @property
    def files_url(self):
        return self.getattr('files_url')

    @property
    def full_name(self):
        return self.getattr('full_name')

    @property
    def lock_at(self):
        return self.getattr('lock_at')

    @property
    def id(self):
        return self.getattr('id')

    @property
    def folders_count(self):
        return self.getattr('folders_count')

    @property
    def name(self):
        return self.getattr('name')

    @property
    def parent_folder_id(self):
        return self.getattr('parent_folder_id')

    @property
    def created_at(self):
        return self.getattr('created_at')

    @property
    def unlock_at(self):
        return self.getattr('unlock_at')

    @property
    def hidden(self):
        return self.getattr('hidden')

    @property
    def hidden_for_user(self):
        return self.getattr('hidden_for_user')

    @property
    def locked(self):
        return self.getattr('locked')

    @property
    def locked_for_user(self):
        return self.getattr('locked_for_user')

    @property
    def for_submissions(self):
        """
        If true, indicates this is a read-only folder containing files submitted to
        assignments
        """
        return self.getattr('for_submissions')

    @property
    def can_upload(self):
        return self.getattr('can_upload')


def list_folders(
    session,
    base_url,
    id,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List folders

    `GET /api/v1/folders/:id/folders`

    Returns the paginated list of folders in the folder.

    https://canvas.instructure.com/doc/api/files.html#method.folders.api_index

    Returns:
        a list of Folders
    """
    method = 'GET'
    url = '/api/v1/folders/{id}/folders'.format(id=id)
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
        constructor=Folder,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def list_all_folders(
    session,
    base_url,
    context: Literal['courses', 'users', 'groups'],
    context_id,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List all folders

    `GET /api/v1/courses/:course_id/folders`

    `GET /api/v1/users/:user_id/folders`

    `GET /api/v1/groups/:group_id/folders`

    Returns the paginated list of all folders for the given context. This will be returned as a flat list containing all subfolders as well.

    https://canvas.instructure.com/doc/api/files.html#method.folders.list_all_folders

    Returns:
        a list of Folders
    """
    if context not in ('courses', 'users', 'groups'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/folders'.format(context=context, context_id=context_id)
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
        constructor=Folder,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def resolve_path(
    session,
    base_url,
    context: Literal['courses', 'users', 'groups'],
    context_id,
    full_path=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Resolve path

    `GET /api/v1/courses/:course_id/folders/by_path/*full_path`

    `GET /api/v1/courses/:course_id/folders/by_path`

    `GET /api/v1/users/:user_id/folders/by_path/*full_path`

    `GET /api/v1/users/:user_id/folders/by_path`

    `GET /api/v1/groups/:group_id/folders/by_path/*full_path`

    `GET /api/v1/groups/:group_id/folders/by_path`

    Given the full path to a folder, returns a list of all Folders in the path hierarchy, starting at the root folder, and ending at the requested folder. The given path is relative to the context's root folder and does not include the root folder's name (e.g., "course files"). If an empty path is given, the context's root folder alone is returned. Otherwise, if no folder exists with the given full path, a Not Found error is returned.

    https://canvas.instructure.com/doc/api/files.html#method.folders.resolve_path

    Returns:
        a list of Folders
    """
    if context not in ('courses', 'users', 'groups'):
        raise ValueError
    method = 'GET'
    if full_path is None:
        url = '/api/v1/{context}/{context_id}/folders/by_path'.format(
            context=context,
            context_id=context_id,
        )
    else:
        url = '/api/v1/{context}/{context_id}/folders/by_path/{full_path}'.format(
            context=context,
            context_id=context_id,
            full_path=full_path,
        )
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    data = [Folder(v, session=session, base_url=base_url) for v in data]
    return data


def get_folder(
    session,
    base_url,
    context: Optional[Literal['courses', 'users', 'groups']],
    context_id,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get folder

    `GET /api/v1/courses/:course_id/folders/:id`

    `GET /api/v1/users/:user_id/folders/:id`

    `GET /api/v1/groups/:group_id/folders/:id`

    `GET /api/v1/folders/:id`

    Returns the details for a folder

    You can get the root folder from a context by using 'root' as the :id. For example, you could get the root folder for a course like:

    https://canvas.instructure.com/doc/api/files.html#method.folders.show

    Returns:
        a Folder
    """
    if context not in ('courses', 'users', 'groups', None):
        raise ValueError
    method = 'GET'
    if context is None:
        url = '/api/v1/folders/{id}'.format(id=id)
    else:
        url = '/api/v1/{context}/{context_id}/folders/{id}'.format(
            context=context,
            context_id=context_id,
            id=id,
        )
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Folder(data, session=session, base_url=base_url)


def update_folder(
    session,
    base_url,
    id,
    name: Optional[str] = None,
    parent_folder_id: Optional[str] = None,
    lock_at=None,
    unlock_at=None,
    locked: Optional[bool] = None,
    hidden: Optional[bool] = None,
    position: Optional[int] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Update folder

    `PUT /api/v1/folders/:id`

    Updates a folder

    https://canvas.instructure.com/doc/api/files.html#method.folders.update

    Returns:
        a Folder
    """
    method = 'PUT'
    url = '/api/v1/folders/{id}'.format(id=id)
    query = [
        ('name', name),
        ('parent_folder_id', parent_folder_id),
        ('lock_at', lock_at),
        ('unlock_at', unlock_at),
        ('locked', locked),
        ('hidden', hidden),
        ('position', position),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Folder(data, session=session, base_url=base_url)


def create_folder(
    session,
    base_url,
    context: Literal['courses', 'users', 'groups', 'folders'],
    context_id,
    name: Optional[str] = None,
    parent_folder_id: Optional[str] = None,
    lock_at=None,
    unlock_at=None,
    locked: Optional[bool] = None,
    hidden: Optional[bool] = None,
    position: Optional[int] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Create folder

    `POST /api/v1/courses/:course_id/folders`

    `POST /api/v1/users/:user_id/folders`

    `POST /api/v1/groups/:group_id/folders`

    `POST /api/v1/folders/:folder_id/folders`

    Creates a folder in the specified context

    https://canvas.instructure.com/doc/api/files.html#method.folders.create

    Returns:
        a Folder
    """
    if context not in ('courses', 'users', 'groups', 'folders'):
        raise ValueError
    method = 'POST'
    url = '/api/v1/{context}/{context_id}/folders'.format(context=context, context_id=context_id)
    query = [
        ('name', name),
        ('parent_folder_id', parent_folder_id),
        ('lock_at', lock_at),
        ('unlock_at', unlock_at),
        ('locked', locked),
        ('hidden', hidden),
        ('position', position),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Folder(data, session=session, base_url=base_url)


def delete_folder(
    session,
    base_url,
    id,
    force: Optional[bool] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Delete folder

    `DELETE /api/v1/folders/:id`

    Remove the specified folder. You can only delete empty folders unless you set the 'force' flag

    https://canvas.instructure.com/doc/api/files.html#method.folders.api_destroy

    Returns:
        a Folder
    """
    method = 'DELETE'
    url = '/api/v1/folders/{id}'.format(id=id)
    query = [
        ('force', force),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Folder(data, session=session, base_url=base_url)


def upload_a_file(
    session,
    base_url,
    folder_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Upload a file

    `POST /api/v1/folders/:folder_id/files`

    Upload a file to a folder.

    This API endpoint is the first step in uploading a file. See the File Upload Documentation for details on the file upload workflow.

    Only those with the "Manage Files" permission on a course or group can upload files to a folder in that course or group.

    https://canvas.instructure.com/doc/api/files.html#method.folders.create_file
    """
    method = 'POST'
    url = '/api/v1/folders/{folder_id}/files'.format(folder_id=folder_id)
    query = []
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def copy_a_file(
    session,
    base_url,
    dest_folder_id,
    source_file_id: Optional[str] = None,
    on_duplicate: Optional[Literal['overwrite', 'rename']] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Copy a file

    POST /api/v1/folders/:dest_folder_id/copy_file

    Copy a file from elsewhere in Canvas into a folder.

    Copying a file across contexts (between courses and users) is permitted, but the source and destination must belong to the same institution.

    https://canvas.instructure.com/doc/api/files.html#method.folders.copy_file

    Returns:
        a File
    """
    method = 'POST'
    url = '/api/v1/folders/{dest_folder_id}/copy_file'.format(dest_folder_id=dest_folder_id)
    query = [
        ('source_file_id', source_file_id),
        ('on_duplicate', on_duplicate),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return files.File(data, session=session, base_url=base_url)


def copy_a_folder(
    session,
    base_url,
    dest_folder_id,
    source_folder_id: Optional[str] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Copy a folder

    `POST /api/v1/folders/:dest_folder_id/copy_folder`

    Copy a folder (and its contents) from elsewhere in Canvas into a folder.

    Copying a folder across contexts (between courses and users) is permitted, but the source and destination must belong to the same institution. If the source and destination folders are in the same context, the source folder may not contain the destination folder. A folder will be renamed at its destination if another folder with the same name already exists.

    https://canvas.instructure.com/doc/api/files.html#method.folders.copy_folder

    Returns:
        a Folder
    """
    method = 'POST'
    url = '/api/v1/folders/{dest_folder_id}/copy_folder'.format(dest_folder_id=dest_folder_id)
    query = [
        ('source_folder_id', source_folder_id),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Folder(data, session=session, base_url=base_url)


def get_uploaded_media_folder_for_user(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get uploaded media folder for user

    `GET /api/v1/courses/:course_id/folders/media`

    `GET /api/v1/groups/:group_id/folders/media`

    Returns the details for a designated upload folder that the user has rights to upload to, and creates it if it doesn't exist.

    If the current user does not have the permissions to manage files in the course or group, the folder will belong to the current user directly.

    https://canvas.instructure.com/doc/api/files.html#method.folders.media_folder

    Returns:
        a Folder
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/folders/media'.format(context=context,
                                                                context_id=context_id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Folder(data, session=session, base_url=base_url)
