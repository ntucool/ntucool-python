from typing import Literal, Optional, Union

from cool import utils
from cool.api import objects, paginations, common


class Section(objects.Base):
    """
    https://canvas.instructure.com/doc/api/sections.html#Section
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('id', 'name')

    @property
    def id(self):
        """The unique identifier for the section."""
        return self.getattr('id')

    @property
    def name(self):
        """The name of the section."""
        return self.getattr('name')

    @property
    def sis_section_id(self):
        """
        The sis id of the section. This field is only included if the user has
        permission to view SIS information.
        """
        return self.getattr('sis_section_id')

    @property
    def integration_id(self):
        """
        Optional: The integration ID of the section. This field is only included if
        the user has permission to view SIS information.
        """
        return self.getattr('integration_id')

    @property
    def sis_import_id(self):
        """
        The unique identifier for the SIS import if created through SIS. This field
        is only included if the user has permission to manage SIS information.
        """
        return self.getattr('sis_import_id')

    @property
    def course_id(self):
        """The unique Canvas identifier for the course in which the section belongs"""
        return self.getattr('course_id')

    @property
    def sis_course_id(self):
        """
        The unique SIS identifier for the course in which the section belongs. This
        field is only included if the user has permission to view SIS information.
        """
        return self.getattr('sis_course_id')

    @property
    def start_at(self):
        """the start date for the section, if applicable"""
        return self.getattr('start_at')

    @property
    def end_at(self):
        """the end date for the section, if applicable"""
        return self.getattr('end_at')

    @property
    def restrict_enrollments_to_section_dates(self):
        """Restrict user enrollments to the start and end dates of the section"""
        return self.getattr('restrict_enrollments_to_section_dates')

    @property
    def nonxlist_course_id(self):
        """The unique identifier of the original course of a cross-listed section"""
        return self.getattr('nonxlist_course_id')

    @property
    def total_students(self):
        """optional: the total number of active and invited students in the section"""
        return self.getattr('total_students')

    @property
    def created_at(self):
        return self.getattr('created_at')

    @property
    def students(self) -> list[common.User]:
        """
        "students": Associations to include with the group. Note: this is only available if you have permission to view users or grades in the course

        https://canvas.instructure.com/doc/api/sections.html#method.sections.index
        """
        constructor_kwargs = {'session': self.session, 'base_url': self.base_url}
        return self.getattr('students',
                            constructor=common.User,
                            constructor_kwargs=constructor_kwargs,
                            type='list')

    @property
    def passback_status(self):
        """
        "passback_status": Include the grade passback status.

        https://canvas.instructure.com/doc/api/sections.html#method.sections.index
        """
        return self.getattr('passback_status')


def list_course_sections(
    session,
    base_url,
    course_id,
    include=None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List course sections

    `GET /api/v1/courses/:course_id/sections`

    A paginated list of the list of sections for this course.

    https://canvas.instructure.com/doc/api/sections.html#method.sections.index

    Returns:
        a list of Sections
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/sections'.format(course_id=course_id)
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
        constructor=Section,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def create_course_section(
    session,
    base_url,
    course_id,
    course_section=None,
    enable_sis_reactivation: Optional[bool] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Create course section

    `POST /api/v1/courses/:course_id/sections`

    Creates a new section for this course.

    https://canvas.instructure.com/doc/api/sections.html#method.sections.create

    Returns:
        a Section
    """
    method = 'POST'
    url = '/api/v1/courses/{course_id}/sections'.format(course_id=course_id)
    query = [
        ('course_section', course_section),
        ('enable_sis_reactivation', enable_sis_reactivation),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Section(data, session=session, base_url=base_url)


def cross_list_a_section(
    session,
    base_url,
    id,
    new_course_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Cross-list a Section

    `POST /api/v1/sections/:id/crosslist/:new_course_id`

    Move the Section to another course.  The new course may be in a different account (department), but must belong to the same root account (institution).

    https://canvas.instructure.com/doc/api/sections.html#method.sections.crosslist

    Returns:
        a Section
    """
    method = 'POST'
    url = '/api/v1/sections/{id}/crosslist/{new_course_id}'.format(id=id,
                                                                   new_course_id=new_course_id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Section(data, session=session, base_url=base_url)


def de_cross_list_a_section(
    session,
    base_url,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    De-cross-list a Section

    `DELETE /api/v1/sections/:id/crosslist`

    Undo cross-listing of a Section, returning it to its original course.

    https://canvas.instructure.com/doc/api/sections.html#method.sections.uncrosslist

    Returns:
        a Section
    """
    method = 'DELETE'
    url = '/api/v1/sections/{id}/crosslist'.format(id=id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Section(data, session=session, base_url=base_url)


def edit_a_section(
    session,
    base_url,
    id,
    course_section=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Edit a section

    `PUT /api/v1/sections/:id`

    Modify an existing section.

    https://canvas.instructure.com/doc/api/sections.html#method.sections.update

    Returns:
        a Section
    """
    method = 'PUT'
    url = '/api/v1/sections/{id}'.format(id=id)
    query = [
        ('course_section', course_section),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Section(data, session=session, base_url=base_url)


def get_section_information(
    session,
    base_url,
    course_id,
    id,
    include=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get section information

    `GET /api/v1/courses/:course_id/sections/:id`

    `GET /api/v1/sections/:id`

    Gets details about a specific section

    https://canvas.instructure.com/doc/api/sections.html#method.sections.show

    Returns:
        a Section
    """
    method = 'GET'
    if course_id is None:
        url = '/api/v1/sections/{id}'.format(id=id)
    else:
        url = '/api/v1/courses/{course_id}/sections/{id}'.format(course_id=course_id, id=id)
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
    return Section(data, session=session, base_url=base_url)


def delete_a_section(
    session,
    base_url,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Delete a section

    `DELETE /api/v1/sections/:id`

    Delete an existing section.  Returns the former Section.

    https://canvas.instructure.com/doc/api/sections.html#method.sections.destroy

    Returns:
        a Section
    """
    method = 'DELETE'
    url = '/api/v1/sections/{id}'.format(id=id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Section(data, session=session, base_url=base_url)
