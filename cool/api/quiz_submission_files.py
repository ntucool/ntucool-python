from cool import utils


def upload_a_file(
    session,
    base_url,
    course_id,
    quiz_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Upload a file

    `POST /api/v1/courses/:course_id/quizzes/:quiz_id/submissions/self/files`

    Associate a new quiz submission file

    This API endpoint is the first step in uploading a quiz submission file. See the File Upload Documentation for details on the file upload workflow as these parameters are interpreted as per the documentation there.

    https://canvas.instructure.com/doc/api/quiz_submission_files.html#method.quizzes/quiz_submission_files.create
    """
    method = 'POST'
    url = '/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/self/files'.format(
        course_id=course_id, quiz_id=quiz_id)
    query = []
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
