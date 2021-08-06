from typing import Optional

from cool import utils
from cool.api import objects, quiz_questions


class QuizSubmissionQuestion(objects.Base):
    """
    https://canvas.instructure.com/doc/api/quiz_submission_questions.html#QuizSubmissionQuestion
    """

    def __init__(self, attributes: dict, session=None, base_url: Optional[str] = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('id', 'quiz_id', 'position', 'question_name')

    @property
    def id(self):
        """The ID of the QuizQuestion this answer is for."""
        return self.getattr('id')

    @property
    def flagged(self):
        """Whether this question is flagged."""
        return self.getattr('flagged')

    @property
    def answer(self):
        """
        The provided answer (if any) for this question. The format of this parameter
        depends on the type of the question, see the Appendix for more information.
        """
        return self.getattr('answer')

    @property
    def answers(self) -> list[quiz_questions.Answer]:
        """
        The possible answers for this question when those possible answers are
        necessary.  The presence of this parameter is dependent on permissions.
        """
        return self.getattr('answers', constructor=quiz_questions.Answer, type='list')

    @property
    def quiz_id(self):
        return self.getattr('quiz_id')

    @property
    def quiz_group_id(self):
        return self.getattr('quiz_group_id')

    @property
    def assessment_question_id(self):
        return self.getattr('assessment_question_id')

    @property
    def position(self):
        return self.getattr('position')

    @property
    def question_name(self):
        return self.getattr('question_name')

    @property
    def question_type(self):
        return self.getattr('question_type')

    @property
    def question_text(self):
        return self.getattr('question_text')

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

    @property
    def correct(self):
        return self.getattr('correct')


class QuizSubmissionQuestionsResponse(objects.Base, objects.CompoundDocument):

    def __init__(self, attributes: dict, session=None, base_url: Optional[str] = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    @property
    def quiz_submission_questions(self) -> list[QuizSubmissionQuestion]:
        constructor_kwargs = {'session': self.session, 'base_url': self.base_url}
        return self.getattr('quiz_submission_questions',
                            constructor=QuizSubmissionQuestion,
                            constructor_kwargs=constructor_kwargs,
                            type='list')

    @property
    def quiz_questions(self) -> list[quiz_questions.QuizQuestion]:
        constructor_kwargs = {'session': self.session, 'base_url': self.base_url}
        return self.getattr('quiz_questions',
                            constructor=quiz_questions.QuizQuestion,
                            constructor_kwargs=constructor_kwargs,
                            type='list')


def get_all_quiz_submission_questions(
    session,
    base_url,
    quiz_submission_id,
    include=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get all quiz submission questions.

    `GET /api/v1/quiz_submissions/:quiz_submission_id/questions`

    Get a list of all the question records for this quiz submission.

    200 OK response code is returned if the request was successful.

    https://canvas.instructure.com/doc/api/quiz_submission_questions.html#method.quizzes/quiz_submission_questions.index
    """
    method = 'GET'
    url = '/api/v1/quiz_submissions/{quiz_submission_id}/questions'.format(
        quiz_submission_id=quiz_submission_id)
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
    return QuizSubmissionQuestionsResponse(data, session=session, base_url=base_url)


def answering_questions(
    session,
    base_url,
    quiz_submission_id,
    attempt: Optional[int] = None,
    validation_token: Optional[str] = None,
    access_code: Optional[str] = None,
    quiz_questions=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Answering questions

    `POST /api/v1/quiz_submissions/:quiz_submission_id/questions`

    Provide or update an answer to one or more QuizQuestions.

    https://canvas.instructure.com/doc/api/quiz_submission_questions.html#method.quizzes/quiz_submission_questions.answer

    Returns:
        a list of QuizSubmissionQuestions
    """
    method = 'POST'
    url = '/api/v1/quiz_submissions/{quiz_submission_id}/questions'.format(
        quiz_submission_id=quiz_submission_id)
    query = [
        ('attempt', attempt),
        ('validation_token', validation_token),
        ('access_code', access_code),
        ('quiz_questions', quiz_questions),
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


def get_a_formatted_student_numerical_answer(
    session,
    base_url,
    quiz_submission_id,
    id,
    answer=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get a formatted student numerical answer.

    `GET /api/v1/quiz_submissions/:quiz_submission_id/questions/:id/formatted_answer`

    Matches the intended behavior of the UI when a numerical answer is entered and returns the resulting formatted number

    https://canvas.instructure.com/doc/api/quiz_submission_questions.html#method.quizzes/quiz_submission_questions.formatted_answer
    """
    method = 'GET'
    url = '/api/v1/quiz_submissions/{quiz_submission_id}/questions/{id}/formatted_answer'.format(
        quiz_submission_id=quiz_submission_id, id=id)
    query = [
        ('answer', answer),
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


def flagging_a_question(
    session,
    base_url,
    quiz_submission_id,
    attempt: Optional[int] = None,
    validation_token: Optional[str] = None,
    access_code: Optional[str] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Flagging a question.

    `PUT /api/v1/quiz_submissions/:quiz_submission_id/questions/:id/flag`

    Set a flag on a quiz question to indicate that you want to return to it later.

    https://canvas.instructure.com/doc/api/quiz_submission_questions.html#method.quizzes/quiz_submission_questions.flag
    """
    method = 'PUT'
    url = '/api/v1/quiz_submissions/{quiz_submission_id}/questions/{id}/flag'.format(
        quiz_submission_id=quiz_submission_id, id=id)
    query = [
        ('attempt', attempt),
        ('validation_token', validation_token),
        ('access_code', access_code),
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


def unflagging_a_question(
    session,
    base_url,
    quiz_submission_id,
    attempt: Optional[int] = None,
    validation_token: Optional[str] = None,
    access_code: Optional[str] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Unflagging a question.

    `PUT /api/v1/quiz_submissions/:quiz_submission_id/questions/:id/unflag`

    Remove the flag that you previously set on a quiz question after you've returned to it.

    https://canvas.instructure.com/doc/api/quiz_submission_questions.html#method.quizzes/quiz_submission_questions.unflag
    """
    method = 'PUT'
    url = '/api/v1/quiz_submissions/{quiz_submission_id}/questions/{id}/unflag'.format(
        quiz_submission_id=quiz_submission_id, id=id)
    query = [
        ('attempt', attempt),
        ('validation_token', validation_token),
        ('access_code', access_code),
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
