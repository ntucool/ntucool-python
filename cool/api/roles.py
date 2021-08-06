from typing import Literal, Optional, Union

from cool import utils
from cool.api import objects, paginations


class RolePermissions(objects.Simple):
    """
    https://canvas.instructure.com/doc/api/roles.html#RolePermissions
    """

    def __init__(self, attributes: dict) -> None:
        super().__init__(attributes=attributes)

    @property
    def enabled(self):
        """Whether the role has the permission"""
        return self.getattr('enabled')

    @property
    def locked(self):
        """Whether the permission is locked by this role"""
        return self.getattr('locked')

    @property
    def applies_to_self(self):
        """
        Whether the permission applies to the account this role is in. Only present
        if enabled is true
        """
        return self.getattr('applies_to_self')

    @property
    def applies_to_descendants(self):
        """
        Whether the permission cascades down to sub accounts of the account this role
        is in. Only present if enabled is true
        """
        return self.getattr('applies_to_descendants')

    @property
    def readonly(self):
        """
        Whether the permission can be modified in this role (i.e. whether the
        permission is locked by an upstream role).
        """
        return self.getattr('readonly')

    @property
    def explicit(self):
        """
        Whether the value of enabled is specified explicitly by this role, or
        inherited from an upstream role.
        """
        return self.getattr('explicit')

    @property
    def prior_default(self):
        """
        The value that would have been inherited from upstream if the role had not
        explicitly set a value. Only present if explicit is true.
        """
        return self.getattr('prior_default')


class Role(objects.Base):
    """
    https://canvas.instructure.com/doc/api/roles.html#Role
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('label',)

    @property
    def label(self):
        """The label of the role."""
        return self.getattr('label')

    @property
    def role(self):
        """The label of the role. (Deprecated alias for 'label')"""
        return self.getattr('role')

    @property
    def base_role_type(self):
        """
        The role type that is being used as a base for this role. For account-level
        roles, this is 'AccountMembership'. For course-level roles, it is an
        enrollment type.
        """
        return self.getattr('base_role_type')

    @property
    def account(self):
        """JSON representation of the account the role is in."""
        return self.getattr('account')

    @property
    def workflow_state(self):
        """The state of the role: 'active', 'inactive', or 'built_in'"""
        return self.getattr('workflow_state')

    @property
    def permissions(self):
        """
        A dictionary of permissions keyed by name (see permissions input parameter in
        the 'Create a role' API).
        """
        return self.getattr('permissions')


def list_roles(
    session,
    base_url,
    account_id,
    state=None,
    show_inherited: Optional[bool] = None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List roles

    `GET /api/v1/accounts/:account_id/roles`

    A paginated list of the roles available to an account.

    https://canvas.instructure.com/doc/api/roles.html#method.role_overrides.api_index

    Returns:
        a list of Roles
    """
    method = 'GET'
    url = '/api/v1/accounts/{account_id}/roles'.format(account_id=account_id)
    query = [
        ('state', state),
        ('show_inherited', show_inherited),
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
        constructor=Role,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def get_a_single_role(
    session,
    base_url,
    account_id,
    id,
    role: Optional[str] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get a single role

    `GET /api/v1/accounts/:account_id/roles/:id`

    Retrieve information about a single role

    https://canvas.instructure.com/doc/api/roles.html#method.role_overrides.show

    Returns:
        a Role
    """
    method = 'GET'
    url = '/api/v1/accounts/{account_id}/roles/{id}'.format(account_id=account_id, id=id)
    query = [
        ('role', role),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Role(data, session=session, base_url=base_url)


def create_a_new_role(
    session,
    base_url,
    account_id,
    label: Optional[str] = None,
    role: Optional[str] = None,
    base_role_type: Optional[Literal['AccountMembership', 'StudentEnrollment', 'TeacherEnrollment',
                                     'TaEnrollment', 'ObserverEnrollment',
                                     'DesignerEnrollment']] = None,
    permissions=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Create a new role

    `POST /api/v1/accounts/:account_id/roles`

    Create a new course-level or account-level role.

    https://canvas.instructure.com/doc/api/roles.html#method.role_overrides.add_role

    Returns:
        a Role
    """
    method = 'POST'
    url = '/api/v1/accounts/{account_id}/roles'.format(account_id=account_id)
    query = [
        ('label', label),
        ('role', role),
        ('base_role_type', base_role_type),
        ('permissions', permissions),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Role(data, session=session, base_url=base_url)


def deactivate_a_role(
    session,
    base_url,
    account_id,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Deactivate a role

    `DELETE /api/v1/accounts/:account_id/roles/:id`

    Deactivates a custom role.  This hides it in the user interface and prevents it from being assigned to new users.  Existing users assigned to the role will continue to function with the same permissions they had previously. Built-in roles cannot be deactivated.

    https://canvas.instructure.com/doc/api/roles.html#method.role_overrides.remove_role

    Returns:
        a Role
    """
    method = 'DELETE'
    url = '/api/v1/accounts/{account_id}/roles/{id}'.format(account_id=account_id, id=id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Role(data, session=session, base_url=base_url)


def activate_a_role(
    session,
    base_url,
    account_id,
    id,
    label: Optional[str] = None,
    permissions=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Activate a role

    `POST /api/v1/accounts/:account_id/roles/:id/activate`

    Re-activates an inactive role (allowing it to be assigned to new users)

    https://canvas.instructure.com/doc/api/roles.html#method.role_overrides.activate_role

    Returns:
        a Role
    """
    method = 'POST'
    url = '/api/v1/accounts/{account_id}/roles/{id}/activate'.format(account_id=account_id, id=id)
    query = [
        ('label', label),
        ('permissions', permissions),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Role(data, session=session, base_url=base_url)


def update_a_role(
    session,
    base_url,
    account_id,
    id,
    role=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Update a role

    `PUT /api/v1/accounts/:account_id/roles/:id`

    Update permissions for an existing role.

    Recognized roles are:

    https://canvas.instructure.com/doc/api/roles.html#method.role_overrides.update

    Returns:
        a Role
    """
    method = 'PUT'
    url = '/api/v1/accounts/{account_id}/roles/{id}'.format(account_id=account_id, id=id)
    query = [
        ('role', role),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Role(data, session=session, base_url=base_url)
