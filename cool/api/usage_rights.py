from typing import Literal, Optional, Union

from cool.api import objects, paginations
from cool import utils


class UsageRights(objects.Simple):
    """
    Describes the copyright and license information for a File

    https://canvas.instructure.com/doc/api/files.html#UsageRights
    """

    def __init__(self, attributes: dict) -> None:
        super().__init__(attributes=attributes)

    @property
    def legal_copyright(self):
        """Copyright line for the file"""
        return self.getattr('legal_copyright')

    @property
    def use_justification(self):
        """
        Justification for using the file in a Canvas course. Valid values are
        'own_copyright', 'public_domain', 'used_by_permission', 'fair_use',
        'creative_commons'
        """
        return self.getattr('use_justification')

    @property
    def license(self):
        """License identifier for the file."""
        return self.getattr('license')

    @property
    def license_name(self):
        """Readable license name"""
        return self.getattr('license_name')

    @property
    def message(self):
        """Explanation of the action performed"""
        return self.getattr('message')

    @property
    def file_ids(self):
        """List of ids of files that were updated"""
        return self.getattr('file_ids')


class License(objects.Simple):
    """
    https://canvas.instructure.com/doc/api/files.html#License
    """

    def __init__(self, attributes: dict) -> None:
        super().__init__(attributes=attributes)

    repr_names = ('id', 'name')

    @property
    def id(self):
        """a short string identifying the license"""
        return self.getattr('id')

    @property
    def name(self):
        """the name of the license"""
        return self.getattr('name')

    @property
    def url(self):
        """http://creativecommons.org/licenses/by-sa/4.0"""
        return self.getattr('url')


def set_usage_rights(
    session,
    base_url,
    context: Literal['courses', 'groups', 'users'],
    context_id,
    usage_rights,
    file_ids=None,
    folder_ids=None,
    publish: Optional[bool] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Set usage rights

    `PUT /api/v1/courses/:course_id/usage_rights`

    `PUT /api/v1/groups/:group_id/usage_rights`

    `PUT /api/v1/users/:user_id/usage_rights`

    Sets copyright and license information for one or more files

    https://canvas.instructure.com/doc/api/files.html#method.usage_rights.set_usage_rights

    Returns:
        a UsageRights
    """
    if context not in ('courses', 'groups', 'users'):
        raise ValueError
    method = 'PUT'
    url = '/api/v1/{context}/{context_id}/usage_rights'.format(context=context,
                                                               context_id=context_id)
    query = [
        ('file_ids', file_ids),
        ('folder_ids', folder_ids),
        ('publish', publish),
        ('usage_rights', usage_rights),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return UsageRights(data)


def remove_usage_rights(
    session,
    base_url,
    context: Literal['courses', 'groups', 'users'],
    context_id,
    file_ids=None,
    folder_ids=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Remove usage rights

    `DELETE /api/v1/courses/:course_id/usage_rights`

    `DELETE /api/v1/groups/:group_id/usage_rights`

    `DELETE /api/v1/users/:user_id/usage_rights`

    Removes copyright and license information associated with one or more files

    https://canvas.instructure.com/doc/api/files.html#method.usage_rights.remove_usage_rights
    """
    if context not in ('courses', 'groups', 'users'):
        raise ValueError
    method = 'DELETE'
    url = '/api/v1/{context}/{context_id}/usage_rights'.format(context=context,
                                                               context_id=context_id)
    query = [
        ('file_ids', file_ids),
        ('folder_ids', folder_ids),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return data


def list_licenses(
    session,
    base_url,
    context: Literal['courses', 'groups', 'users'],
    context_id,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List licenses

    `GET /api/v1/courses/:course_id/content_licenses`

    `GET /api/v1/groups/:group_id/content_licenses`

    `GET /api/v1/users/:user_id/content_licenses`

    A paginated list of licenses that can be applied

    https://canvas.instructure.com/doc/api/files.html#method.usage_rights.licenses

    NTU COOL does not seem to support pagination.

    Returns:
        a list of Licenses
    """
    if context not in ('courses', 'groups', 'users'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/content_licenses'.format(context=context,
                                                                   context_id=context_id)
    query = [
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
        constructor=License,
        raise_for_error=raise_for_error,
    )
