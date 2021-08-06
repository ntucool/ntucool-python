from typing import Literal, Optional, Union

from cool import utils
from cool.api import objects, paginations


class FeatureFlag(objects.Base):
    """
    https://canvas.instructure.com/doc/api/feature_flags.html#FeatureFlag
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('context_type', 'context_id', 'feature')

    @property
    def context_type(self):
        """
        The type of object to which this flag applies (Account, Course, or User).
        (This field is not present if this FeatureFlag represents the global Canvas
        default)
        """
        return self.getattr('context_type')

    @property
    def context_id(self):
        """
        The id of the object to which this flag applies (This field is not present if
        this FeatureFlag represents the global Canvas default)
        """
        return self.getattr('context_id')

    @property
    def feature(self):
        """The feature this flag controls"""
        return self.getattr('feature')

    @property
    def state(self):
        """
        The policy for the feature at this context.  can be 'off', 'allowed',
        'allowed_on', or 'on'.
        """
        return self.getattr('state')

    @property
    def locked(self):
        """
        If set, this feature flag cannot be changed in the caller's context because
        the flag is set 'off' or 'on' in a higher context
        """
        return self.getattr('locked')

    @property
    def locking_account_id(self):
        """
        Deprecated
        [2016-01-15] FeatureFlags previously had a locking_account_id field; it was never used, and has been removed. It is still included in API responses for backwards compatibility reasons. Its value is always null.

        https://canvas.instructure.com/doc/api/feature_flags.html
        """
        return self.getattr('locking_account_id')

    @property
    def transitions(self):
        return self.getattr('transitions')

    @property
    def parent_state(self):
        return self.getattr('parent_state')


class Feature(objects.Base):
    """
    https://canvas.instructure.com/doc/api/feature_flags.html#Feature
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('feature', 'applies_to')

    @property
    def feature(self):
        """The symbolic name of the feature, used in FeatureFlags"""
        return self.getattr('feature')

    @property
    def display_name(self):
        """The user-visible name of the feature"""
        return self.getattr('display_name')

    @property
    def applies_to(self):
        """
        The type of object the feature applies to (RootAccount, Account, Course, or
        User):
        * RootAccount features may only be controlled by flags on root accounts.
        * Account features may be controlled by flags on accounts and their parent
        accounts.
        * Course features may be controlled by flags on courses and their parent
        accounts.
        * User features may be controlled by flags on users and site admin only.
        """
        return self.getattr('applies_to')

    @property
    def enable_at(self):
        """
        The date this feature will be globally enabled, or null if this is not
        planned. (This information is subject to change.)
        """
        return self.getattr('enable_at')

    @property
    def feature_flag(self) -> FeatureFlag:
        """The FeatureFlag that applies to the caller"""
        constructor_kwargs = {'session': self.session, 'base_url': self.base_url}
        return self.getattr('feature_flag',
                            constructor=FeatureFlag,
                            constructor_kwargs=constructor_kwargs)

    @property
    def root_opt_in(self):
        """
        If true, a feature that is 'allowed' globally will be 'off' by default in
        root accounts. Otherwise, root accounts inherit the global 'allowed' setting,
        which allows sub-accounts and courses to turn features on with no root
        account action.
        """
        return self.getattr('root_opt_in')

    @property
    def beta(self):
        """
        Whether the feature is a beta feature. If true, the feature may not be fully
        polished and may be subject to change in the future.
        """
        return self.getattr('beta')

    @property
    def autoexpand(self):
        """
        Whether the details of the feature are autoexpanded on page load vs. the user
        clicking to expand.
        """
        return self.getattr('autoexpand')

    @property
    def development(self):
        """
        Whether the feature is in active development. Features in this state are only
        visible in test and beta instances and are not yet available for production
        use.
        """
        return self.getattr('development')

    @property
    def release_notes_url(self):
        """A URL to the release notes describing the feature"""
        return self.getattr('release_notes_url')

    @property
    def description(self):
        return self.getattr('description')


def list_features(
    session,
    base_url,
    context: Literal['courses', 'accounts', 'users'],
    context_id,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List features

    `GET /api/v1/courses/:course_id/features`

    `GET /api/v1/accounts/:account_id/features`

    `GET /api/v1/users/:user_id/features`

    A paginated list of all features that apply to a given Account, Course, or User.

    https://canvas.instructure.com/doc/api/feature_flags.html#method.feature_flags.index

    Returns:
        a list of Features
    """
    if context not in ('courses', 'accounts', 'users'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/features'.format(context=context, context_id=context_id)
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
        constructor=Feature,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def list_enabled_features(
    session,
    base_url,
    context: Literal['courses', 'accounts', 'users'],
    context_id,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
) -> Union[paginations.Pagination[str], list[str]]:
    """
    List enabled features

    `GET /api/v1/courses/:course_id/features/enabled`

    `GET /api/v1/accounts/:account_id/features/enabled`

    `GET /api/v1/users/:user_id/features/enabled`

    A paginated list of all features that are enabled on a given Account, Course, or User. Only the feature names are returned.

    https://canvas.instructure.com/doc/api/feature_flags.html#method.feature_flags.enabled_features

    NTU COOL does not seem to support pagination.
    """
    if context not in ('courses', 'accounts', 'users'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/features/enabled'.format(context=context,
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
        raise_for_error=raise_for_error,
    )


def list_environment_features(
    session,
    base_url,
    params=None,
    raise_for_error: bool = True,
):
    """
    List environment features

    `GET /api/v1/features/environment`

    Return a hash of global feature settings that pertain to the Canvas user interface. This is the same information supplied to the web interface as ENV.FEATURES.

    https://canvas.instructure.com/doc/api/feature_flags.html#method.feature_flags.environment

    NTU COOL does not seem to support this resource.
    """
    raise NotImplementedError
    method = 'GET'
    url = '/api/v1/features/environment'
    query = []
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def get_feature_flag(
    session,
    base_url,
    context: Literal['courses', 'accounts', 'users'],
    context_id,
    feature,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get feature flag

    `GET /api/v1/courses/:course_id/features/flags/:feature`

    `GET /api/v1/accounts/:account_id/features/flags/:feature`

    `GET /api/v1/users/:user_id/features/flags/:feature`

    Get the feature flag that applies to a given Account, Course, or User. The flag may be defined on the object, or it may be inherited from a parent account. You can look at the context_id and context_type of the returned object to determine which is the case. If these fields are missing, then the object is the global Canvas default.

    https://canvas.instructure.com/doc/api/feature_flags.html#method.feature_flags.show

    Returns:
        a FeatureFlag
    """
    if context not in ('courses', 'accounts', 'users'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/features/flags/{feature}'.format(context=context,
                                                                           context_id=context_id,
                                                                           feature=feature)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return FeatureFlag(data, session=session, base_url=base_url)


def set_feature_flag(
    session,
    base_url,
    context: Literal['courses', 'accounts', 'users'],
    context_id,
    feature,
    state: Optional[str] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Set feature flag

    `PUT /api/v1/courses/:course_id/features/flags/:feature`

    `PUT /api/v1/accounts/:account_id/features/flags/:feature`

    `PUT /api/v1/users/:user_id/features/flags/:feature`

    Set a feature flag for a given Account, Course, or User. This call will fail if a parent account sets a feature flag for the same feature in any state other than "allowed".

    https://canvas.instructure.com/doc/api/feature_flags.html#method.feature_flags.update

    Returns:
        a FeatureFlag
    """
    if context not in ('courses', 'accounts', 'users'):
        raise ValueError
    method = 'PUT'
    url = '/api/v1/{context}/{context_id}/features/flags/{feature}'.format(context=context,
                                                                           context_id=context_id,
                                                                           feature=feature)
    query = [
        ('state', state),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return FeatureFlag(data, session=session, base_url=base_url)


def remove_feature_flag(
    session,
    base_url,
    context: Literal['courses', 'accounts', 'users'],
    context_id,
    feature,
    params=None,
    raise_for_error: bool = True,
):
    """
    Remove feature flag

    `DELETE /api/v1/courses/:course_id/features/flags/:feature`

    `DELETE /api/v1/accounts/:account_id/features/flags/:feature`

    `DELETE /api/v1/users/:user_id/features/flags/:feature`

    Remove feature flag for a given Account, Course, or User.  (Note that the flag must be defined on the Account, Course, or User directly.)  The object will then inherit the feature flags from a higher account, if any exist.  If this flag was 'on' or 'off', then lower-level account flags that were masked by this one will apply again.

    https://canvas.instructure.com/doc/api/feature_flags.html#method.feature_flags.delete

    Returns:
        a FeatureFlag
    """
    if context not in ('courses', 'accounts', 'users'):
        raise ValueError
    method = 'DELETE'
    url = '/api/v1/{context}/{context_id}/features/flags/{feature}'.format(context=context,
                                                                           context_id=context_id,
                                                                           feature=feature)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return FeatureFlag(data, session=session, base_url=base_url)
