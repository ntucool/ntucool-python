from typing import Literal, Optional, Union

from cool import utils
from cool.api import objects, paginations


class ExternalTool(objects.Base):
    """
    https://canvas.instructure.com/doc/api/external_tools.html#method.external_tools.show
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('id', 'domain', 'consumer_key', 'name')

    @property
    def id(self):
        """The unique identifier for the tool"""
        return self.getattr('id')

    @property
    def domain(self):
        """The domain to match links against"""
        return self.getattr('domain')

    @property
    def url(self):
        """The url to match links against"""
        return self.getattr('url')

    @property
    def consumer_key(self):
        """The consumer key used by the tool (The associated shared secret is not returned)"""
        return self.getattr('consumer_key')

    @property
    def name(self):
        """The name of the tool"""
        return self.getattr('name')

    @property
    def description(self):
        """A description of the tool"""
        return self.getattr('description')

    @property
    def created_at(self):
        """Timestamp of creation"""
        return self.getattr('created_at')

    @property
    def updated_at(self):
        """Timestamp of last update"""
        return self.getattr('updated_at')

    @property
    def privacy_level(self):
        """
        What information to send to the external tool, "anonymous", "name_only", "public"
        """
        return self.getattr('privacy_level')

    @property
    def custom_fields(self):
        """Custom fields that will be sent to the tool consumer"""
        return self.getattr('custom_fields')

    @property
    def is_rce_favorite(self):
        """Boolean determining whether this tool should be in a preferred location in the RCE."""
        return self.getattr('is_rce_favorite')

    @property
    def account_navigation(self):
        """The configuration for account navigation links (see create API for values)"""
        return self.getattr('account_navigation')

    @property
    def assignment_selection(self):
        """The configuration for assignment selection links (see create API for values)"""
        return self.getattr('assignment_selection')

    @property
    def course_home_sub_navigation(self):
        """The configuration for course home navigation links (see create API for values)"""
        return self.getattr('course_home_sub_navigation')

    @property
    def course_navigation(self):
        """The configuration for course navigation links (see create API for values)"""
        return self.getattr('course_navigation')

    @property
    def editor_button(self):
        """The configuration for a WYSIWYG editor button (see create API for values)"""
        return self.getattr('editor_button')

    @property
    def homework_submission(self):
        """The configuration for homework submission selection (see create API for values)"""
        return self.getattr('homework_submission')

    @property
    def link_selection(self):
        """The configuration for link selection (see create API for values)"""
        return self.getattr('link_selection')

    @property
    def migration_selection(self):
        """The configuration for migration selection (see create API for values)"""
        return self.getattr('migration_selection')

    @property
    def resource_selection(self):
        """The configuration for a resource selector in modules (see create API for values)"""
        return self.getattr('resource_selection')

    @property
    def tool_configuration(self):
        """The configuration for a tool configuration link (see create API for values)"""
        return self.getattr('tool_configuration')

    @property
    def user_navigation(self):
        """The configuration for user navigation links (see create API for values)"""
        return self.getattr('user_navigation')

    @property
    def selection_width(self):
        """The pixel width of the iFrame that the tool will be rendered in"""
        return self.getattr('selection_width')

    @property
    def selection_height(self):
        """The pixel height of the iFrame that the tool will be rendered in"""
        return self.getattr('selection_height')

    @property
    def icon_url(self):
        """The url for the tool icon"""
        return self.getattr('icon_url')

    @property
    def not_selectable(self):
        """whether the tool is not selectable from assignment and modules"""
        return self.getattr('not_selectable')

    @property
    def workflow_state(self):
        return self.getattr('workflow_state')

    @property
    def vendor_help_link(self):
        return self.getattr('vendor_help_link')

    @property
    def similarity_detection(self):
        return self.getattr('similarity_detection')

    @property
    def assignment_edit(self):
        return self.getattr('assignment_edit')

    @property
    def assignment_menu(self):
        return self.getattr('assignment_menu')

    @property
    def assignment_index_menu(self):
        return self.getattr('assignment_index_menu')

    @property
    def assignment_group_menu(self):
        return self.getattr('assignment_group_menu')

    @property
    def assignment_view(self):
        return self.getattr('assignment_view')

    @property
    def collaboration(self):
        return self.getattr('collaboration')

    @property
    def course_assignments_menu(self):
        return self.getattr('course_assignments_menu')

    @property
    def course_settings_sub_navigation(self):
        return self.getattr('course_settings_sub_navigation')

    @property
    def discussion_topic_menu(self):
        return self.getattr('discussion_topic_menu')

    @property
    def discussion_topic_index_menu(self):
        return self.getattr('discussion_topic_index_menu')

    @property
    def file_menu(self):
        return self.getattr('file_menu')

    @property
    def file_index_menu(self):
        return self.getattr('file_index_menu')

    @property
    def global_navigation(self):
        return self.getattr('global_navigation')

    @property
    def module_menu(self):
        return self.getattr('module_menu')

    @property
    def module_group_menu(self):
        return self.getattr('module_group_menu')

    @property
    def module_index_menu(self):
        return self.getattr('module_index_menu')

    @property
    def post_grades(self):
        return self.getattr('post_grades')

    @property
    def quiz_menu(self):
        return self.getattr('quiz_menu')

    @property
    def quiz_index_menu(self):
        return self.getattr('quiz_index_menu')

    @property
    def student_context_card(self):
        return self.getattr('student_context_card')

    @property
    def wiki_index_menu(self):
        return self.getattr('wiki_index_menu')

    @property
    def wiki_page_menu(self):
        return self.getattr('wiki_page_menu')

    @property
    def version(self):
        return self.getattr('version')


def list_external_tools(
    session,
    base_url,
    context: Literal['courses', 'accounts', 'groups'],
    context_id,
    search_term: Optional[str] = None,
    selectable: Optional[bool] = None,
    include_parents: Optional[bool] = None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List external tools

    `GET /api/v1/courses/:course_id/external_tools`

    `GET /api/v1/accounts/:account_id/external_tools`

    `GET /api/v1/groups/:group_id/external_tools`

    Returns the paginated list of external tools for the current context. See the get request docs for a single tool for a list of properties on an external tool.

    https://canvas.instructure.com/doc/api/external_tools.html#method.external_tools.index
    """
    if context not in ('courses', 'accounts', 'groups'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/external_tools'.format(context=context,
                                                                 context_id=context_id)
    query = [
        ('search_term', search_term),
        ('selectable', selectable),
        ('include_parents', include_parents),
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
        constructor=ExternalTool,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def get_a_sessionless_launch_url_for_an_external_tool(
    session,
    base_url,
    context: Literal['courses', 'accounts'],
    context_id,
    id: Optional[str] = None,
    url: Optional[str] = None,
    assignment_id: Optional[str] = None,
    module_item_id: Optional[str] = None,
    launch_type: Optional[Literal['assessment', 'module_item']] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get a sessionless launch url for an external tool.

    `GET /api/v1/courses/:course_id/external_tools/sessionless_launch`

    `GET /api/v1/accounts/:account_id/external_tools/sessionless_launch`

    Returns a sessionless launch url for an external tool.

    NOTE: Either the id or url must be provided unless launch_type is assessment or module_item.

    https://canvas.instructure.com/doc/api/external_tools.html#method.external_tools.generate_sessionless_launch
    """
    if context not in ('courses', 'accounts'):
        raise ValueError
    method = 'GET'
    _url = '/api/v1/{context}/{context_id}/external_tools/sessionless_launch'.format(
        context=context, context_id=context_id)
    query = [
        ('id', id),
        ('url', url),
        ('assignment_id', assignment_id),
        ('module_item_id', module_item_id),
        ('launch_type', launch_type),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        _url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return data


def get_a_single_external_tool(
    session,
    base_url,
    context: Literal['courses', 'accounts'],
    context_id,
    external_tool_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get a single external tool

    `GET /api/v1/courses/:course_id/external_tools/:external_tool_id`

    `GET /api/v1/accounts/:account_id/external_tools/:external_tool_id`

    Returns the specified external tool.

    https://canvas.instructure.com/doc/api/external_tools.html#method.external_tools.show
    """
    if context not in ('courses', 'accounts'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/external_tools/{external_tool_id}'.format(
        context=context, context_id=context_id, external_tool_id=external_tool_id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return ExternalTool(data, session=session, base_url=base_url)


def create_an_external_tool(
    session,
    base_url,
    context: Literal['courses', 'accounts'],
    context_id,
    client_id: Optional[str] = None,
    name: Optional[str] = None,
    privacy_level: Optional[Literal['anonymous', 'name_only', 'public']] = None,
    consumer_key: Optional[str] = None,
    shared_secret: Optional[str] = None,
    description: Optional[str] = None,
    url: Optional[str] = None,
    domain: Optional[str] = None,
    icon_url: Optional[str] = None,
    text: Optional[str] = None,
    custom_fields=None,
    is_rce_favorite: Optional[bool] = None,
    account_navigation=None,
    user_navigation=None,
    course_home_sub_navigation=None,
    course_navigation=None,
    editor_button=None,
    homework_submission=None,
    link_selection=None,
    migration_selection=None,
    tool_configuration=None,
    resource_selection=None,
    config_type: Optional[str] = None,
    config_xml: Optional[str] = None,
    config_url: Optional[str] = None,
    not_selectable: Optional[bool] = None,
    oauth_compliant: Optional[bool] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Create an external tool

    `POST /api/v1/courses/:course_id/external_tools`

    `POST /api/v1/accounts/:account_id/external_tools`

    Create an external tool in the specified course/account. The created tool will be returned, see the "show" endpoint for an example. If a client ID is supplied canvas will attempt to create a context external tool using the LTI 1.3 standard.

    https://canvas.instructure.com/doc/api/external_tools.html#method.external_tools.create
    """
    if context not in ('courses', 'accounts'):
        raise ValueError
    method = 'POST'
    _url = '/api/v1/{context}/{context_id}/external_tools'.format(context=context,
                                                                  context_id=context_id)
    query = [
        ('client_id', client_id),
        ('name', name),
        ('privacy_level', privacy_level),
        ('consumer_key', consumer_key),
        ('shared_secret', shared_secret),
        ('description', description),
        ('url', url),
        ('domain', domain),
        ('icon_url', icon_url),
        ('text', text),
        ('custom_fields', custom_fields),
        ('is_rce_favorite', is_rce_favorite),
        ('account_navigation', account_navigation),
        ('user_navigation', user_navigation),
        ('course_home_sub_navigation', course_home_sub_navigation),
        ('course_navigation', course_navigation),
        ('editor_button', editor_button),
        ('homework_submission', homework_submission),
        ('link_selection', link_selection),
        ('migration_selection', migration_selection),
        ('tool_configuration', tool_configuration),
        ('resource_selection', resource_selection),
        ('config_type', config_type),
        ('config_xml', config_xml),
        ('config_url', config_url),
        ('not_selectable', not_selectable),
        ('oauth_compliant', oauth_compliant),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        _url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return ExternalTool(data, session=session, base_url=base_url)


def edit_an_external_tool(
    session,
    base_url,
    context: Literal['courses', 'accounts'],
    context_id,
    external_tool_id,
    client_id: Optional[str] = None,
    name: Optional[str] = None,
    privacy_level: Optional[Literal['anonymous', 'name_only', 'public']] = None,
    consumer_key: Optional[str] = None,
    shared_secret: Optional[str] = None,
    description: Optional[str] = None,
    url: Optional[str] = None,
    domain: Optional[str] = None,
    icon_url: Optional[str] = None,
    text: Optional[str] = None,
    custom_fields=None,
    is_rce_favorite: Optional[bool] = None,
    account_navigation=None,
    user_navigation=None,
    course_home_sub_navigation=None,
    course_navigation=None,
    editor_button=None,
    homework_submission=None,
    link_selection=None,
    migration_selection=None,
    tool_configuration=None,
    resource_selection=None,
    config_type: Optional[str] = None,
    config_xml: Optional[str] = None,
    config_url: Optional[str] = None,
    not_selectable: Optional[bool] = None,
    oauth_compliant: Optional[bool] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Edit an external tool

    `PUT /api/v1/courses/:course_id/external_tools/:external_tool_id`

    `PUT /api/v1/accounts/:account_id/external_tools/:external_tool_id`

    Update the specified external tool. Uses same parameters as create

    https://canvas.instructure.com/doc/api/external_tools.html#method.external_tools.update
    """
    if context not in ('courses', 'accounts'):
        raise ValueError
    method = 'PUT'
    _url = '/api/v1/{context}/{context_id}/external_tools/{external_tool_id}'.format(
        context=context, context_id=context_id, external_tool_id=external_tool_id)
    query = [
        ('client_id', client_id),
        ('name', name),
        ('privacy_level', privacy_level),
        ('consumer_key', consumer_key),
        ('shared_secret', shared_secret),
        ('description', description),
        ('url', url),
        ('domain', domain),
        ('icon_url', icon_url),
        ('text', text),
        ('custom_fields', custom_fields),
        ('is_rce_favorite', is_rce_favorite),
        ('account_navigation', account_navigation),
        ('user_navigation', user_navigation),
        ('course_home_sub_navigation', course_home_sub_navigation),
        ('course_navigation', course_navigation),
        ('editor_button', editor_button),
        ('homework_submission', homework_submission),
        ('link_selection', link_selection),
        ('migration_selection', migration_selection),
        ('tool_configuration', tool_configuration),
        ('resource_selection', resource_selection),
        ('config_type', config_type),
        ('config_xml', config_xml),
        ('config_url', config_url),
        ('not_selectable', not_selectable),
        ('oauth_compliant', oauth_compliant),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        _url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return data


def delete_an_external_tool(
    session,
    base_url,
    context: Literal['courses', 'accounts'],
    context_id,
    external_tool_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Delete an external tool

    `DELETE /api/v1/courses/:course_id/external_tools/:external_tool_id`

    `DELETE /api/v1/accounts/:account_id/external_tools/:external_tool_id`

    Remove the specified external tool

    https://canvas.instructure.com/doc/api/external_tools.html#method.external_tools.destroy
    """
    if context not in ('courses', 'accounts'):
        raise ValueError
    method = 'DELETE'
    _url = '/api/v1/{context}/{context_id}/external_tools/{external_tool_id}'.format(
        context=context, context_id=context_id, external_tool_id=external_tool_id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        _url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return data


def add_tool_to_rce_favorites(
    session,
    base_url,
    account_id,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Add tool to RCE Favorites

    `POST /api/v1/accounts/:account_id/external_tools/rce_favorites/:id`

    Add the specified editor_button external tool to a preferred location in the RCE for courses in the given account and its subaccounts (if the subaccounts haven't set their own RCE Favorites). Cannot set more than 2 RCE Favorites.

    https://canvas.instructure.com/doc/api/external_tools.html#method.external_tools.add_rce_favorite
    """
    method = 'POST'
    _url = '/api/v1/accounts/{account_id}/external_tools/rce_favorites/{id}'.format(
        account_id=account_id, id=id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        _url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return data


def remove_tool_from_rce_favorites(
    session,
    base_url,
    account_id,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Remove tool from RCE Favorites

    `DELETE /api/v1/accounts/:account_id/external_tools/rce_favorites/:id`

    Remove the specified external tool from a preferred location in the RCE for the given account

    https://canvas.instructure.com/doc/api/external_tools.html#method.external_tools.remove_rce_favorite
    """
    method = 'DELETE'
    _url = '/api/v1/accounts/{account_id}/external_tools/rce_favorites/{id}'.format(
        account_id=account_id, id=id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        _url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return data


def get_visible_course_navigation_tools(
    session,
    base_url,
    context_codes=None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get visible course navigation tools

    `GET /api/v1/external_tools/visible_course_nav_tools`

    Get a list of external tools with the course_navigation placement that have not been hidden in course settings and whose visibility settings apply to the requesting user. These tools are the same that appear in the course navigation.

    The response format is the same as for List external tools, but with additional context_id and context_name fields on each element in the array.

    https://canvas.instructure.com/doc/api/external_tools.html#method.external_tools.all_visible_nav_tools
    """
    raise NotImplementedError
    method = 'GET'
    url = '/api/v1/external_tools/visible_course_nav_tools'
    query = [
        ('context_codes', context_codes),
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
        constructor=ExternalTool,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def get_visible_course_navigation_tools_for_a_single_course(
    session,
    base_url,
    course_id,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get visible course navigation tools for a single course

    `GET /api/v1/courses/:course_id/external_tools/visible_course_nav_tools`

    Get a list of external tools with the course_navigation placement that have not been hidden in course settings and whose visibility settings apply to the requesting user. These tools are the same that appear in the course navigation.

    The response format is the same as Get visible course navigation tools.

    https://canvas.instructure.com/doc/api/external_tools.html#method.external_tools.visible_course_nav_tools
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/external_tools/visible_course_nav_tools'.format(
        course_id=course_id)
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
        constructor=ExternalTool,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )
