from typing import Optional

from cool import utils
from cool.api import common, objects, quizzes


class QuizSubmission(objects.Base):
    """
    https://canvas.instructure.com/doc/api/quiz_submissions.html#QuizSubmission
    """

    def __init__(self, attributes: dict, session=None, base_url: Optional[str] = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('id', 'quiz_id', 'user_id', 'submission_id', 'attempt')

    @property
    def id(self):
        """The ID of the quiz submission."""
        return self.getattr('id')

    @property
    def quiz_id(self):
        """The ID of the Quiz the quiz submission belongs to."""
        return self.getattr('quiz_id')

    @property
    def user_id(self):
        """The ID of the Student that made the quiz submission."""
        return self.getattr('user_id')

    @property
    def submission_id(self):
        """The ID of the Submission the quiz submission represents."""
        return self.getattr('submission_id')

    @property
    def started_at(self):
        """The time at which the student started the quiz submission."""
        return self.getattr('started_at')

    @property
    def finished_at(self):
        """The time at which the student submitted the quiz submission."""
        return self.getattr('finished_at')

    @property
    def end_at(self):
        """
        The time at which the quiz submission will be overdue, and be flagged as a
        late submission.
        """
        return self.getattr('end_at')

    @property
    def attempt(self):
        """
        For quizzes that allow multiple attempts, this field specifies the quiz
        submission attempt number.
        """
        return self.getattr('attempt')

    @property
    def extra_attempts(self):
        """
        Number of times the student was allowed to re-take the quiz over the
        multiple-attempt limit.
        """
        return self.getattr('extra_attempts')

    @property
    def extra_time(self):
        """Amount of extra time allowed for the quiz submission, in minutes."""
        return self.getattr('extra_time')

    @property
    def manually_unlocked(self):
        """The student can take the quiz even if it's locked for everyone else"""
        return self.getattr('manually_unlocked')

    @property
    def time_spent(self):
        """Amount of time spent, in seconds."""
        return self.getattr('time_spent')

    @property
    def score(self):
        """The score of the quiz submission, if graded."""
        return self.getattr('score')

    @property
    def score_before_regrade(self):
        """The original score of the quiz submission prior to any re-grading."""
        return self.getattr('score_before_regrade')

    @property
    def kept_score(self):
        """
        For quizzes that allow multiple attempts, this is the score that will be
        used, which might be the score of the latest, or the highest, quiz
        submission.
        """
        return self.getattr('kept_score')

    @property
    def fudge_points(self):
        """Number of points the quiz submission's score was fudged by."""
        return self.getattr('fudge_points')

    @property
    def has_seen_results(self):
        """Whether the student has viewed their results to the quiz."""
        return self.getattr('has_seen_results')

    @property
    def workflow_state(self):
        """
        The current state of the quiz submission. Possible values:
        ['untaken'|'pending_review'|'complete'|'settings_only'|'preview'].
        """
        return self.getattr('workflow_state')

    @property
    def overdue_and_needs_submission(self):
        """Indicates whether the quiz submission is overdue and needs submission"""
        return self.getattr('overdue_and_needs_submission')

    @property
    def quiz_version(self):
        return self.getattr('quiz_version')

    @property
    def quiz_points_possible(self):
        return self.getattr('quiz_points_possible')

    @property
    def validation_token(self):
        return self.getattr('validation_token')

    @property
    def attempts_left(self):
        return self.getattr('attempts_left')

    @property
    def excused(self):
        return self.getattr('excused?')

    @property
    def html_url(self):
        return self.getattr('html_url')

    @property
    def result_url(self):
        return self.getattr('result_url')


class QuizSubmissionsResponse(objects.Base, objects.CompoundDocument):

    def __init__(self, attributes: dict, session=None, base_url: Optional[str] = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    @property
    def quiz_submissions(self) -> list[QuizSubmission]:
        constructor_kwargs = {'session': self.session, 'base_url': self.base_url}
        return self.getattr('quiz_submissions',
                            constructor=QuizSubmission,
                            constructor_kwargs=constructor_kwargs,
                            type='list')

    @property
    def submissions(self) -> list[common.Submission]:
        constructor_kwargs = {'session': self.session, 'base_url': self.base_url}
        return self.getattr('submissions',
                            constructor=common.Submission,
                            constructor_kwargs=constructor_kwargs,
                            type='list')

    @property
    def quizzes(self) -> list[quizzes.Quiz]:
        constructor_kwargs = {'session': self.session, 'base_url': self.base_url}
        return self.getattr('quizzes',
                            constructor=quizzes.Quiz,
                            constructor_kwargs=constructor_kwargs,
                            type='list')

    @property
    def users(self) -> list[common.User]:
        constructor_kwargs = {'session': self.session, 'base_url': self.base_url}
        return self.getattr('users',
                            constructor=common.User,
                            constructor_kwargs=constructor_kwargs,
                            type='list')


def get_all_quiz_submissions(
    session,
    base_url,
    course_id,
    quiz_id,
    include=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get all quiz submissions.

    `GET /api/v1/courses/:course_id/quizzes/:quiz_id/submissions`

    Get a list of all submissions for this quiz. Users who can view or manage grades for a course will have submissions from multiple users returned. A user who can only submit will have only their own submissions returned. When a user has an in-progress submission, only that submission is returned. When there isn't an in-progress quiz_submission, all completed submissions, including previous attempts, are returned.

    200 OK response code is returned if the request was successful.

    https://canvas.instructure.com/doc/api/quiz_submissions.html#method.quizzes/quiz_submissions_api.index
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions'.format(course_id=course_id,
                                                                             quiz_id=quiz_id)
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
    return QuizSubmissionsResponse(data, session=session, base_url=base_url)


def get_the_quiz_submission(
    session,
    base_url,
    course_id,
    quiz_id,
    include=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get the quiz submission.

    `GET /api/v1/courses/:course_id/quizzes/:quiz_id/submission`

    Get the submission for this quiz for the current user.

    200 OK response code is returned if the request was successful.

    https://canvas.instructure.com/doc/api/quiz_submissions.html#method.quizzes/quiz_submissions_api.submission
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/quizzes/{quiz_id}/submission'.format(course_id=course_id,
                                                                            quiz_id=quiz_id)
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
    return QuizSubmissionsResponse(data, session=session, base_url=base_url)


def get_a_single_quiz_submission(
    session,
    base_url,
    course_id,
    quiz_id,
    id,
    include=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get a single quiz submission.

    `GET /api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id`

    Get a single quiz submission.

    200 OK response code is returned if the request was successful.

    https://canvas.instructure.com/doc/api/quiz_submissions.html#method.quizzes/quiz_submissions_api.show
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}'.format(
        course_id=course_id, quiz_id=quiz_id, id=id)
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
    return QuizSubmissionsResponse(data, session=session, base_url=base_url)


def create_the_quiz_submission_start_a_quiz_taking_session(
    session,
    base_url,
    course_id,
    quiz_id,
    access_code: Optional[str] = None,
    preview: Optional[bool] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Create the quiz submission (start a quiz-taking session)

    `POST /api/v1/courses/:course_id/quizzes/:quiz_id/submissions`

    Start taking a Quiz by creating a QuizSubmission which you can use to answer questions and submit your answers.

    https://canvas.instructure.com/doc/api/quiz_submissions.html#method.quizzes/quiz_submissions_api.create
    """
    method = 'POST'
    url = '/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions'.format(course_id=course_id,
                                                                             quiz_id=quiz_id)
    query = [
        ('access_code', access_code),
        ('preview', preview),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return QuizSubmissionsResponse(data, session=session, base_url=base_url)


def update_student_question_scores_and_comments(
    session,
    base_url,
    course_id,
    quiz_id,
    id,
    quiz_submissions=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Update student question scores and comments.

    `PUT /api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id`

    Update the amount of points a student has scored for questions they've answered, provide comments for the student about their answer(s), or simply fudge the total score by a specific amount of points.

    https://canvas.instructure.com/doc/api/quiz_submissions.html#method.quizzes/quiz_submissions_api.update
    """
    method = 'PUT'
    url = '/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}'.format(
        course_id=course_id, quiz_id=quiz_id, id=id)
    query = [
        ('quiz_submissions', quiz_submissions),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return QuizSubmissionsResponse(data, session=session, base_url=base_url)


def complete_the_quiz_submission_turn_it_in(
    session,
    base_url,
    course_id,
    quiz_id,
    id,
    attempt: Optional[int] = None,
    validation_token: Optional[str] = None,
    access_code: Optional[str] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Complete the quiz submission (turn it in).

    `POST /api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id/complete`

    Complete the quiz submission by marking it as complete and grading it. When the quiz submission has been marked as complete, no further modifications will be allowed.

    https://canvas.instructure.com/doc/api/quiz_submissions.html#method.quizzes/quiz_submissions_api.complete
    """
    method = 'POST'
    url = '/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/complete'.format(
        course_id=course_id, quiz_id=quiz_id, id=id)
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
    return QuizSubmissionsResponse(data, session=session, base_url=base_url)


def get_current_quiz_submission_times(
    session,
    base_url,
    course_id,
    quiz_id,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get current quiz submission times.

    `GET /api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id/time`

    Get the current timing data for the quiz attempt, both the end_at timestamp and the time_left parameter.

    https://canvas.instructure.com/doc/api/quiz_submissions.html#method.quizzes/quiz_submissions_api.time
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/time'.format(
        course_id=course_id, quiz_id=quiz_id, id=id)
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
