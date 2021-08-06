from typing import Literal, Optional, Union

from cool import utils
from cool.api import objects, paginations


class AuthenticationProvider(objects.Base):
    """
    https://canvas.instructure.com/doc/api/authentication_providers.html#AuthenticationProvider
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    @property
    def identifier_format(self):
        """Valid for SAML providers."""
        return self.getattr('identifier_format')

    @property
    def auth_type(self):
        """Valid for all providers."""
        return self.getattr('auth_type')

    @property
    def id(self):
        """Valid for all providers."""
        return self.getattr('id')

    @property
    def log_out_url(self):
        """Valid for SAML providers."""
        return self.getattr('log_out_url')

    @property
    def log_in_url(self):
        """Valid for SAML and CAS providers."""
        return self.getattr('log_in_url')

    @property
    def certificate_fingerprint(self):
        """Valid for SAML providers."""
        return self.getattr('certificate_fingerprint')

    @property
    def requested_authn_context(self):
        """Valid for SAML providers."""
        return self.getattr('requested_authn_context')

    @property
    def auth_host(self):
        """Valid for LDAP providers."""
        return self.getattr('auth_host')

    @property
    def auth_filter(self):
        """Valid for LDAP providers."""
        return self.getattr('auth_filter')

    @property
    def auth_over_tls(self):
        """Valid for LDAP providers."""
        return self.getattr('auth_over_tls')

    @property
    def auth_base(self):
        """Valid for LDAP and CAS providers."""
        return self.getattr('auth_base')

    @property
    def auth_username(self):
        """Valid for LDAP providers."""
        return self.getattr('auth_username')

    @property
    def auth_port(self):
        """Valid for LDAP providers."""
        return self.getattr('auth_port')

    @property
    def position(self):
        """Valid for all providers."""
        return self.getattr('position')

    @property
    def idp_entity_id(self):
        """Valid for SAML providers."""
        return self.getattr('idp_entity_id')

    @property
    def login_attribute(self):
        """Valid for SAML providers."""
        return self.getattr('login_attribute')

    @property
    def sig_alg(self):
        """Valid for SAML providers."""
        return self.getattr('sig_alg')

    @property
    def jit_provisioning(self):
        """
        Just In Time provisioning. Valid for all providers except Canvas (which has
        the similar in concept self_registration setting).
        """
        return self.getattr('jit_provisioning')

    @property
    def federated_attributes(self):
        return self.getattr('federated_attributes')

    @property
    def mfa_required(self):
        """
        If multi-factor authentication is required when logging in with this
        authentication provider. The account must not have MFA disabled.
        """
        return self.getattr('mfa_required')


class SSOSettings(objects.Base):
    """
    Settings that are applicable across an account's authentication
    configuration, even if there are multiple individual providers

    https://canvas.instructure.com/doc/api/authentication_providers.html#SSOSettings
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    @property
    def login_handle_name(self):
        """The label used for unique login identifiers."""
        return self.getattr('login_handle_name')

    @property
    def change_password_url(self):
        """
        The url to redirect users to for password resets. Leave blank for default
        Canvas behavior
        """
        return self.getattr('change_password_url')

    @property
    def auth_discovery_url(self):
        """
        If a discovery url is set, canvas will forward all users to that URL when
        they need to be authenticated. That page will need to then help the user
        figure out where they need to go to log in. If no discovery url is
        configured, the first configuration will be used to attempt to authenticate
        the user.
        """
        return self.getattr('auth_discovery_url')

    @property
    def unknown_user_url(self):
        """
        If an unknown user url is set, Canvas will forward to that url when a service
        authenticates a user, but that user does not exist in Canvas. The default
        behavior is to present an error.
        """
        return self.getattr('unknown_user_url')


class FederatedAttributesConfig(objects.Simple):
    """
    A mapping of Canvas attribute names to attribute names that a provider may
    send, in order to update the value of these attributes when a user logs in.
    The values can be a FederatedAttributeConfig, or a raw string corresponding
    to the "attribute" property of a FederatedAttributeConfig. In responses, full
    FederatedAttributeConfig objects are returned if JIT provisioning is enabled,
    otherwise just the attribute names are returned.

    https://canvas.instructure.com/doc/api/authentication_providers.html#FederatedAttributesConfig
    """

    def __init__(self, attributes: dict) -> None:
        super().__init__(attributes=attributes)

    @property
    def admin_roles(self):
        """
        A comma separated list of role names to grant to the user. Note that these
        only apply at the root account level, and not sub-accounts. If the attribute
        is not marked for provisioning only, the user will also be removed from any
        other roles they currently hold that are not still specified by the IdP.
        """
        return self.getattr('admin_roles')

    @property
    def display_name(self):
        """The full display name of the user"""
        return self.getattr('display_name')

    @property
    def email(self):
        """The user's e-mail address"""
        return self.getattr('email')

    @property
    def given_name(self):
        """The first, or given, name of the user"""
        return self.getattr('given_name')

    @property
    def integration_id(self):
        """The secondary unique identifier for SIS purposes"""
        return self.getattr('integration_id')

    @property
    def locale(self):
        """The user's preferred locale/language"""
        return self.getattr('locale')

    @property
    def name(self):
        """The full name of the user"""
        return self.getattr('name')

    @property
    def sis_user_id(self):
        """The unique SIS identifier"""
        return self.getattr('sis_user_id')

    @property
    def sortable_name(self):
        """The full name of the user for sorting purposes"""
        return self.getattr('sortable_name')

    @property
    def surname(self):
        """The surname, or last name, of the user"""
        return self.getattr('surname')

    @property
    def timezone(self):
        """The user's preferred time zone"""
        return self.getattr('timezone')


def list_authentication_providers(
    session,
    base_url,
    account_id,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List authentication providers

    `GET /api/v1/accounts/:account_id/authentication_providers`

    Returns a paginated list of authentication providers

    https://canvas.instructure.com/doc/api/authentication_providers.html#method.authentication_providers.index

    Returns:
        a list of AuthenticationProviders
    """
    method = 'GET'
    url = '/api/v1/accounts/{account_id}/authentication_providers'.format(account_id=account_id)
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
        constructor=AuthenticationProvider,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def add_authentication_provider():
    """
    Add authentication provider

    `POST /api/v1/accounts/:account_id/authentication_providers`

    Add external authentication provider(s) for the account. Services may be Apple, CAS, Facebook, GitHub, Google, LDAP, LinkedIn, Microsoft, OpenID Connect, SAML, or Twitter.

    Each authentication provider is specified as a set of parameters as described below. A provider specification must include an 'auth_type' parameter with a value of 'apple', 'canvas', 'cas', 'clever', 'facebook', 'github', 'google', 'ldap', 'linkedin', 'microsoft', 'openid_connect', 'saml', or 'twitter'. The other recognized parameters depend on this auth_type; unrecognized parameters are discarded. Provider specifications not specifying a valid auth_type are ignored.

    You can set the 'position' for any provider. The config in the 1st position is considered the default. You can set 'jit_provisioning' for any provider besides Canvas. You can set 'mfa_required' for any provider.

    https://canvas.instructure.com/doc/api/authentication_providers.html#method.authentication_providers.create

    Returns:
        a AuthenticationProvider
    """
    raise NotImplementedError


def update_authentication_provider():
    """
    Update authentication provider

    `PUT /api/v1/accounts/:account_id/authentication_providers/:id`

    Update an authentication provider using the same options as the create endpoint. You can not update an existing provider to a new authentication type.

    https://canvas.instructure.com/doc/api/authentication_providers.html#method.authentication_providers.update

    Returns:
        a AuthenticationProvider
    """
    raise NotImplementedError


def get_authentication_provider(
    session,
    base_url,
    account_id,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get authentication provider

    `GET /api/v1/accounts/:account_id/authentication_providers/:id`

    Get the specified authentication provider

    https://canvas.instructure.com/doc/api/authentication_providers.html#method.authentication_providers.show

    Returns:
        a AuthenticationProvider
    """
    method = 'GET'
    url = '/api/v1/accounts/{account_id}/authentication_providers/{id}'.format(
        account_id=account_id, id=id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return AuthenticationProvider(data, session=session, base_url=base_url)


def delete_authentication_provider():
    """
    Delete authentication provider

    `DELETE /api/v1/accounts/:account_id/authentication_providers/:id`

    Delete the config

    https://canvas.instructure.com/doc/api/authentication_providers.html#method.authentication_providers.destroy
    """
    raise NotImplementedError


def show_account_auth_settings():
    """
    show account auth settings

    `GET /api/v1/accounts/:account_id/sso_settings`

    The way to get the current state of each account level setting that's relevant to Single Sign On configuration

    You can list the current state of each setting with "update_sso_settings"

    https://canvas.instructure.com/doc/api/authentication_providers.html#method.authentication_providers.show_sso_settings

    Returns:
        a SSOSettings
    """
    raise NotImplementedError


def update_account_auth_settings():
    """
    update account auth settings

    `PUT /api/v1/accounts/:account_id/sso_settings`

    For various cases of mixed SSO configurations, you may need to set some configuration at the account level to handle the particulars of your setup.

    This endpoint accepts a PUT request to set several possible account settings. All setting are optional on each request, any that are not provided at all are simply retained as is.  Any that provide the key but a null-ish value (blank string, null, undefined) will be UN-set.

    You can list the current state of each setting with "show_sso_settings"

    https://canvas.instructure.com/doc/api/authentication_providers.html#method.authentication_providers.update_sso_settings

    Returns:
        a SSOSettings
    """
    raise NotImplementedError
