from typing import Literal, Optional, Union

from cool import utils
from cool.api import objects, paginations


class Module(objects.Base):
    """
    https://canvas.instructure.com/doc/api/modules.html#Module
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('id', 'name')

    @property
    def id(self):
        """the unique identifier for the module"""
        return self.getattr('id')

    @property
    def workflow_state(self):
        """the state of the module: 'active', 'deleted'"""
        return self.getattr('workflow_state')

    @property
    def position(self):
        """the position of this module in the course (1-based)"""
        return self.getattr('position')

    @property
    def name(self):
        """the name of this module"""
        return self.getattr('name')

    @property
    def unlock_at(self):
        """(Optional) the date this module will unlock"""
        return self.getattr('unlock_at')

    @property
    def require_sequential_progress(self):
        """Whether module items must be unlocked in order"""
        return self.getattr('require_sequential_progress')

    @property
    def prerequisite_module_ids(self):
        """IDs of Modules that must be completed before this one is unlocked"""
        return self.getattr('prerequisite_module_ids')

    @property
    def items_count(self):
        """The number of items in the module"""
        return self.getattr('items_count')

    @property
    def items_url(self):
        """The API URL to retrive this module's items"""
        return self.getattr('items_url')

    @property
    def items(self) -> list['ModuleItem']:
        """
        The contents of this module, as an array of Module Items. (Present only if
        requested via include[]=items AND the module is not deemed too large by
        Canvas.)
        """
        constructor_kwargs = {'session': self.session, 'base_url': self.base_url}
        return self.getattr(
            'items',
            constructor=ModuleItem,
            constructor_kwargs=constructor_kwargs,
            type='list',
        )

    @property
    def state(self):
        """
        The state of this Module for the calling user one of 'locked', 'unlocked',
        'started', 'completed' (Optional; present only if the caller is a student or
        if the optional parameter 'student_id' is included)
        """
        return self.getattr('state')

    @property
    def completed_at(self):
        """
        the date the calling user completed the module (Optional; present only if the
        caller is a student or if the optional parameter 'student_id' is included)
        """
        return self.getattr('completed_at')

    @property
    def publish_final_grade(self):
        """
        if the student's final grade for the course should be published to the SIS
        upon completion of this module
        """
        return self.getattr('publish_final_grade')

    @property
    def published(self):
        """
        (Optional) Whether this module is published. This field is present only if
        the caller has permission to view unpublished modules.
        """
        return self.getattr('published')


class CompletionRequirement(objects.Simple):
    """
    https://canvas.instructure.com/doc/api/modules.html#CompletionRequirement
    """

    def __init__(self, attributes: dict) -> None:
        super().__init__(attributes=attributes)

    repr_names = ('type',)

    @property
    def type(self):
        """
        one of 'must_view', 'must_submit', 'must_contribute', 'min_score',
        'must_mark_done'
        """
        return self.getattr('type')

    @property
    def min_score(self):
        """minimum score required to complete (only present when type == 'min_score')"""
        return self.getattr('min_score')

    @property
    def completed(self):
        """
        whether the calling user has met this requirement (Optional; present only if
        the caller is a student or if the optional parameter 'student_id' is
        included)
        """
        return self.getattr('completed')


class ContentDetails(objects.Simple):
    """
    https://canvas.instructure.com/doc/api/modules.html#ContentDetails
    """

    def __init__(self, attributes: dict) -> None:
        super().__init__(attributes=attributes)

    @property
    def points_possible(self):
        return self.getattr('points_possible')

    @property
    def due_at(self):
        return self.getattr('due_at')

    @property
    def unlock_at(self):
        return self.getattr('unlock_at')

    @property
    def lock_at(self):
        return self.getattr('lock_at')

    @property
    def locked_for_user(self):
        return self.getattr('locked_for_user')

    @property
    def lock_explanation(self):
        return self.getattr('lock_explanation')

    @property
    def lock_info(self):
        return self.getattr('lock_info')

    @property
    def hidden(self):
        return self.getattr('hidden')

    @property
    def display_name(self):
        return self.getattr('display_name')

    @property
    def thumbnail_url(self):
        return self.getattr('thumbnail_url')

    @property
    def locked(self):
        return self.getattr('locked')


class ModuleItem(objects.Base):
    """
    https://canvas.instructure.com/doc/api/modules.html#ModuleItem
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('id', 'title')

    @property
    def id(self):
        """the unique identifier for the module item"""
        return self.getattr('id')

    @property
    def module_id(self):
        """the id of the Module this item appears in"""
        return self.getattr('module_id')

    @property
    def position(self):
        """the position of this item in the module (1-based)"""
        return self.getattr('position')

    @property
    def title(self):
        """the title of this item"""
        return self.getattr('title')

    @property
    def indent(self):
        """0-based indent level; module items may be indented to show a hierarchy"""
        return self.getattr('indent')

    @property
    def type(self):
        """
        the type of object referred to one of 'File', 'Page', 'Discussion',
        'Assignment', 'Quiz', 'SubHeader', 'ExternalUrl', 'ExternalTool'
        """
        return self.getattr('type')

    @property
    def content_id(self):
        """
        the id of the object referred to applies to 'File', 'Discussion',
        'Assignment', 'Quiz', 'ExternalTool' types
        """
        return self.getattr('content_id')

    @property
    def html_url(self):
        """link to the item in Canvas"""
        return self.getattr('html_url')

    @property
    def url(self):
        """(Optional) link to the Canvas API object, if applicable"""
        return self.getattr('url')

    @property
    def page_url(self):
        """(only for 'Page' type) unique locator for the linked wiki page"""
        return self.getattr('page_url')

    @property
    def external_url(self):
        """
        (only for 'ExternalUrl' and 'ExternalTool' types) external url that the item
        points to
        """
        return self.getattr('external_url')

    @property
    def new_tab(self):
        """(only for 'ExternalTool' type) whether the external tool opens in a new tab"""
        return self.getattr('new_tab')

    @property
    def completion_requirement(self) -> CompletionRequirement:
        """Completion requirement for this module item"""
        return self.getattr('completion_requirement', constructor=CompletionRequirement)

    @property
    def content_details(self) -> ContentDetails:
        """
        (Present only if requested through include[]=content_details) If applicable,
        returns additional details specific to the associated object
        """
        return self.getattr('content_details', constructor=ContentDetails)

    @property
    def published(self):
        """
        (Optional) Whether this module item is published. This field is present only
        if the caller has permission to view unpublished items.
        """
        return self.getattr('published')


class ModuleItemSequenceNode(objects.Base):
    """
    https://canvas.instructure.com/doc/api/modules.html#ModuleItemSequenceNode
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    @property
    def prev(self):
        """The previous ModuleItem in the sequence"""
        constructor_kwargs = {'session': self.session, 'base_url': self.base_url}
        return self.getattr('prev', constructor=ModuleItem, constructor_kwargs=constructor_kwargs)

    @property
    def current(self) -> ModuleItem:
        """The ModuleItem being queried"""
        constructor_kwargs = {'session': self.session, 'base_url': self.base_url}
        return self.getattr('current',
                            constructor=ModuleItem,
                            constructor_kwargs=constructor_kwargs)

    @property
    def next(self):
        """The next ModuleItem in the sequence"""
        constructor_kwargs = {'session': self.session, 'base_url': self.base_url}
        return self.getattr('next', constructor=ModuleItem, constructor_kwargs=constructor_kwargs)

    @property
    def mastery_path(self):
        """The conditional release rule for the module item, if applicable"""
        return self.getattr('mastery_path')


class ModuleItemSequence(objects.Base):
    """
    https://canvas.instructure.com/doc/api/modules.html#ModuleItemSequence
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    @property
    def items(self) -> list[ModuleItemSequenceNode]:
        """
        an array containing one ModuleItemSequenceNode for each appearence of the
        asset in the module sequence (up to 10 total)
        """
        return self.getattr('items', constructor=ModuleItemSequenceNode, type='list')

    @property
    def modules(self) -> list[Module]:
        """an array containing each Module referenced above"""
        constructor_kwargs = {'session': self.session, 'base_url': self.base_url}
        return self.getattr('modules',
                            constructor=Module,
                            constructor_kwargs=constructor_kwargs,
                            type='list')


def list_modules(
    session,
    base_url,
    course_id,
    include=None,
    search_term: Optional[str] = None,
    student_id: Optional[str] = None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List modules

    `GET /api/v1/courses/:course_id/modules`

    A paginated list of the modules in a course

    https://canvas.instructure.com/doc/api/modules.html#method.context_modules_api.index

    Returns:
        a list of Modules
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/modules'.format(course_id=course_id)
    query = [
        ('include', include),
        ('search_term', search_term),
        ('student_id', student_id),
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
        constructor=Module,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def show_module(
    session,
    base_url,
    course_id,
    id,
    include=None,
    student_id: Optional[str] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Show module

    `GET /api/v1/courses/:course_id/modules/:id`

    Get information about a single module

    https://canvas.instructure.com/doc/api/modules.html#method.context_modules_api.show

    Returns:
        a Module
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/modules/{id}'.format(course_id=course_id, id=id)
    query = [
        ('include', include),
        ('student_id', student_id),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Module(data, session=session, base_url=base_url)


def create_a_module(
    session,
    base_url,
    course_id,
    module=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Create a module

    `POST /api/v1/courses/:course_id/modules`

    Create and return a new module

    https://canvas.instructure.com/doc/api/modules.html#method.context_modules_api.create

    Returns:
        a Module
    """
    method = 'POST'
    url = '/api/v1/courses/{course_id}/modules'.format(course_id=course_id)
    query = [
        ('module', module),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Module(data, session=session, base_url=base_url)


def update_a_module(
    session,
    base_url,
    course_id,
    id,
    module=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Update a module

    `PUT /api/v1/courses/:course_id/modules/:id`

    Update and return an existing module

    https://canvas.instructure.com/doc/api/modules.html#method.context_modules_api.update

    Returns:
        a Module
    """
    method = 'PUT'
    url = '/api/v1/courses/{course_id}/modules/{id}'.format(course_id=course_id, id=id)
    query = [
        ('module', module),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Module(data, session=session, base_url=base_url)


def delete_module(
    session,
    base_url,
    course_id,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Delete module

    `DELETE /api/v1/courses/:course_id/modules/:id`

    Delete a module

    https://canvas.instructure.com/doc/api/modules.html#method.context_modules_api.destroy

    Returns:
        a Module
    """
    method = 'DELETE'
    url = '/api/v1/courses/{course_id}/modules/{id}'.format(course_id=course_id, id=id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Module(data, session=session, base_url=base_url)


def re_lock_module_progressions(
    session,
    base_url,
    course_id,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Re-lock module progressions

    `PUT /api/v1/courses/:course_id/modules/:id/relock`

    Resets module progressions to their default locked state and recalculates them based on the current requirements.

    Adding progression requirements to an active course will not lock students out of modules they have already unlocked unless this action is called.

    https://canvas.instructure.com/doc/api/modules.html#method.context_modules_api.relock

    Returns:
        a Module
    """
    method = 'PUT'
    url = '/api/v1/courses/{course_id}/modules/{id}/relock'.format(course_id=course_id, id=id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Module(data, session=session, base_url=base_url)


def list_module_items(
    session,
    base_url,
    course_id,
    module_id,
    include=None,
    search_term: Optional[str] = None,
    student_id: Optional[str] = None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List module items

    `GET /api/v1/courses/:course_id/modules/:module_id/items`

    A paginated list of the items in a module

    https://canvas.instructure.com/doc/api/modules.html#method.context_module_items_api.index

    Returns:
        a list of ModuleItems
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/modules/{module_id}/items'.format(course_id=course_id,
                                                                         module_id=module_id)
    query = [
        ('include', include),
        ('search_term', search_term),
        ('student_id', student_id),
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
        constructor=ModuleItem,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def show_module_item(
    session,
    base_url,
    course_id,
    module_id,
    id,
    include=None,
    student_id: Optional[str] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Show module item

    `GET /api/v1/courses/:course_id/modules/:module_id/items/:id`

    Get information about a single module item

    https://canvas.instructure.com/doc/api/modules.html#method.context_module_items_api.show

    Returns:
        a ModuleItem
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/modules/{module_id}/items/{id}'.format(course_id=course_id,
                                                                              module_id=module_id,
                                                                              id=id)
    query = [
        ('include', include),
        ('student_id', student_id),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return ModuleItem(data, session=session, base_url=base_url)


def create_a_module_item(
    session,
    base_url,
    course_id,
    module_id,
    module_item=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Create a module item

    `POST /api/v1/courses/:course_id/modules/:module_id/items`

    Create and return a new module item

    https://canvas.instructure.com/doc/api/modules.html#method.context_module_items_api.create

    Returns:
        a ModuleItem
    """
    method = 'POST'
    url = '/api/v1/courses/{course_id}/modules/{module_id}/items'.format(course_id=course_id,
                                                                         module_id=module_id)
    query = [
        ('module_item', module_item),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return ModuleItem(data, session=session, base_url=base_url)


def update_a_module_item(
    session,
    base_url,
    course_id,
    module_id,
    id,
    module_item=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Update a module item

    `PUT /api/v1/courses/:course_id/modules/:module_id/items/:id`

    Update and return an existing module item

    https://canvas.instructure.com/doc/api/modules.html#method.context_module_items_api.update

    Returns:
        a ModuleItem
    """
    method = 'PUT'
    url = '/api/v1/courses/{course_id}/modules/{module_id}/items/{id}'.format(course_id=course_id,
                                                                              module_id=module_id,
                                                                              id=id)
    query = [
        ('module_item', module_item),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return ModuleItem(data, session=session, base_url=base_url)


def select_a_mastery_path(
    session,
    base_url,
    course_id,
    module_id,
    id,
    assignment_set_id: Optional[str] = None,
    student_id: Optional[str] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Select a mastery path

    `POST /api/v1/courses/:course_id/modules/:module_id/items/:id/select_mastery_path`

    Select a mastery path when module item includes several possible paths. Requires Mastery Paths feature to be enabled. Returns a compound document with the assignments included in the given path and any module items related to those assignments

    https://canvas.instructure.com/doc/api/modules.html#method.context_module_items_api.select_mastery_path
    """
    method = 'POST'
    url = '/api/v1/courses/{course_id}/modules/{module_id}/items/{id}/select_mastery_path'.format(
        course_id=course_id, module_id=module_id, id=id)
    query = [
        ('assignment_set_id', assignment_set_id),
        ('student_id', student_id),
    ]
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def delete_module_item(
    session,
    base_url,
    course_id,
    module_id,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Delete module item

    `DELETE /api/v1/courses/:course_id/modules/:module_id/items/:id`

    Delete a module item

    https://canvas.instructure.com/doc/api/modules.html#method.context_module_items_api.destroy

    Returns:
        a ModuleItem
    """
    method = 'DELETE'
    url = '/api/v1/courses/{course_id}/modules/{module_id}/items/{id}'.format(course_id=course_id,
                                                                              module_id=module_id,
                                                                              id=id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return ModuleItem(data, session=session, base_url=base_url)


def mark_module_item_as_done(
    session,
    base_url,
    course_id,
    module_id,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Mark module item as done

    `PUT /api/v1/courses/:course_id/modules/:module_id/items/:id/done`

    Mark a module item as done. Use HTTP method PUT to mark as done.

    https://canvas.instructure.com/doc/api/modules.html#method.context_module_items_api.mark_as_done
    """
    method = 'PUT'
    url = '/api/v1/courses/{course_id}/modules/{module_id}/items/{id}/done'.format(
        course_id=course_id, module_id=module_id, id=id)
    query = []
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def mark_module_item_as_not_done(
    session,
    base_url,
    course_id,
    module_id,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Mark module item as not done

    `DELETE /api/v1/courses/:course_id/modules/:module_id/items/:id/done`

    Mark a module item as not done. Use HTTP method DELETE to mark as not done.

    https://canvas.instructure.com/doc/api/modules.html#method.context_module_items_api.mark_as_done
    """
    method = 'DELETE'
    url = '/api/v1/courses/{course_id}/modules/{module_id}/items/{id}/done'.format(
        course_id=course_id, module_id=module_id, id=id)
    query = []
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def get_module_item_sequence(
    session,
    base_url,
    course_id,
    asset_type: Optional[str] = None,
    asset_id: Optional[int] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get module item sequence

    `GET /api/v1/courses/:course_id/module_item_sequence`

    Given an asset in a course, find the ModuleItem it belongs to, the previous and next Module Items in the course sequence, and also any applicable mastery path rules

    https://canvas.instructure.com/doc/api/modules.html#method.context_module_items_api.item_sequence

    Returns:
        a ModuleItemSequence
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/module_item_sequence'.format(course_id=course_id)
    query = [
        ('asset_type', asset_type),
        ('asset_id', asset_id),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return ModuleItemSequence(data, session=session, base_url=base_url)


def mark_module_item_read(
    session,
    base_url,
    course_id,
    module_id,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Mark module item read

    `POST /api/v1/courses/:course_id/modules/:module_id/items/:id/mark_read`

    Fulfills "must view" requirement for a module item. It is generally not necessary to do this explicitly, but it is provided for applications that need to access external content directly (bypassing the html_url redirect that normally allows Canvas to fulfill "must view" requirements).

    This endpoint cannot be used to complete requirements on locked or unpublished module items.
    """
    method = 'POST'
    url = '/api/v1/courses/{course_id}/modules/{module_id}/items/{id}/mark_read'.format(
        course_id=course_id, module_id=module_id, id=id)
    query = []
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
