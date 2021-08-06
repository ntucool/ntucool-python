from typing import Literal, Optional, Union

from cool import utils
from cool.api import objects, paginations


class QuizQuestion(objects.Base):
    """
    https://canvas.instructure.com/doc/api/quiz_questions.html#QuizQuestion
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('id', 'quiz_id', 'position', 'question_name')

    @property
    def id(self):
        """The ID of the quiz question."""
        return self.getattr('id')

    @property
    def quiz_id(self):
        """The ID of the Quiz the question belongs to."""
        return self.getattr('quiz_id')

    @property
    def position(self):
        """The order in which the question will be retrieved and displayed."""
        return self.getattr('position')

    @property
    def question_name(self):
        """The name of the question."""
        return self.getattr('question_name')

    @property
    def question_type(self):
        """The type of the question."""
        return self.getattr('question_type')

    @property
    def question_text(self):
        """The text of the question."""
        return self.getattr('question_text')

    @property
    def points_possible(self):
        """
        The maximum amount of points possible received for getting this question
        correct.
        """
        return self.getattr('points_possible')

    @property
    def correct_comments(self):
        """The comments to display if the student answers the question correctly."""
        return self.getattr('correct_comments')

    @property
    def incorrect_comments(self):
        """The comments to display if the student answers incorrectly."""
        return self.getattr('incorrect_comments')

    @property
    def neutral_comments(self):
        """The comments to display regardless of how the student answered."""
        return self.getattr('neutral_comments')

    @property
    def answers(self) -> list['Answer']:
        """An array of available answers to display to the student."""
        return self.getattr('answers', constructor=Answer, type='list')

    @property
    def quiz_group_id(self):
        return self.getattr('quiz_group_id')

    @property
    def assessment_question_id(self):
        return self.getattr('assessment_question_id')

    @property
    def variables(self):
        return self.getattr('variables')

    @property
    def formulas(self):
        return self.getattr('formulas')

    @property
    def answer_tolerance(self):
        return self.getattr('answer_tolerance')

    @property
    def formula_decimal_places(self):
        return self.getattr('formula_decimal_places')

    @property
    def matches(self):
        return self.getattr('matches')


class Answer(objects.Base):
    """
    https://canvas.instructure.com/doc/api/quiz_questions.html#Answer
    """

    def __init__(self, attributes: dict) -> None:
        super().__init__(attributes=attributes)

    repr_names = ('id',)

    @property
    def id(self):
        """
        The unique identifier for the answer.  Do not supply if this answer is part
        of a new question
        """
        return self.getattr('id')

    @property
    def answer_text(self):
        """The text of the answer."""
        return self.getattr('answer_text')

    @property
    def answer_weight(self):
        """
        An integer to determine correctness of the answer. Incorrect answers should
        be 0, correct answers should be 100.
        """
        return self.getattr('answer_weight')

    @property
    def answer_comments(self):
        """Specific contextual comments for a particular answer."""
        return self.getattr('answer_comments')

    @property
    def text_after_answers(self):
        """Used in missing word questions.  The text to follow the missing word"""
        return self.getattr('text_after_answers')

    @property
    def answer_match_left(self):
        """
        Used in matching questions.  The static value of the answer that will be
        displayed on the left for students to match for.
        """
        return self.getattr('answer_match_left')

    @property
    def answer_match_right(self):
        """
        Used in matching questions. The correct match for the value given in
        answer_match_left.  Will be displayed in a dropdown with the other
        answer_match_right values..
        """
        return self.getattr('answer_match_right')

    @property
    def matching_answer_incorrect_matches(self):
        """
        Used in matching questions. A list of distractors, delimited by new lines (
        ) that will be seeded with all the answer_match_right values.
        """
        return self.getattr('matching_answer_incorrect_matches')

    @property
    def numerical_answer_type(self):
        """
        Used in numerical questions.  Values can be 'exact_answer', 'range_answer',
        or 'precision_answer'.
        """
        return self.getattr('numerical_answer_type')

    @property
    def exact(self):
        """
        Used in numerical questions of type 'exact_answer'.  The value the answer
        should equal.
        """
        return self.getattr('exact')

    @property
    def margin(self):
        """
        Used in numerical questions of type 'exact_answer'. The margin of error
        allowed for the student's answer.
        """
        return self.getattr('margin')

    @property
    def approximate(self):
        """
        Used in numerical questions of type 'precision_answer'.  The value the answer
        should equal.
        """
        return self.getattr('approximate')

    @property
    def precision(self):
        """
        Used in numerical questions of type 'precision_answer'. The numerical
        precision that will be used when comparing the student's answer.
        """
        return self.getattr('precision')

    @property
    def start(self):
        """
        Used in numerical questions of type 'range_answer'. The start of the allowed
        range (inclusive).
        """
        return self.getattr('start')

    @property
    def end(self):
        """
        Used in numerical questions of type 'range_answer'. The end of the allowed
        range (inclusive).
        """
        return self.getattr('end')

    @property
    def blank_id(self):
        """Used in fill in multiple blank and multiple dropdowns questions."""
        return self.getattr('blank_id')

    @property
    def text(self):
        return self.getattr('text')

    @property
    def html(self):
        return self.getattr('html')


def list_questions_in_a_quiz_or_a_submission(
    session,
    base_url,
    course_id,
    quiz_id,
    quiz_submission_id: Optional[int] = None,
    quiz_submission_attempt: Optional[int] = None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List questions in a quiz or a submission

    `GET /api/v1/courses/:course_id/quizzes/:quiz_id/questions`

    Returns the paginated list of QuizQuestions in this quiz.

    https://canvas.instructure.com/doc/api/quiz_questions.html#method.quizzes/quiz_questions.index

    Returns:
        a list of QuizQuestions
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/quizzes/{quiz_id}/questions'.format(course_id=course_id,
                                                                           quiz_id=quiz_id)
    query = [
        ('quiz_submission_id', quiz_submission_id),
        ('quiz_submission_attempt', quiz_submission_attempt),
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
        constructor=QuizQuestion,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def get_a_single_quiz_question(
    session,
    base_url,
    course_id,
    quiz_id,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get a single quiz question

    `GET /api/v1/courses/:course_id/quizzes/:quiz_id/questions/:id`

    Returns the quiz question with the given id

    https://canvas.instructure.com/doc/api/quiz_questions.html#method.quizzes/quiz_questions.show

    Returns:
        a QuizQuestion
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/quizzes/{quiz_id}/questions/{id}'.format(course_id=course_id,
                                                                                quiz_id=quiz_id,
                                                                                id=id)
    query = []
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def create_a_single_quiz_question():
    """
    Create a single quiz question

    `POST /api/v1/courses/:course_id/quizzes/:quiz_id/questions`

    Create a new quiz question for this quiz

    https://canvas.instructure.com/doc/api/quiz_questions.html#method.quizzes/quiz_questions.create

    Returns:
        a QuizQuestion
    """
    raise NotImplementedError


def update_an_existing_quiz_question():
    """
    Update an existing quiz question

    `PUT /api/v1/courses/:course_id/quizzes/:quiz_id/questions/:id`

    Updates an existing quiz question for this quiz

    https://canvas.instructure.com/doc/api/quiz_questions.html#method.quizzes/quiz_questions.update

    Returns:
        a QuizQuestion
    """
    raise NotImplementedError


def delete_a_quiz_question():
    """
    Delete a quiz question

    `DELETE /api/v1/courses/:course_id/quizzes/:quiz_id/questions/:id`

    204 No Content response code is returned if the deletion was successful.

    https://canvas.instructure.com/doc/api/quiz_questions.html#method.quizzes/quiz_questions.destroy
    """
    raise NotImplementedError
