from typing import Optional

from cool import utils
from cool.api import objects


class QuizSubmissionEvent(objects.Base):
    """
    An event passed from the Quiz Submission take page

    https://canvas.instructure.com/doc/api/quiz_submission_events.html#QuizSubmissionEvent
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    @property
    def created_at(self):
        """a timestamp record of creation time"""
        return self.getattr('created_at')

    @property
    def event_type(self):
        """the type of event being sent"""
        return self.getattr('event_type')

    @property
    def event_data(self):
        """custom contextual data for the specific event type"""
        return self.getattr('event_data')


def submit_captured_events(
    session,
    base_url,
    course_id,
    quiz_id,
    id,
    quiz_submission_events=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Submit captured events

    `POST /api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id/events`

    Store a set of events which were captured during a quiz taking session.

    On success, the response will be 204 No Content with an empty body.

    https://canvas.instructure.com/doc/api/quiz_submission_events.html#method.quizzes/quiz_submission_events_api.create
    """
    method = 'POST'
    url = '/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/events'.format(
        course_id=course_id, quiz_id=quiz_id, id=id)
    query = [
        ('quiz_submission_events', quiz_submission_events),
    ]
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def retrieve_captured_events(
    session,
    base_url,
    course_id,
    quiz_id,
    id,
    attempt: Optional[int] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Retrieve captured events

    `GET /api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id/events`

    Retrieve the set of events captured during a specific submission attempt.

    https://canvas.instructure.com/doc/api/quiz_submission_events.html#method.quizzes/quiz_submission_events_api.index
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/events'.format(
        course_id=course_id, quiz_id=quiz_id, id=id)
    query = [
        ('attempt', attempt),
    ]
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
