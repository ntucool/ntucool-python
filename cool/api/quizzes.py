from typing import Literal, Optional, Union

from cool import utils
from cool.api import objects, paginations


class QuizPermissions(objects.Simple):
    """
    https://canvas.instructure.com/doc/api/quizzes.html#QuizPermissions
    """

    def __init__(self, attributes: dict) -> None:
        super().__init__(attributes=attributes)

    @property
    def read(self):
        """
        Permissions the user has for the quiz
        whether the user can view the quiz
        """
        return self.getattr('read')

    @property
    def submit(self):
        """whether the user may submit a submission for the quiz"""
        return self.getattr('submit')

    @property
    def create(self):
        """whether the user may create a new quiz"""
        return self.getattr('create')

    @property
    def manage(self):
        """whether the user may edit, update, or delete the quiz"""
        return self.getattr('manage')

    @property
    def read_statistics(self):
        """whether the user may view quiz statistics for this quiz"""
        return self.getattr('read_statistics')

    @property
    def review_grades(self):
        """whether the user may review grades for all quiz submissions for this quiz"""
        return self.getattr('review_grades')

    @property
    def update(self):
        """whether the user may update the quiz"""
        return self.getattr('update')

    @property
    def preview(self):
        return self.getattr('preview')

    @property
    def delete(self):
        return self.getattr('delete')

    @property
    def grade(self):
        return self.getattr('grade')

    @property
    def view_answer_audits(self):
        return self.getattr('view_answer_audits')


class Quiz(objects.Base):
    """
    https://canvas.instructure.com/doc/api/quizzes.html#Quiz
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('id', 'title')

    @property
    def id(self):
        """the ID of the quiz"""
        return self.getattr('id')

    @property
    def title(self):
        """the title of the quiz"""
        return self.getattr('title')

    @property
    def html_url(self):
        """the HTTP/HTTPS URL to the quiz"""
        return self.getattr('html_url')

    @property
    def mobile_url(self):
        """
        a url suitable for loading the quiz in a mobile webview.  it will persiste
        the headless session and, for quizzes in public courses, will force the user
        to login
        """
        return self.getattr('mobile_url')

    @property
    def preview_url(self):
        """
        A url that can be visited in the browser with a POST request to preview a
        quiz as the teacher. Only present when the user may grade
        """
        return self.getattr('preview_url')

    @property
    def description(self):
        """the description of the quiz"""
        return self.getattr('description')

    @property
    def quiz_type(self):
        """
        type of quiz possible values: 'practice_quiz', 'assignment', 'graded_survey',
        'survey'
        """
        return self.getattr('quiz_type')

    @property
    def assignment_group_id(self):
        """the ID of the quiz's assignment group:"""
        return self.getattr('assignment_group_id')

    @property
    def time_limit(self):
        """quiz time limit in minutes"""
        return self.getattr('time_limit')

    @property
    def shuffle_answers(self):
        """shuffle answers for students?"""
        return self.getattr('shuffle_answers')

    @property
    def hide_results(self):
        """
        let students see their quiz responses? possible values: null, 'always',
        'until_after_last_attempt'
        """
        return self.getattr('hide_results')

    @property
    def show_correct_answers(self):
        """
        show which answers were correct when results are shown? only valid if
        hide_results=null
        """
        return self.getattr('show_correct_answers')

    @property
    def show_correct_answers_last_attempt(self):
        """
        restrict the show_correct_answers option above to apply only to the last
        submitted attempt of a quiz that allows multiple attempts. only valid if
        show_correct_answers=true and allowed_attempts > 1
        """
        return self.getattr('show_correct_answers_last_attempt')

    @property
    def show_correct_answers_at(self):
        """
        when should the correct answers be visible by students? only valid if
        show_correct_answers=true
        """
        return self.getattr('show_correct_answers_at')

    @property
    def hide_correct_answers_at(self):
        """
        prevent the students from seeing correct answers after the specified date has
        passed. only valid if show_correct_answers=true
        """
        return self.getattr('hide_correct_answers_at')

    @property
    def one_time_results(self):
        """
        prevent the students from seeing their results more than once (right after
        they submit the quiz)
        """
        return self.getattr('one_time_results')

    @property
    def scoring_policy(self):
        """
        which quiz score to keep (only if allowed_attempts != 1) possible values:
        'keep_highest', 'keep_latest'
        """
        return self.getattr('scoring_policy')

    @property
    def allowed_attempts(self):
        """how many times a student can take the quiz -1 = unlimited attempts"""
        return self.getattr('allowed_attempts')

    @property
    def one_question_at_a_time(self):
        """show one question at a time?"""
        return self.getattr('one_question_at_a_time')

    @property
    def question_count(self):
        """the number of questions in the quiz"""
        return self.getattr('question_count')

    @property
    def points_possible(self):
        """The total point value given to the quiz"""
        return self.getattr('points_possible')

    @property
    def cant_go_back(self):
        """lock questions after answering? only valid if one_question_at_a_time=true"""
        return self.getattr('cant_go_back')

    @property
    def access_code(self):
        """access code to restrict quiz access"""
        return self.getattr('access_code')

    @property
    def ip_filter(self):
        """IP address or range that quiz access is limited to"""
        return self.getattr('ip_filter')

    @property
    def due_at(self):
        """when the quiz is due"""
        return self.getattr('due_at')

    @property
    def lock_at(self):
        """when to lock the quiz"""
        return self.getattr('lock_at')

    @property
    def unlock_at(self):
        """when to unlock the quiz"""
        return self.getattr('unlock_at')

    @property
    def published(self):
        """whether the quiz has a published or unpublished draft state."""
        return self.getattr('published')

    @property
    def unpublishable(self):
        """
        Whether the assignment's 'published' state can be changed to false. Will be
        false if there are student submissions for the quiz.
        """
        return self.getattr('unpublishable')

    @property
    def locked_for_user(self):
        """Whether or not this is locked for the user."""
        return self.getattr('locked_for_user')

    @property
    def lock_info(self):
        """
        (Optional) Information for the user about the lock. Present when
        locked_for_user is true.
        """
        return self.getattr('lock_info')

    @property
    def lock_explanation(self):
        """
        (Optional) An explanation of why this is locked for the user. Present when
        locked_for_user is true.
        """
        return self.getattr('lock_explanation')

    @property
    def speedgrader_url(self):
        """
        Link to Speed Grader for this quiz. Will not be present if quiz is
        unpublished
        """
        return self.getattr('speedgrader_url')

    @property
    def quiz_extensions_url(self):
        """Link to endpoint to send extensions for this quiz."""
        return self.getattr('quiz_extensions_url')

    @property
    def permissions(self) -> QuizPermissions:
        """Permissions the user has for the quiz"""
        return self.getattr('permissions', constructor=QuizPermissions)

    @property
    def all_dates(self):
        """list of due dates for the quiz"""
        return self.getattr('all_dates')

    @property
    def version_number(self):
        """Current version number of the quiz"""
        return self.getattr('version_number')

    @property
    def question_types(self):
        """List of question types in the quiz"""
        return self.getattr('question_types')

    @property
    def anonymous_submissions(self):
        """
        Whether survey submissions will be kept anonymous (only applicable to
        'graded_survey', 'survey' quiz types)
        """
        return self.getattr('anonymous_submissions')

    @property
    def timer_autosubmit_disabled(self):
        return self.getattr('timer_autosubmit_disabled')

    @property
    def can_update(self):
        return self.getattr('can_update')

    @property
    def require_lockdown_browser(self):
        return self.getattr('require_lockdown_browser')

    @property
    def require_lockdown_browser_for_results(self):
        return self.getattr('require_lockdown_browser_for_results')

    @property
    def require_lockdown_browser_monitor(self):
        return self.getattr('require_lockdown_browser_monitor')

    @property
    def lockdown_browser_monitor_data(self):
        return self.getattr('lockdown_browser_monitor_data')

    @property
    def quiz_reports_url(self):
        return self.getattr('quiz_reports_url')

    @property
    def quiz_statistics_url(self):
        return self.getattr('quiz_statistics_url')

    @property
    def quiz_submission_versions_html_url(self):
        return self.getattr('quiz_submission_versions_html_url')

    @property
    def assignment_id(self):
        return self.getattr('assignment_id')

    @property
    def has_access_code(self):
        return self.getattr('has_access_code')

    @property
    def post_to_sis(self):
        return self.getattr('post_to_sis')

    @property
    def migration_id(self):
        return self.getattr('migration_id')


def list_quizzes_in_a_course(
    session,
    base_url,
    course_id,
    search_term: Optional[str] = None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List quizzes in a course

    `GET /api/v1/courses/:course_id/quizzes`

    Returns the paginated list of Quizzes in this course.

    https://canvas.instructure.com/doc/api/quizzes.html#method.quizzes/quizzes_api.index

    Returns:
        a list of Quizzes
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/quizzes'.format(course_id=course_id)
    query = [
        ('search_term', search_term),
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
        constructor=Quiz,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def get_a_single_quiz(
    session,
    base_url,
    course_id,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get a single quiz

    `GET /api/v1/courses/:course_id/quizzes/:id`

    Returns the quiz with the given id.

    https://canvas.instructure.com/doc/api/quizzes.html#method.quizzes/quizzes_api.show

    Returns:
        a Quiz
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/quizzes/{id}'.format(course_id=course_id, id=id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Quiz(data, session=session, base_url=base_url)


def create_a_quiz(
    session,
    base_url,
    course_id,
    quiz=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Create a quiz

    `POST /api/v1/courses/:course_id/quizzes`

    Create a new quiz for this course.

    https://canvas.instructure.com/doc/api/quizzes.html#method.quizzes/quizzes_api.create

    Returns:
        a Quiz
    """
    method = 'POST'
    url = '/api/v1/courses/{course_id}/quizzes'.format(course_id=course_id)
    query = [
        ('quiz', quiz),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Quiz(data, session=session, base_url=base_url)


def edit_a_quiz(
    session,
    base_url,
    course_id,
    id,
    quiz=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Edit a quiz

    `PUT /api/v1/courses/:course_id/quizzes/:id`

    Modify an existing quiz. See the documentation for quiz creation.

    https://canvas.instructure.com/doc/api/quizzes.html#method.quizzes/quizzes_api.update

    Returns:
        a Quiz
    """
    method = 'PUT'
    url = '/api/v1/courses/{course_id}/quizzes/{id}'.format(course_id=course_id, id=id)
    query = [
        ('quiz', quiz),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Quiz(data, session=session, base_url=base_url)


def delete_a_quiz(
    session,
    base_url,
    course_id,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Delete a quiz

    `DELETE /api/v1/courses/:course_id/quizzes/:id`

    https://canvas.instructure.com/doc/api/quizzes.html#method.quizzes/quizzes_api.destroy
    """
    method = 'DELETE'
    url = '/api/v1/courses/{course_id}/quizzes/{id}'.format(course_id=course_id, id=id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Quiz(data, session=session, base_url=base_url)


def reorder_quiz_items(
    session,
    base_url,
    course_id,
    id,
    order=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Reorder quiz items

    `POST /api/v1/courses/:course_id/quizzes/:id/reorder`

    Change order of the quiz questions or groups within the quiz

    204 No Content response code is returned if the reorder was successful.

    https://canvas.instructure.com/doc/api/quizzes.html#method.quizzes/quizzes_api.reorder
    """
    method = 'POST'
    url = '/api/v1/courses/{course_id}/quizzes/{id}/reorder'.format(course_id=course_id, id=id)
    query = [
        ('order', order),
    ]
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def validate_quiz_access_code(
    session,
    base_url,
    course_id,
    id,
    access_code: Optional[str] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Validate quiz access code

    `POST /api/v1/courses/:course_id/quizzes/:id/validate_access_code`

    Accepts an access code and returns a boolean indicating whether that access code is correct

    https://canvas.instructure.com/doc/api/quizzes.html#method.quizzes/quizzes_api.validate_access_code
    """
    method = 'POST'
    url = '/api/v1/courses/{course_id}/quizzes/{id}/validate_access_code'.format(
        course_id=course_id, id=id)
    query = [
        ('access_code', access_code),
    ]
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
