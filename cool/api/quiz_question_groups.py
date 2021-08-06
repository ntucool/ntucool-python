from typing import Literal, Optional, Union

from cool import utils
from cool.api import objects, paginations


class QuizGroup(objects.Base):
    """
    https://canvas.instructure.com/doc/api/quiz_question_groups.html#QuizGroup
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('id', 'quiz_id', 'name')

    @property
    def id(self):
        """The ID of the question group."""
        return self.getattr('id')

    @property
    def quiz_id(self):
        """The ID of the Quiz the question group belongs to."""
        return self.getattr('quiz_id')

    @property
    def name(self):
        """The name of the question group."""
        return self.getattr('name')

    @property
    def pick_count(self):
        """The number of questions to pick from the group to display to the student."""
        return self.getattr('pick_count')

    @property
    def question_points(self):
        """The amount of points allotted to each question in the group."""
        return self.getattr('question_points')

    @property
    def assessment_question_bank_id(self):
        """The ID of the Assessment question bank to pull questions from."""
        return self.getattr('assessment_question_bank_id')

    @property
    def position(self):
        """The order in which the question group will be retrieved and displayed."""
        return self.getattr('position')


def get_a_single_quiz_group(
    session,
    base_url,
    course_id,
    quiz_id,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get a single quiz group

    `GET /api/v1/courses/:course_id/quizzes/:quiz_id/groups/:id`

    Returns details of the quiz group with the given id.

    https://canvas.instructure.com/doc/api/quiz_question_groups.html#method.quizzes/quiz_groups.show

    Returns:
        a QuizGroup
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}'.format(course_id=course_id,
                                                                             quiz_id=quiz_id,
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
    return QuizGroup(data, session=session, base_url=base_url)


def create_a_question_group(
    session,
    base_url,
    course_id,
    quiz_id,
    quiz_groups=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Create a question group

    `POST /api/v1/courses/:course_id/quizzes/:quiz_id/groups`

    Create a new question group for this quiz

    201 Created response code is returned if the creation was successful.

    https://canvas.instructure.com/doc/api/quiz_question_groups.html#method.quizzes/quiz_groups.create
    """
    method = 'POST'
    url = '/api/v1/courses/{course_id}/quizzes/{quiz_id}/groups'.format(course_id=course_id,
                                                                        quiz_id=quiz_id)
    query = [
        ('quiz_groups', quiz_groups),
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


def update_a_question_group(
    session,
    base_url,
    course_id,
    quiz_id,
    id,
    quiz_groups=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Update a question group

    `PUT /api/v1/courses/:course_id/quizzes/:quiz_id/groups/:id`

    Update a question group

    https://canvas.instructure.com/doc/api/quiz_question_groups.html#method.quizzes/quiz_groups.update
    """
    method = 'PUT'
    url = '/api/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}'.format(course_id=course_id,
                                                                             quiz_id=quiz_id,
                                                                             id=id)
    query = [
        ('quiz_groups', quiz_groups),
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


def delete_a_question_group(
    session,
    base_url,
    course_id,
    quiz_id,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Delete a question group

    `DELETE /api/v1/courses/:course_id/quizzes/:quiz_id/groups/:id`

    Delete a question group

    <b>204 No Content<b> response code is returned if the deletion was successful.

    https://canvas.instructure.com/doc/api/quiz_question_groups.html#method.quizzes/quiz_groups.destroy
    """
    raise NotImplementedError
    method = 'DELETE'
    url = '/api/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}'.format(course_id=course_id,
                                                                             quiz_id=quiz_id,
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
    return data


def reorder_question_groups(
    session,
    base_url,
    course_id,
    quiz_id,
    id,
    order=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Reorder question groups

    `POST /api/v1/courses/:course_id/quizzes/:quiz_id/groups/:id/reorder`

    Change the order of the quiz questions within the group

    <b>204 No Content<b> response code is returned if the reorder was successful.

    https://canvas.instructure.com/doc/api/quiz_question_groups.html#method.quizzes/quiz_groups.reorder
    """
    raise NotImplementedError
    method = 'POST'
    url = '/api/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}/reorder'.format(
        course_id=course_id, quiz_id=quiz_id, id=id)
    query = [
        ('order', order),
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
