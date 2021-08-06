from typing import Literal, Optional, Union

from cool import utils
from cool.api import common, objects, paginations


class PairingCode(objects.Simple):
    """
    A code used for linking a user to a student to observe them.

    https://canvas.instructure.com/doc/api/user_observees.html#PairingCode
    """

    def __init__(self, attributes: dict) -> None:
        super().__init__(attributes=attributes)

    @property
    def user_id(self):
        """The ID of the user."""
        return self.getattr('user_id')

    @property
    def code(self):
        """The actual code to be sent to other APIs"""
        return self.getattr('code')

    @property
    def expires_at(self):
        """When the code expires"""
        return self.getattr('expires_at')

    @property
    def workflow_state(self):
        """The current status of the code"""
        return self.getattr('workflow_state')


def list_observees(
    session,
    base_url,
    user_id,
    include=None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List observees

    `GET /api/v1/users/:user_id/observees`

    A paginated list of the users that the given user is observing.

    Note: all users are allowed to list their own observees. Administrators can list other users' observees.

    The returned observees will include an attribute "observation_link_root_account_ids", a list of ids for the root accounts the observer and observee are linked on. The observer will only be able to observe in courses associated with these root accounts.

    https://canvas.instructure.com/doc/api/user_observees.html#method.user_observees.index

    Returns:
        a list of Users
    """
    method = 'GET'
    url = '/api/v1/users/{user_id}/observees'.format(user_id=user_id)
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
        constructor=common.User,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def list_observers(
    session,
    base_url,
    user_id,
    include=None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List observers

    `GET /api/v1/users/:user_id/observers`

    A paginated list of the users that the given user is observing.

    Note: all users are allowed to list their own observees. Administrators can list other users' observees.

    The returned observees will include an attribute "observation_link_root_account_ids", a list of ids for the root accounts the observer and observee are linked on. The observer will only be able to observe in courses associated with these root accounts.

    https://canvas.instructure.com/doc/api/user_observees.html#method.user_observees.observers

    Returns:
        a list of Users
    """
    method = 'GET'
    url = '/api/v1/users/{user_id}/observers'.format(user_id=user_id)
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
        constructor=common.User,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def add_an_observee_with_credentials(
    session,
    base_url,
    user_id,
    observee=None,
    access_token: Optional[str] = None,
    pairing_code: Optional[str] = None,
    root_account_id: Optional[int] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Add an observee with credentials

    `POST /api/v1/users/:user_id/observees`

    Register the given user to observe another user, given the observee's credentials.

    Note: all users are allowed to add their own observees, given the observee's credentials or access token are provided. Administrators can add observees given credentials, access token or the observee's id.

    https://canvas.instructure.com/doc/api/user_observees.html#method.user_observees.create

    Returns:
        a User
    """
    method = 'POST'
    url = '/api/v1/users/{user_id}/observees'.format(user_id=user_id)
    query = [
        ('observee', observee),
        ('access_token', access_token),
        ('pairing_code', pairing_code),
        ('root_account_id', root_account_id),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return common.User(data, session=session, base_url=base_url)


def show_an_observee(
    session,
    base_url,
    user_id,
    observee_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Show an observee

    `GET /api/v1/users/:user_id/observees/:observee_id`

    Gets information about an observed user.

    Note: all users are allowed to view their own observees.

    https://canvas.instructure.com/doc/api/user_observees.html#method.user_observees.show

    Returns:
        a User
    """
    method = 'GET'
    url = '/api/v1/users/{user_id}/observees/{observee_id}'.format(user_id=user_id,
                                                                   observee_id=observee_id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return common.User(data, session=session, base_url=base_url)


def show_an_observer(
    session,
    base_url,
    user_id,
    observer_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Show an observer

    `GET /api/v1/users/:user_id/observers/:observer_id`

    Gets information about an observed user.

    Note: all users are allowed to view their own observers.

    https://canvas.instructure.com/doc/api/user_observees.html#method.user_observees.show_observer

    Returns:
        a User
    """
    method = 'GET'
    url = '/api/v1/users/{user_id}/observers/{observer_id}'.format(user_id=user_id,
                                                                   observer_id=observer_id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return common.User(data, session=session, base_url=base_url)


def add_an_observee(
    session,
    base_url,
    user_id,
    observee_id,
    root_account_id: Optional[int] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Add an observee

    `PUT /api/v1/users/:user_id/observees/:observee_id`

    Registers a user as being observed by the given user.

    https://canvas.instructure.com/doc/api/user_observees.html#method.user_observees.update

    Returns:
        a User
    """
    method = 'PUT'
    url = '/api/v1/users/{user_id}/observees/{observee_id}'.format(user_id=user_id,
                                                                   observee_id=observee_id)
    query = [
        ('root_account_id', root_account_id),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return common.User(data, session=session, base_url=base_url)


def remove_an_observee(
    session,
    base_url,
    user_id,
    observee_id,
    root_account_id: Optional[int] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Remove an observee

    `DELETE /api/v1/users/:user_id/observees/:observee_id`

    Unregisters a user as being observed by the given user.

    https://canvas.instructure.com/doc/api/user_observees.html#method.user_observees.destroy

    Returns:
        a User
    """
    method = 'DELETE'
    url = '/api/v1/users/{user_id}/observees/{observee_id}'.format(user_id=user_id,
                                                                   observee_id=observee_id)
    query = [
        ('root_account_id', root_account_id),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return common.User(data, session=session, base_url=base_url)


def create_observer_pairing_code(
    session,
    base_url,
    user_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Create observer pairing code

    `POST /api/v1/users/:user_id/observer_pairing_codes`

    If the user is a student, will generate a code to be used with self registration or observees APIs to link another user to this student.

    https://canvas.instructure.com/doc/api/user_observees.html#method.observer_pairing_codes_api.create

    Returns:
        a PairingCode
    """
    method = 'POST'
    url = '/api/v1/users/{user_id}/observer_pairing_codes'.format(user_id=user_id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return PairingCode(data)
