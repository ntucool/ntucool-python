from typing import Literal, Optional, Union

from cool import utils
from cool.api import objects, paginations


class Rubric(objects.Base):
    """
    https://canvas.instructure.com/doc/api/rubrics.html#Rubric
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('id', 'context_type', 'context_id', 'title')

    @property
    def id(self):
        """the ID of the rubric"""
        return self.getattr('id')

    @property
    def title(self):
        """title of the rubric"""
        return self.getattr('title')

    @property
    def context_id(self):
        """the context owning the rubric"""
        return self.getattr('context_id')

    @property
    def context_type(self):
        return self.getattr('context_type')

    @property
    def points_possible(self):
        return self.getattr('points_possible')

    @property
    def reusable(self):
        return self.getattr('reusable')

    @property
    def read_only(self):
        return self.getattr('read_only')

    @property
    def free_form_criterion_comments(self):
        """whether or not free-form comments are used"""
        return self.getattr('free_form_criterion_comments')

    @property
    def hide_score_total(self):
        return self.getattr('hide_score_total')

    @property
    def data(self):
        """An array with all of this Rubric's grading Criteria"""
        return self.getattr('data')

    @property
    def assessments(self):
        """
        If an assessment type is included in the 'include' parameter, includes an
        array of rubric assessment objects for a given rubric, based on the
        assessment type requested. If the user does not request an assessment type
        this key will be absent.
        """
        return self.getattr('assessments')

    @property
    def associations(self):
        """
        If an association type is included in the 'include' parameter, includes an
        array of rubric association objects for a given rubric, based on the
        association type requested. If the user does not request an association type
        this key will be absent.
        """
        return self.getattr('associations')


def create_a_single_rubric():
    """
    Create a single rubric

    `POST /api/v1/courses/:course_id/rubrics`

    Returns the rubric with the given id.

    Unfortuantely this endpoint does not return a standard Rubric object, instead it returns a hash that looks like

    This may eventually be deprecated in favor of a more standardized return value, but that is not currently planned.

    https://canvas.instructure.com/doc/api/rubrics.html#method.rubrics.create
    """
    raise NotImplementedError


def update_a_single_rubric():
    """
    Update a single rubric

    `PUT /api/v1/courses/:course_id/rubrics/:id`

    Returns the rubric with the given id.

    Unfortuantely this endpoint does not return a standard Rubric object, instead it returns a hash that looks like

    This may eventually be deprecated in favor of a more standardized return value, but that is not currently planned.

    https://canvas.instructure.com/doc/api/rubrics.html#method.rubrics.update
    """
    raise NotImplementedError


def delete_a_single_rubric():
    """
    Delete a single rubric

    `DELETE /api/v1/courses/:course_id/rubrics/:id`

    Deletes a Rubric and removes all RubricAssociations.

    https://canvas.instructure.com/doc/api/rubrics.html#method.rubrics.destroy

    Returns:
        a Rubric
    """
    raise NotImplementedError


def list_rubrics(
    session,
    base_url,
    context: Literal['accounts', 'courses'],
    context_id,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List rubrics

    `GET /api/v1/accounts/:account_id/rubrics`

    `GET /api/v1/courses/:course_id/rubrics`

    Returns the paginated list of active rubrics for the current context.

    https://canvas.instructure.com/doc/api/rubrics.html#method.rubrics_api.index
    """
    if context not in ('accounts', 'courses'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/rubrics'.format(context=context, context_id=context_id)
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
        constructor=Rubric,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def get_a_single_rubric(
    session,
    base_url,
    context: Literal['accounts', 'courses'],
    context_id,
    id,
    include=None,
    style: Optional[Literal['full', 'comments_only']] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get a single rubric

    `GET /api/v1/accounts/:account_id/rubrics/:id`

    `GET /api/v1/courses/:course_id/rubrics/:id`

    Returns the rubric with the given id.

    https://canvas.instructure.com/doc/api/rubrics.html#method.rubrics_api.show

    Returns:
        a Rubric
    """
    if context not in ('accounts', 'courses'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/rubrics/{id}'.format(context=context,
                                                               context_id=context_id,
                                                               id=id)
    query = [
        ('include', include),
        ('style', style),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Rubric(data, session=session, base_url=base_url)


def create_a_single_rubric_assessment():
    """
    Create a single rubric assessment

    `POST /api/v1/courses/:course_id/rubric_associations/:rubric_association_id/rubric_assessments`

    Returns the rubric assessment with the given id. The returned object also provides the information of

    https://canvas.instructure.com/doc/api/rubrics.html#method.rubric_assessments.create
    """
    raise NotImplementedError


def update_a_single_rubric_assessment():
    """
    Update a single rubric assessment

    `PUT /api/v1/courses/:course_id/rubric_associations/:rubric_association_id/rubric_assessments/:id`

    Returns the rubric assessment with the given id. The returned object also provides the information of

    https://canvas.instructure.com/doc/api/rubrics.html#method.rubric_assessments.update
    """
    raise NotImplementedError


def delete_a_single_rubric_assessment():
    """
    Delete a single rubric assessment

    `DELETE /api/v1/courses/:course_id/rubric_associations/:rubric_association_id/rubric_assessments/:id`

    Deletes a rubric assessment

    https://canvas.instructure.com/doc/api/rubrics.html#method.rubric_assessments.destroy

    Returns:
        a RubricAssessment
    """
    raise NotImplementedError


def create_a_rubricassociation():
    """
    Create a RubricAssociation

    `POST /api/v1/courses/:course_id/rubric_associations`

    Returns the rubric with the given id.

    https://canvas.instructure.com/doc/api/rubrics.html#method.rubric_associations.create

    Returns:
        a RubricAssociation
    """
    raise NotImplementedError


def update_a_rubricassociation():
    """
    Update a RubricAssociation

    `PUT /api/v1/courses/:course_id/rubric_associations/:id`

    Returns the rubric with the given id.

    https://canvas.instructure.com/doc/api/rubrics.html#method.rubric_associations.update

    Returns:
        a RubricAssociation
    """
    raise NotImplementedError


def delete_a_rubricassociation():
    """
    Delete a RubricAssociation

    `DELETE /api/v1/courses/:course_id/rubric_associations/:id`

    Delete the RubricAssociation with the given ID

    https://canvas.instructure.com/doc/api/rubrics.html#method.rubric_associations.destroy

    Returns:
        a RubricAssociation
    """
    raise NotImplementedError
