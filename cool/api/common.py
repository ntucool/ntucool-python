from typing import Literal, Optional, Union

from cool import utils
from cool.api import objects, paginations


class ExternalToolTagAttributes(objects.Simple):
    """
    https://canvas.instructure.com/doc/api/assignments.html#ExternalToolTagAttributes
    """

    def __init__(self, attributes: dict) -> None:
        super().__init__(attributes=attributes)

    @property
    def url(self):
        """URL to the external tool"""
        return self.getattr('url')

    @property
    def new_tab(self):
        """Whether or not there is a new tab for the external tool"""
        return self.getattr('new_tab')

    @property
    def resource_link_id(self):
        """the identifier for this tool_tag"""
        return self.getattr('resource_link_id')


class LockInfo(objects.Simple):
    """
    https://canvas.instructure.com/doc/api/assignments.html#LockInfo
    """

    def __init__(self, attributes: dict) -> None:
        super().__init__(attributes=attributes)

    repr_names = ('asset_string',)

    @property
    def asset_string(self):
        """Asset string for the object causing the lock"""
        return self.getattr('asset_string')

    @property
    def unlock_at(self):
        """
        (Optional) Time at which this was/will be unlocked. Must be before the due
        date.
        """
        return self.getattr('unlock_at')

    @property
    def lock_at(self):
        """(Optional) Time at which this was/will be locked. Must be after the due date."""
        return self.getattr('lock_at')

    @property
    def context_module(self):
        """(Optional) Context module causing the lock."""
        return self.getattr('context_module')

    @property
    def manually_locked(self):
        return self.getattr('manually_locked')

    @property
    def can_view(self):
        return self.getattr('can_view')


class RubricRating(objects.Simple):
    """
    https://canvas.instructure.com/doc/api/assignments.html#RubricRating
    """

    def __init__(self, attributes: dict) -> None:
        super().__init__(attributes=attributes)

    repr_names = ('id', 'points', 'description')

    @property
    def points(self):
        return self.getattr('points')

    @property
    def id(self):
        return self.getattr('id')

    @property
    def description(self):
        return self.getattr('description')

    @property
    def long_description(self):
        return self.getattr('long_description')


class RubricCriteria(objects.Simple):
    """
    https://canvas.instructure.com/doc/api/assignments.html#RubricCriteria
    """

    def __init__(self, attributes: dict) -> None:
        super().__init__(attributes=attributes)

    repr_names = ('id', 'points', 'description')

    @property
    def points(self):
        return self.getattr('points')

    @property
    def id(self):
        """The id of rubric criteria."""
        return self.getattr('id')

    @property
    def learning_outcome_id(self):
        """(Optional) The id of the learning outcome this criteria uses, if any."""
        return self.getattr('learning_outcome_id')

    @property
    def vendor_guid(self):
        """
        (Optional) The 3rd party vendor's GUID for the outcome this criteria
        references, if any.
        """
        return self.getattr('vendor_guid')

    @property
    def description(self):
        return self.getattr('description')

    @property
    def long_description(self):
        return self.getattr('long_description')

    @property
    def criterion_use_range(self):
        return self.getattr('criterion_use_range')

    @property
    def ratings(self) -> list[RubricRating]:
        return self.getattr('ratings', constructor=RubricRating, type='list')

    @property
    def ignore_for_scoring(self):
        return self.getattr('ignore_for_scoring')


class AssignmentDate(objects.Simple):
    """
    Object representing a due date for an assignment or quiz. If the due date
    came from an assignment override, it will have an 'id' field.

    https://canvas.instructure.com/doc/api/assignments.html#AssignmentDate
    """

    def __init__(self, attributes: dict) -> None:
        super().__init__(attributes=attributes)

    @property
    def id(self):
        """
        (Optional, missing if 'base' is present) id of the assignment override this
        date represents
        """
        return self.getattr('id')

    @property
    def base(self):
        """
        (Optional, present if 'id' is missing) whether this date represents the
        assignment's or quiz's default due date
        """
        return self.getattr('base')

    @property
    def title(self):
        return self.getattr('title')

    @property
    def due_at(self):
        """
        The due date for the assignment. Must be between the unlock date and the lock
        date if there are lock dates
        """
        return self.getattr('due_at')

    @property
    def unlock_at(self):
        """
        The unlock date for the assignment. Must be before the due date if there is a
        due date.
        """
        return self.getattr('unlock_at')

    @property
    def lock_at(self):
        """
        The lock date for the assignment. Must be after the due date if there is a
        due date.
        """
        return self.getattr('lock_at')

    @property
    def in_closed_grading_period(self):
        return self.getattr('in_closed_grading_period')

    @property
    def can_edit(self):
        """
        an extra Boolean value will be included with each Assignment (and AssignmentDate if all_dates is supplied) to indicate whether the caller can edit the assignment or date. Moderated grading and closed grading periods may restrict a user's ability to edit an assignment.

        https://canvas.instructure.com/doc/api/assignments.html#method.assignments_api.index
        """
        return self.getattr('can_edit')


class ScoreStatistic(objects.Simple):
    """
    Used by Assignment model

    https://canvas.instructure.com/doc/api/assignments.html#ScoreStatistic
    """

    repr_names = ('min', 'max', 'mean')

    def __init__(self, attributes: dict) -> None:
        super().__init__(attributes=attributes)

    @property
    def min(self):
        """Min score"""
        return self.getattr('min')

    @property
    def max(self):
        """Max score"""
        return self.getattr('max')

    @property
    def mean(self):
        """Mean score"""
        return self.getattr('mean')


class Assignment(objects.Base):
    """
    https://canvas.instructure.com/doc/api/assignments.html#Assignment
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('id', 'name')

    @property
    def id(self):
        """the ID of the assignment"""
        return self.getattr('id')

    @property
    def name(self):
        """the name of the assignment"""
        return self.getattr('name')

    @property
    def description(self):
        """the assignment description, in an HTML fragment"""
        return self.getattr('description')

    @property
    def created_at(self):
        """The time at which this assignment was originally created"""
        return self.getattr('created_at')

    @property
    def updated_at(self):
        """The time at which this assignment was last modified in any way"""
        return self.getattr('updated_at')

    @property
    def due_at(self):
        """
        the due date for the assignment. returns null if not present. NOTE: If this
        assignment has assignment overrides, this field will be the due date as it
        applies to the user requesting information from the API.
        """
        return self.getattr('due_at')

    @property
    def lock_at(self):
        """
        the lock date (assignment is locked after this date). returns null if not
        present. NOTE: If this assignment has assignment overrides, this field will
        be the lock date as it applies to the user requesting information from the
        API.
        """
        return self.getattr('lock_at')

    @property
    def unlock_at(self):
        """
        the unlock date (assignment is unlocked after this date) returns null if not
        present NOTE: If this assignment has assignment overrides, this field will be
        the unlock date as it applies to the user requesting information from the
        API.
        """
        return self.getattr('unlock_at')

    @property
    def has_overrides(self):
        """whether this assignment has overrides"""
        return self.getattr('has_overrides')

    @property
    def all_dates(self) -> list[AssignmentDate]:
        """(Optional) all dates associated with the assignment, if applicable"""
        return self.getattr('all_dates', constructor=AssignmentDate, type='list')

    @property
    def course_id(self):
        """the ID of the course the assignment belongs to"""
        return self.getattr('course_id')

    @property
    def html_url(self):
        """the URL to the assignment's web page"""
        return self.getattr('html_url')

    @property
    def submissions_download_url(self):
        """the URL to download all submissions as a zip"""
        return self.getattr('submissions_download_url')

    @property
    def assignment_group_id(self):
        """the ID of the assignment's group"""
        return self.getattr('assignment_group_id')

    @property
    def due_date_required(self):
        """
        Boolean flag indicating whether the assignment requires a due date based on
        the account level setting
        """
        return self.getattr('due_date_required')

    @property
    def allowed_extensions(self):
        """
        Allowed file extensions, which take effect if submission_types includes
        'online_upload'.
        """
        return self.getattr('allowed_extensions')

    @property
    def max_name_length(self):
        """An integer indicating the maximum length an assignment's name may be"""
        return self.getattr('max_name_length')

    @property
    def turnitin_enabled(self):
        """
        Boolean flag indicating whether or not Turnitin has been enabled for the
        assignment. NOTE: This flag will not appear unless your account has the
        Turnitin plugin available
        """
        return self.getattr('turnitin_enabled')

    @property
    def vericite_enabled(self):
        """
        Boolean flag indicating whether or not VeriCite has been enabled for the
        assignment. NOTE: This flag will not appear unless your account has the
        VeriCite plugin available
        """
        return self.getattr('vericite_enabled')

    @property
    def turnitin_settings(self):
        """
        Settings to pass along to turnitin to control what kinds of matches should be
        considered. originality_report_visibility can be 'immediate',
        'after_grading', 'after_due_date', or 'never' exclude_small_matches_type can
        be null, 'percent', 'words' exclude_small_matches_value: - if type is null,
        this will be null also - if type is 'percent', this will be a number between
        0 and 100 representing match size to exclude as a percentage of the document
        size. - if type is 'words', this will be number > 0 representing how many
        words a match must contain for it to be considered NOTE: This flag will not
        appear unless your account has the Turnitin plugin available
        """
        return self.getattr('turnitin_settings')

    @property
    def grade_group_students_individually(self):
        """
        If this is a group assignment, boolean flag indicating whether or not
        students will be graded individually.
        """
        return self.getattr('grade_group_students_individually')

    @property
    def external_tool_tag_attributes(self):
        """
        (Optional) assignment's settings for external tools if submission_types
        include 'external_tool'. Only url and new_tab are included (new_tab defaults
        to false).  Use the 'External Tools' API if you need more information about
        an external tool.
        """
        return self.getattr('external_tool_tag_attributes', constructor=ExternalToolTagAttributes)

    @property
    def peer_reviews(self):
        """Boolean indicating if peer reviews are required for this assignment"""
        return self.getattr('peer_reviews')

    @property
    def automatic_peer_reviews(self):
        """
        Boolean indicating peer reviews are assigned automatically. If false, the
        teacher is expected to manually assign peer reviews.
        """
        return self.getattr('automatic_peer_reviews')

    @property
    def peer_review_count(self):
        """
        Integer representing the amount of reviews each user is assigned. NOTE: This
        key is NOT present unless you have automatic_peer_reviews set to true.
        """
        return self.getattr('peer_review_count')

    @property
    def peer_reviews_assign_at(self):
        """
        String representing a date the reviews are due by. Must be a date that occurs
        after the default due date. If blank, or date is not after the assignment's
        due date, the assignment's due date will be used. NOTE: This key is NOT
        present unless you have automatic_peer_reviews set to true.
        """
        return self.getattr('peer_reviews_assign_at')

    @property
    def intra_group_peer_reviews(self):
        """
        Boolean representing whether or not members from within the same group on a
        group assignment can be assigned to peer review their own group's work
        """
        return self.getattr('intra_group_peer_reviews')

    @property
    def group_category_id(self):
        """
        The ID of the assignment’s group set, if this is a group assignment. For
        group discussions, set group_category_id on the discussion topic, not the
        linked assignment.
        """
        return self.getattr('group_category_id')

    @property
    def needs_grading_count(self):
        """
        if the requesting user has grading rights, the number of submissions that
        need grading.
        """
        return self.getattr('needs_grading_count')

    @property
    def needs_grading_count_by_section(self):
        """
        if the requesting user has grading rights and the
        'needs_grading_count_by_section' flag is specified, the number of submissions
        that need grading split out by section. NOTE: This key is NOT present unless
        you pass the 'needs_grading_count_by_section' argument as true.  ANOTHER
        NOTE: it's possible to be enrolled in multiple sections, and if a student is
        setup that way they will show an assignment that needs grading in multiple
        sections (effectively the count will be duplicated between sections)
        """
        return self.getattr('needs_grading_count_by_section')

    @property
    def position(self):
        """the sorting order of the assignment in the group"""
        return self.getattr('position')

    @property
    def post_to_sis(self):
        """(optional, present if Sync Grades to SIS feature is enabled)"""
        return self.getattr('post_to_sis')

    @property
    def integration_id(self):
        """(optional, Third Party unique identifier for Assignment)"""
        return self.getattr('integration_id')

    @property
    def integration_data(self):
        """(optional, Third Party integration data for assignment)"""
        return self.getattr('integration_data')

    @property
    def points_possible(self):
        """the maximum points possible for the assignment"""
        return self.getattr('points_possible')

    @property
    def submission_types(self):
        """
        the types of submissions allowed for this assignment list containing one or
        more of the following: 'discussion_topic', 'online_quiz', 'on_paper', 'none',
        'external_tool', 'online_text_entry', 'online_url', 'online_upload',
        'media_recording', 'student_annotation'
        """
        return self.getattr('submission_types')

    @property
    def has_submitted_submissions(self):
        """If true, the assignment has been submitted to by at least one student"""
        return self.getattr('has_submitted_submissions')

    @property
    def grading_type(self):
        """
        The type of grading the assignment receives; one of 'pass_fail', 'percent',
        'letter_grade', 'gpa_scale', 'points'
        """
        return self.getattr('grading_type')

    @property
    def grading_standard_id(self):
        """
        The id of the grading standard being applied to this assignment. Valid if
        grading_type is 'letter_grade' or 'gpa_scale'.
        """
        return self.getattr('grading_standard_id')

    @property
    def published(self):
        """Whether the assignment is published"""
        return self.getattr('published')

    @property
    def unpublishable(self):
        """
        Whether the assignment's 'published' state can be changed to false. Will be
        false if there are student submissions for the assignment.
        """
        return self.getattr('unpublishable')

    @property
    def only_visible_to_overrides(self):
        """Whether the assignment is only visible to overrides."""
        return self.getattr('only_visible_to_overrides')

    @property
    def locked_for_user(self):
        """Whether or not this is locked for the user."""
        return self.getattr('locked_for_user')

    @property
    def lock_info(self) -> LockInfo:
        """
        (Optional) Information for the user about the lock. Present when
        locked_for_user is true.
        """
        return self.getattr('lock_info', constructor=LockInfo)

    @property
    def lock_explanation(self):
        """
        (Optional) An explanation of why this is locked for the user. Present when
        locked_for_user is true.
        """
        return self.getattr('lock_explanation')

    @property
    def quiz_id(self):
        """
        (Optional) id of the associated quiz (applies only when submission_types is
        ['online_quiz'])
        """
        return self.getattr('quiz_id')

    @property
    def anonymous_submissions(self):
        """
        (Optional) whether anonymous submissions are accepted (applies only to quiz
        assignments)
        """
        return self.getattr('anonymous_submissions')

    @property
    def discussion_topic(self):
        """(Optional) the DiscussionTopic associated with the assignment, if applicable"""
        return self.getattr('discussion_topic')

    @property
    def freeze_on_copy(self):
        """
        (Optional) Boolean indicating if assignment will be frozen when it is copied.
        NOTE: This field will only be present if the AssignmentFreezer plugin is
        available for your account.
        """
        return self.getattr('freeze_on_copy')

    @property
    def frozen(self):
        """
        (Optional) Boolean indicating if assignment is frozen for the calling user.
        NOTE: This field will only be present if the AssignmentFreezer plugin is
        available for your account.
        """
        return self.getattr('frozen')

    @property
    def frozen_attributes(self):
        """
        (Optional) Array of frozen attributes for the assignment. Only account
        administrators currently have permission to change an attribute in this list.
        Will be empty if no attributes are frozen for this assignment. Possible
        frozen attributes are: title, description, lock_at, points_possible,
        grading_type, submission_types, assignment_group_id, allowed_extensions,
        group_category_id, notify_of_update, peer_reviews NOTE: This field will only
        be present if the AssignmentFreezer plugin is available for your account.
        """
        return self.getattr('frozen_attributes')

    @property
    def submission(self):
        """
        (Optional) If 'submission' is included in the 'include' parameter, includes a
        Submission object that represents the current user's (user who is requesting
        information from the api) current submission for the assignment. See the
        Submissions API for an example response. If the user does not have a
        submission, this key will be absent.
        """
        return self.getattr('submission')

    @property
    def use_rubric_for_grading(self):
        """
        (Optional) If true, the rubric is directly tied to grading the assignment.
        Otherwise, it is only advisory. Included if there is an associated rubric.
        """
        return self.getattr('use_rubric_for_grading')

    @property
    def rubric_settings(self):
        """
        (Optional) An object describing the basic attributes of the rubric, including
        the point total. Included if there is an associated rubric.
        """
        return self.getattr('rubric_settings')

    @property
    def rubric(self) -> list[RubricCriteria]:
        """
        (Optional) A list of scoring criteria and ratings for each rubric criterion.
        Included if there is an associated rubric.
        """
        return self.getattr('rubric', constructor=RubricCriteria, type='list')

    @property
    def assignment_visibility(self):
        """
        (Optional) If 'assignment_visibility' is included in the 'include' parameter,
        includes an array of student IDs who can see this assignment.
        """
        return self.getattr('assignment_visibility')

    @property
    def overrides(self):
        """
        (Optional) If 'overrides' is included in the 'include' parameter, includes an
        array of assignment override objects.
        """
        constructor_kwargs = {'session': self.session, 'base_url': self.base_url}
        return self.getattr('overrides',
                            constructor=AssignmentOverride,
                            constructor_kwargs=constructor_kwargs,
                            type='list')

    @property
    def omit_from_final_grade(self):
        """
        (Optional) If true, the assignment will be omitted from the student's final
        grade
        """
        return self.getattr('omit_from_final_grade')

    @property
    def moderated_grading(self):
        """Boolean indicating if the assignment is moderated."""
        return self.getattr('moderated_grading')

    @property
    def grader_count(self):
        """
        The maximum number of provisional graders who may issue grades for this
        assignment. Only relevant for moderated assignments. Must be a positive
        value, and must be set to 1 if the course has fewer than two active
        instructors. Otherwise, the maximum value is the number of active instructors
        in the course minus one, or 10 if the course has more than 11 active
        instructors.
        """
        return self.getattr('grader_count')

    @property
    def final_grader_id(self):
        """
        The user ID of the grader responsible for choosing final grades for this
        assignment. Only relevant for moderated assignments.
        """
        return self.getattr('final_grader_id')

    @property
    def grader_comments_visible_to_graders(self):
        """
        Boolean indicating if provisional graders' comments are visible to other
        provisional graders. Only relevant for moderated assignments.
        """
        return self.getattr('grader_comments_visible_to_graders')

    @property
    def graders_anonymous_to_graders(self):
        """
        Boolean indicating if provisional graders' identities are hidden from other
        provisional graders. Only relevant for moderated assignments with
        grader_comments_visible_to_graders set to true.
        """
        return self.getattr('graders_anonymous_to_graders')

    @property
    def grader_names_visible_to_final_grader(self):
        """
        Boolean indicating if provisional grader identities are visible to the final
        grader. Only relevant for moderated assignments.
        """
        return self.getattr('grader_names_visible_to_final_grader')

    @property
    def anonymous_grading(self):
        """
        Boolean indicating if the assignment is graded anonymously. If true, graders
        cannot see student identities.
        """
        return self.getattr('anonymous_grading')

    @property
    def allowed_attempts(self):
        """
        The number of submission attempts a student can make for this assignment. -1
        is considered unlimited.
        """
        return self.getattr('allowed_attempts')

    @property
    def post_manually(self):
        """
        Whether the assignment has manual posting enabled. Only relevant for courses
        using New Gradebook.
        """
        return self.getattr('post_manually')

    @property
    def score_statistics(self) -> ScoreStatistic:
        """
        (Optional) If 'score_statistics' and 'submission' are included in the
        'include' parameter and statistics are available, includes the min, max, and
        mode for this assignment
        """
        return self.getattr('score_statistics', constructor=ScoreStatistic)

    @property
    def can_submit(self):
        """
        (Optional) If retrieving a single assignment and 'can_submit' is included in
        the 'include' parameter, flags whether user has the right to submit the
        assignment (i.e. checks enrollment dates, submission types, locked status,
        attempts remaining, etc...). Including 'can submit' automatically includes
        'submission' in the include parameter. Not available when observed_users are
        included.
        """
        return self.getattr('can_submit')

    @property
    def anonymous_peer_reviews(self):
        return self.getattr('anonymous_peer_reviews')

    @property
    def anonymous_instructor_annotations(self):
        return self.getattr('anonymous_instructor_annotations')

    @property
    def secure_params(self):
        return self.getattr('secure_params')

    @property
    def in_closed_grading_period(self):
        return self.getattr('in_closed_grading_period')

    @property
    def is_quiz_assignment(self):
        return self.getattr('is_quiz_assignment')

    @property
    def can_duplicate(self):
        return self.getattr('can_duplicate')

    @property
    def original_course_id(self):
        return self.getattr('original_course_id')

    @property
    def original_assignment_id(self):
        return self.getattr('original_assignment_id')

    @property
    def original_assignment_name(self):
        return self.getattr('original_assignment_name')

    @property
    def original_quiz_id(self):
        return self.getattr('original_quiz_id')

    @property
    def workflow_state(self):
        return self.getattr('workflow_state')

    @property
    def muted(self):
        return self.getattr('muted')

    @property
    def anonymize_students(self):
        return self.getattr('anonymize_students')

    @property
    def require_lockdown_browser(self):
        return self.getattr('require_lockdown_browser')

    @property
    def free_form_criterion_comments(self):
        return self.getattr('free_form_criterion_comments')

    @property
    def can_edit(self):
        """
        an extra Boolean value will be included with each Assignment (and AssignmentDate if all_dates is supplied) to indicate whether the caller can edit the assignment or date. Moderated grading and closed grading periods may restrict a user's ability to edit an assignment.

        https://canvas.instructure.com/doc/api/assignments.html#method.assignments_api.index
        """
        return self.getattr('can_edit')


class AssignmentOverride(objects.Base):
    """
    https://canvas.instructure.com/doc/api/assignments.html#AssignmentOverride
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('id', 'assignment_id', 'title')

    @property
    def id(self):
        """the ID of the assignment override"""
        return self.getattr('id')

    @property
    def assignment_id(self):
        """the ID of the assignment the override applies to"""
        return self.getattr('assignment_id')

    @property
    def student_ids(self):
        """
        the IDs of the override's target students (present if the override targets an
        ad-hoc set of students)
        """
        return self.getattr('student_ids')

    @property
    def group_id(self):
        """
        the ID of the override's target group (present if the override targets a
        group and the assignment is a group assignment)
        """
        return self.getattr('group_id')

    @property
    def course_section_id(self):
        """
        the ID of the overrides's target section (present if the override targets a
        section)
        """
        return self.getattr('course_section_id')

    @property
    def title(self):
        """the title of the override"""
        return self.getattr('title')

    @property
    def due_at(self):
        """the overridden due at (present if due_at is overridden)"""
        return self.getattr('due_at')

    @property
    def all_day(self):
        """the overridden all day flag (present if due_at is overridden)"""
        return self.getattr('all_day')

    @property
    def all_day_date(self):
        """the overridden all day date (present if due_at is overridden)"""
        return self.getattr('all_day_date')

    @property
    def unlock_at(self):
        """the overridden unlock at (present if unlock_at is overridden)"""
        return self.getattr('unlock_at')

    @property
    def lock_at(self):
        """the overridden lock at, if any (present if lock_at is overridden)"""
        return self.getattr('lock_at')


def delete_an_assignment(
    session,
    base_url,
    course_id,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Delete an assignment

    `DELETE /api/v1/courses/:course_id/assignments/:id`

    Delete the given assignment.

    https://canvas.instructure.com/doc/api/assignments.html#method.assignments.destroy

    Returns:
        a Assignment
    """
    method = 'DELETE'
    url = '/api/v1/courses/{course_id}/assignments/{id}'.format(course_id=course_id, id=id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Assignment(data, session=session, base_url=base_url)


def list_assignments(
    session,
    base_url,
    course_id,
    assignment_group_id,
    include=None,
    search_term: Optional[str] = None,
    override_assignment_dates: Optional[bool] = None,
    needs_grading_count_by_section: Optional[bool] = None,
    bucket: Optional[Literal['past', 'overdue', 'undated', 'ungraded', 'unsubmitted', 'upcoming',
                             'future']] = None,
    assignment_ids=None,
    order_by: Optional[Literal['position', 'name', 'due_at']] = None,
    post_to_sis: Optional[bool] = None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List assignments

    `GET /api/v1/courses/:course_id/assignments`

    `GET /api/v1/courses/:course_id/assignment_groups/:assignment_group_id/assignments`

    Returns the paginated list of assignments for the current course or assignment group.

    https://canvas.instructure.com/doc/api/assignments.html#method.assignments_api.index

    Returns:
        a list of Assignments
    """
    method = 'GET'
    if assignment_group_id is None:
        url = '/api/v1/courses/{course_id}/assignments'.format(course_id=course_id)
    else:
        url = '/api/v1/courses/{course_id}/assignment_groups/{assignment_group_id}/assignments'.format(
            course_id=course_id, assignment_group_id=assignment_group_id)
    query = [
        ('include', include),
        ('search_term', search_term),
        ('override_assignment_dates', override_assignment_dates),
        ('needs_grading_count_by_section', needs_grading_count_by_section),
        ('bucket', bucket),
        ('assignment_ids', assignment_ids),
        ('order_by', order_by),
        ('post_to_sis', post_to_sis),
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
        constructor=Assignment,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def list_assignments_for_user(
    session,
    base_url,
    user_id,
    course_id,
    include=None,
    search_term: Optional[str] = None,
    override_assignment_dates: Optional[bool] = None,
    needs_grading_count_by_section: Optional[bool] = None,
    bucket: Optional[Literal['past', 'overdue', 'undated', 'ungraded', 'unsubmitted', 'upcoming',
                             'future']] = None,
    assignment_ids=None,
    order_by: Optional[Literal['position', 'name', 'due_at']] = None,
    post_to_sis: Optional[bool] = None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List assignments for user

    `GET /api/v1/users/:user_id/courses/:course_id/assignments`

    Returns the paginated list of assignments for the specified user if the current user has rights to view. See List assignments for valid arguments.

    https://canvas.instructure.com/doc/api/assignments.html#method.assignments_api.user_index
    """
    method = 'GET'
    url = '/api/v1/users/{user_id}/courses/{course_id}/assignments'.format(user_id=user_id,
                                                                           course_id=course_id)
    query = [
        ('include', include),
        ('search_term', search_term),
        ('override_assignment_dates', override_assignment_dates),
        ('needs_grading_count_by_section', needs_grading_count_by_section),
        ('bucket', bucket),
        ('assignment_ids', assignment_ids),
        ('order_by', order_by),
        ('post_to_sis', post_to_sis),
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
        constructor=Assignment,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def duplicate_assignnment(
    session,
    base_url,
    course_id,
    assignment_id,
    result_type: Optional[Literal['Quiz']] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Duplicate assignnment

    `POST /api/v1/courses/:course_id/assignments/:assignment_id/duplicate`

    Duplicate an assignment and return a json based on result_type argument.

    https://canvas.instructure.com/doc/api/assignments.html#method.assignments_api.duplicate

    Returns:
        a Assignment
    """
    method = 'POST'
    url = '/api/v1/courses/{course_id}/assignments/{assignment_id}/duplicate'.format(
        course_id=course_id, assignment_id=assignment_id)
    query = [
        ('result_type', result_type),
    ]
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def get_a_single_assignment(
    session,
    base_url,
    course_id,
    id,
    include=None,
    override_assignment_dates: Optional[bool] = None,
    needs_grading_count_by_section: Optional[bool] = None,
    all_dates: Optional[bool] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get a single assignment

    `GET /api/v1/courses/:course_id/assignments/:id`

    Returns the assignment with the given id.

    https://canvas.instructure.com/doc/api/assignments.html#method.assignments_api.show

    Returns:
        a Assignment
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/assignments/{id}'.format(course_id=course_id, id=id)
    query = [
        ('include', include),
        ('override_assignment_dates', override_assignment_dates),
        ('needs_grading_count_by_section', needs_grading_count_by_section),
        ('all_dates', all_dates),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Assignment(data, session=session, base_url=base_url)


def create_an_assignment(
    session,
    base_url,
    course_id,
    assignment=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Create an assignment

    `POST /api/v1/courses/:course_id/assignments`

    Create a new assignment for this course. The assignment is created in the active state.

    https://canvas.instructure.com/doc/api/assignments.html#method.assignments_api.create

    Returns:
        a Assignment
    """
    method = 'POST'
    url = '/api/v1/courses/{course_id}/assignments'.format(course_id=course_id)
    query = [
        ('assignment', assignment),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Assignment(data, session=session, base_url=base_url)


def edit_an_assignment(
    session,
    base_url,
    course_id,
    id,
    assignment=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Edit an assignment

    `PUT /api/v1/courses/:course_id/assignments/:id`

    Modify an existing assignment.

    https://canvas.instructure.com/doc/api/assignments.html#method.assignments_api.update

    Returns:
        a Assignment
    """
    method = 'PUT'
    url = '/api/v1/courses/{course_id}/assignments/{id}'.format(course_id=course_id, id=id)
    query = [
        ('assignment', assignment),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Assignment(data, session=session, base_url=base_url)


def bulk_update_assignment_dates():
    """
    Bulk update assignment dates

    `PUT /api/v1/courses/:course_id/assignments/bulk_update`

    Update due dates and availability dates for multiple assignments in a course.

    Accepts a JSON array of objects containing two keys each: id, the assignment id, and all_dates, an array of AssignmentDate structures containing the base and/or override dates for the assignment, as returned from the List assignments endpoint with include[]=all_dates.

    This endpoint cannot create or destroy assignment overrides; any existing assignment overrides that are not referenced in the arguments will be left alone. If an override is given, any dates that are not supplied with it will be defaulted. To clear a date, specify null explicitly.

    All referenced assignments will be validated before any are saved. A list of errors will be returned if any provided dates are invalid, and no changes will be saved.

    The bulk update is performed in a background job, use the Progress API to check its status.

    https://canvas.instructure.com/doc/api/assignments.html#method.assignments_api.bulk_update

    Returns:
        a Progress
    """
    raise NotImplementedError


def list_assignment_overrides(
    session,
    base_url,
    course_id,
    assignment_id,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List assignment overrides

    `GET /api/v1/courses/:course_id/assignments/:assignment_id/overrides`

    Returns the paginated list of overrides for this assignment that target sections/groups/students visible to the current user.

    https://canvas.instructure.com/doc/api/assignments.html#method.assignment_overrides.index

    Returns:
        a list of AssignmentOverrides
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/assignments/{assignment_id}/overrides'.format(
        course_id=course_id, assignment_id=assignment_id)
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
        constructor=AssignmentOverride,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def get_a_single_assignment_override(
    session,
    base_url,
    course_id,
    assignment_id,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get a single assignment override

    `GET /api/v1/courses/:course_id/assignments/:assignment_id/overrides/:id`

    Returns details of the the override with the given id.

    https://canvas.instructure.com/doc/api/assignments.html#method.assignment_overrides.show

    Returns:
        a AssignmentOverride
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id}'.format(
        course_id=course_id, assignment_id=assignment_id, id=id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return AssignmentOverride(data, session=session, base_url=base_url)


def redirect_to_the_assignment_override_for_a_group(
    session,
    base_url,
    group_id,
    assignment_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Redirect to the assignment override for a group

    `GET /api/v1/groups/:group_id/assignments/:assignment_id/override`

    Responds with a redirect to the override for the given group, if any (404 otherwise).

    https://canvas.instructure.com/doc/api/assignments.html#method.assignment_overrides.group_alias
    """
    method = 'GET'
    url = '/api/v1/groups/{group_id}/assignments/{assignment_id}/override'.format(
        group_id=group_id, assignment_id=assignment_id)
    query = []
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def redirect_to_the_assignment_override_for_a_section(
    session,
    base_url,
    course_section_id,
    assignment_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Redirect to the assignment override for a section

    `GET /api/v1/sections/:course_section_id/assignments/:assignment_id/override`

    Responds with a redirect to the override for the given section, if any (404 otherwise).

    https://canvas.instructure.com/doc/api/assignments.html#method.assignment_overrides.section_alias
    """
    method = 'GET'
    url = '/api/v1/sections/{course_section_id}/assignments/{assignment_id}/override'.format(
        course_section_id=course_section_id, assignment_id=assignment_id)
    query = []
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def create_an_assignment_override(
    session,
    base_url,
    course_id,
    assignment_id,
    assignment_override=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Create an assignment override

    `POST /api/v1/courses/:course_id/assignments/:assignment_id/overrides`

    One of student_ids, group_id, or course_section_id must be present. At most one should be present; if multiple are present only the most specific (student_ids first, then group_id, then course_section_id) is used and any others are ignored.

    https://canvas.instructure.com/doc/api/assignments.html#method.assignment_overrides.create

    Returns:
        a AssignmentOverride
    """
    method = 'POST'
    url = '/api/v1/courses/{course_id}/assignments/{assignment_id}/overrides'.format(
        course_id=course_id, assignment_id=assignment_id)
    query = [
        ('assignment_override', assignment_override),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return AssignmentOverride(data, session=session, base_url=base_url)


def update_an_assignment_override(
    session,
    base_url,
    course_id,
    assignment_id,
    id,
    assignment_override=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Update an assignment override

    `PUT /api/v1/courses/:course_id/assignments/:assignment_id/overrides/:id`

    All current overridden values must be supplied if they are to be retained; e.g. if due_at was overridden, but this PUT omits a value for due_at, due_at will no longer be overridden. If the override is adhoc and student_ids is not supplied, the target override set is unchanged. Target override sets cannot be changed for group or section overrides.

    https://canvas.instructure.com/doc/api/assignments.html#method.assignment_overrides.update

    Returns:
        a AssignmentOverride
    """
    method = 'PUT'
    url = '/api/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id}'.format(
        course_id=course_id, assignment_id=assignment_id, id=id)
    query = [
        ('assignment_override', assignment_override),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return AssignmentOverride(data, session=session, base_url=base_url)


def delete_an_assignment_override(
    session,
    base_url,
    course_id,
    assignment_id,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Delete an assignment override

    `DELETE /api/v1/courses/:course_id/assignments/:assignment_id/overrides/:id`

    Deletes an override and returns its former details.

    https://canvas.instructure.com/doc/api/assignments.html#method.assignment_overrides.destroy

    Returns:
        a AssignmentOverride
    """
    method = 'DELETE'
    url = '/api/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id}'.format(
        course_id=course_id, assignment_id=assignment_id, id=id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return AssignmentOverride(data, session=session, base_url=base_url)


def batch_retrieve_overrides_in_a_course(
    session,
    base_url,
    course_id,
    assignment_overrides=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Batch retrieve overrides in a course

    `GET /api/v1/courses/:course_id/assignments/overrides`

    Returns a list of specified overrides in this course, providing they target sections/groups/students visible to the current user. Returns null elements in the list for requests that were not found.

    https://canvas.instructure.com/doc/api/assignments.html#method.assignment_overrides.batch_retrieve

    Returns:
        a list of AssignmentOverrides
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/assignments/overrides'.format(course_id=course_id)
    query = [
        ('assignment_overrides', assignment_overrides),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    data = [
        None if v is None else AssignmentOverride(v, session=session, base_url=base_url)
        for v in data
    ]
    return data


def batch_create_overrides_in_a_course(
    session,
    base_url,
    course_id,
    assignment_overrides=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Batch create overrides in a course

    `POST /api/v1/courses/:course_id/assignments/overrides`

    Creates the specified overrides for each assignment.  Handles creation in a transaction, so all records are created or none are.

    One of student_ids, group_id, or course_section_id must be present. At most one should be present; if multiple are present only the most specific (student_ids first, then group_id, then course_section_id) is used and any others are ignored.

    Errors are reported in an errors attribute, an array of errors corresponding to inputs.  Global errors will be reported as a single element errors array

    https://canvas.instructure.com/doc/api/assignments.html#method.assignment_overrides.batch_create

    Returns:
        a list of AssignmentOverrides
    """
    method = 'POST'
    url = '/api/v1/courses/{course_id}/assignments/overrides'.format(course_id=course_id)
    query = [
        ('assignment_overrides', assignment_overrides),
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


def batch_update_overrides_in_a_course(
    session,
    base_url,
    course_id,
    assignment_overrides=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Batch update overrides in a course

    `PUT /api/v1/courses/:course_id/assignments/overrides`

    Updates a list of specified overrides for each assignment.  Handles overrides in a transaction, so either all updates are applied or none. See Update an assignment override for available attributes.

    All current overridden values must be supplied if they are to be retained; e.g. if due_at was overridden, but this PUT omits a value for due_at, due_at will no longer be overridden. If the override is adhoc and student_ids is not supplied, the target override set is unchanged. Target override sets cannot be changed for group or section overrides.

    Errors are reported in an errors attribute, an array of errors corresponding to inputs.  Global errors will be reported as a single element errors array

    https://canvas.instructure.com/doc/api/assignments.html#method.assignment_overrides.batch_update

    Returns:
        a list of AssignmentOverrides
    """
    method = 'PUT'
    url = '/api/v1/courses/{course_id}/assignments/overrides'.format(course_id=course_id)
    query = [
        ('assignment_overrides', assignment_overrides),
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


class Course(objects.Base):
    """
    https://canvas.instructure.com/doc/api/courses.html#Course
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('id', 'name')

    @property
    def id(self):
        """the unique identifier for the course"""
        return self.getattr('id')

    @property
    def sis_course_id(self):
        """
        the SIS identifier for the course, if defined. This field is only included if
        the user has permission to view SIS information.
        """
        return self.getattr('sis_course_id')

    @property
    def uuid(self):
        """the UUID of the course"""
        return self.getattr('uuid')

    @property
    def integration_id(self):
        """
        the integration identifier for the course, if defined. This field is only
        included if the user has permission to view SIS information.
        """
        return self.getattr('integration_id')

    @property
    def sis_import_id(self):
        """
        the unique identifier for the SIS import. This field is only included if the
        user has permission to manage SIS information.
        """
        return self.getattr('sis_import_id')

    @property
    def name(self):
        """the full name of the course"""
        return self.getattr('name')

    @property
    def course_code(self):
        """the course code"""
        return self.getattr('course_code')

    @property
    def workflow_state(self):
        """
        the current state of the course one of 'unpublished', 'available',
        'completed', or 'deleted'
        """
        return self.getattr('workflow_state')

    @property
    def account_id(self):
        """the account associated with the course"""
        return self.getattr('account_id')

    @property
    def root_account_id(self):
        """the root account associated with the course"""
        return self.getattr('root_account_id')

    @property
    def enrollment_term_id(self):
        """the enrollment term associated with the course"""
        return self.getattr('enrollment_term_id')

    @property
    def grading_periods(self):
        """A list of grading periods associated with the course"""
        return self.getattr('grading_periods')

    @property
    def grading_standard_id(self):
        """the grading standard associated with the course"""
        return self.getattr('grading_standard_id')

    @property
    def grade_passback_setting(self):
        """the grade_passback_setting set on the course"""
        return self.getattr('grade_passback_setting')

    @property
    def created_at(self):
        """the date the course was created."""
        return self.getattr('created_at')

    @property
    def start_at(self):
        """the start date for the course, if applicable"""
        return self.getattr('start_at')

    @property
    def end_at(self):
        """the end date for the course, if applicable"""
        return self.getattr('end_at')

    @property
    def locale(self):
        """the course-set locale, if applicable"""
        return self.getattr('locale')

    @property
    def enrollments(self):
        """
        A list of enrollments linking the current user to the course. For student
        enrollments, grading information may be included if include[]=total_scores
        """
        return self.getattr('enrollments')

    @property
    def total_students(self):
        """optional: the total number of active and invited students in the course"""
        return self.getattr('total_students')

    @property
    def calendar(self):
        """course calendar"""
        return self.getattr('calendar')

    @property
    def default_view(self):
        """
        the type of page that users will see when they first visit the course -
        'feed': Recent Activity Dashboard - 'wiki': Wiki Front Page - 'modules':
        Course Modules/Sections Page - 'assignments': Course Assignments List -
        'syllabus': Course Syllabus Page other types may be added in the future
        """
        return self.getattr('default_view')

    @property
    def syllabus_body(self):
        """optional: user-generated HTML for the course syllabus"""
        return self.getattr('syllabus_body')

    @property
    def needs_grading_count(self):
        """
        optional: the number of submissions needing grading returned only if the
        current user has grading rights and include[]=needs_grading_count
        """
        return self.getattr('needs_grading_count')

    @property
    def term(self):
        """
        optional: the enrollment term object for the course returned only if
        include[]=term
        """
        return self.getattr('term')

    @property
    def course_progress(self):
        """
        optional: information on progress through the course returned only if
        include[]=course_progress
        """
        return self.getattr('course_progress')

    @property
    def apply_assignment_group_weights(self):
        """weight final grade based on assignment group percentages"""
        return self.getattr('apply_assignment_group_weights')

    @property
    def permissions(self):
        """
        optional: the permissions the user has for the course. returned only for a
        single course and include[]=permissions
        """
        return self.getattr('permissions')

    @property
    def is_public(self):
        return self.getattr('is_public')

    @property
    def is_public_to_auth_users(self):
        return self.getattr('is_public_to_auth_users')

    @property
    def public_syllabus(self):
        return self.getattr('public_syllabus')

    @property
    def public_syllabus_to_auth(self):
        return self.getattr('public_syllabus_to_auth')

    @property
    def public_description(self):
        """optional: the public description of the course"""
        return self.getattr('public_description')

    @property
    def storage_quota_mb(self):
        return self.getattr('storage_quota_mb')

    @property
    def storage_quota_used_mb(self):
        return self.getattr('storage_quota_used_mb')

    @property
    def hide_final_grades(self):
        return self.getattr('hide_final_grades')

    @property
    def license(self):
        return self.getattr('license')

    @property
    def allow_student_assignment_edits(self):
        return self.getattr('allow_student_assignment_edits')

    @property
    def allow_wiki_comments(self):
        return self.getattr('allow_wiki_comments')

    @property
    def allow_student_forum_attachments(self):
        return self.getattr('allow_student_forum_attachments')

    @property
    def open_enrollment(self):
        return self.getattr('open_enrollment')

    @property
    def self_enrollment(self):
        return self.getattr('self_enrollment')

    @property
    def restrict_enrollments_to_course_dates(self):
        return self.getattr('restrict_enrollments_to_course_dates')

    @property
    def course_format(self):
        return self.getattr('course_format')

    @property
    def access_restricted_by_date(self):
        """
        optional: this will be true if this user is currently prevented from viewing
        the course because of date restriction settings
        """
        return self.getattr('access_restricted_by_date')

    @property
    def time_zone(self):
        """The course's IANA time zone name."""
        return self.getattr('time_zone')

    @property
    def blueprint(self):
        """
        optional: whether the course is set as a Blueprint Course (blueprint fields
        require the Blueprint Courses feature)
        """
        return self.getattr('blueprint')

    @property
    def blueprint_restrictions(self):
        """optional: Set of restrictions applied to all locked course objects"""
        return self.getattr('blueprint_restrictions')

    @property
    def blueprint_restrictions_by_object_type(self):
        """
        optional: Sets of restrictions differentiated by object type applied to
        locked course objects
        """
        return self.getattr('blueprint_restrictions_by_object_type')

    @property
    def template(self):
        """
        optional: whether the course is set as a template (requires the Course
        Templates feature)
        """
        return self.getattr('template')

    @property
    def overridden_course_visibility(self):
        return self.getattr('overridden_course_visibility')

    @property
    def sections(self):
        """
        "sections": Section enrollment information to include with each Course. Returns an
        array of hashes containing the section ID (id), section name (name), start and end
        dates (start_at, end_at), as well as the enrollment type (enrollment_role, e.g.
        'StudentEnrollment').

        https://canvas.instructure.com/doc/api/courses.html#method.courses.index
        """
        return self.getattr('sections')

    @property
    def passback_status(self):
        """
        "passback_status": Include the grade passback_status

        https://canvas.instructure.com/doc/api/courses.html#method.courses.index
        """
        return self.getattr('passback_status')

    @property
    def has_grading_periods(self):
        """include[]=current_grading_period_scores"""
        return self.getattr('has_grading_periods')

    @property
    def multiple_grading_periods_enabled(self):
        """include[]=current_grading_period_scores"""
        return self.getattr('multiple_grading_periods_enabled')

    @property
    def has_weighted_grading_periods(self):
        """include[]=current_grading_period_scores"""
        return self.getattr('has_weighted_grading_periods')

    @property
    def account(self):
        """
        "account": Optional information to include with each Course. When account is given,
        the account json for each course is returned.

        https://canvas.instructure.com/doc/api/courses.html#method.courses.index
        """
        return self.getattr('account')

    @property
    def is_favorite(self):
        """
        "favorites": Optional information to include with each Course. Indicates if the user has
        marked the course as a favorite course.

        https://canvas.instructure.com/doc/api/courses.html#method.courses.index
        """
        return self.getattr('is_favorite')

    @property
    def teachers(self):
        """
        "teachers": Teacher information to include with each Course. Returns an array of
        hashes containing the UserDisplay information for each teacher in the course.

        https://canvas.instructure.com/doc/api/courses.html#method.courses.index
        """
        return self.getattr('teachers')

    @property
    def image_download_url(self):
        """
        "course_image": Optional course image data for when there is a course image and the
        course image feature flag has been enabled

        https://canvas.instructure.com/doc/api/courses.html#method.courses.index
        """
        return self.getattr('image_download_url')

    @property
    def concluded(self):
        """
        "concluded": Optional information to include with each Course. Indicates whether the
        course has been concluded, taking course and term dates into account.

        https://canvas.instructure.com/doc/api/courses.html#method.courses.index
        """
        return self.getattr('concluded')

    @property
    def tabs(self):
        """
        "tabs": Optional information to include with each Course. Will include the list of tabs
        configured for each course. See the List available tabs API for more information.

        https://canvas.instructure.com/doc/api/courses.html#method.courses.index
        """
        return self.getattr('tabs')

    @property
    def html_url(self):
        return self.getattr('html_url')

    @property
    def group_weighting_scheme(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('group_weighting_scheme')

    @property
    def conclude_at(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('conclude_at')

    @property
    def allow_student_wiki_edits(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('allow_student_wiki_edits')

    @property
    def updated_at(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('updated_at')

    @property
    def show_public_context_messages(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('show_public_context_messages')

    @property
    def default_wiki_editing_roles(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('default_wiki_editing_roles')

    @property
    def wiki_id(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('wiki_id')

    @property
    def allow_student_organized_groups(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('allow_student_organized_groups')

    @property
    def abstract_course_id(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('abstract_course_id')

    @property
    def sis_source_id(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('sis_source_id')

    @property
    def sis_batch_id(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('sis_batch_id')

    @property
    def storage_quota(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('storage_quota')

    @property
    def tab_configuration(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('tab_configuration')

    @property
    def turnitin_comments(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('turnitin_comments')

    @property
    def indexed(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('indexed')

    @property
    def template_course_id(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('template_course_id')

    @property
    def settings(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('settings')

    @property
    def replacement_course_id(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('replacement_course_id')

    @property
    def stuck_sis_fields(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('stuck_sis_fields')

    @property
    def self_enrollment_code(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('self_enrollment_code')

    @property
    def self_enrollment_limit(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('self_enrollment_limit')

    @property
    def lti_context_id(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('lti_context_id')

    @property
    def turnitin_id(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('turnitin_id')

    @property
    def show_announcements_on_home_page(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('show_announcements_on_home_page')

    @property
    def home_page_announcement_limit(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('home_page_announcement_limit')

    @property
    def latest_outcome_import_id(self):
        """
        https://canvas.instructure.com/doc/api/search.html#method.search.all_courses
        """
        return self.getattr('latest_outcome_import_id')


def list_your_courses(
    session,
    base_url,
    enrollment_type: Literal['teacher', 'student', 'ta', 'observer', 'designer'] = None,
    enrollment_role: str = None,
    enrollment_role_id: int = None,
    enrollment_state: Literal['active', 'invited_or_pending', 'completed'] = None,
    exclude_blueprint_courses: bool = None,
    include=None,
    state=None,
    per_page: int = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List your courses

    `GET /api/v1/courses`

    Returns the paginated list of active courses for the current user.

    https://canvas.instructure.com/doc/api/courses.html#method.courses.index

    Returns:
        a list of Courses
    """
    method = 'GET'
    url = '/api/v1/courses'
    query = [
        ('enrollment_type', enrollment_type),
        ('enrollment_role', enrollment_role),
        ('enrollment_role_id', enrollment_role_id),
        ('enrollment_state', enrollment_state),
        ('exclude_blueprint_courses', exclude_blueprint_courses),
        ('include', include),
        ('state', state),
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
        constructor=Course,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def list_courses_for_a_user(
    session,
    base_url,
    user_id,
    include=None,
    state=None,
    enrollment_state: Literal['active', 'invited_or_pending', 'completed'] = None,
    homeroom: bool = None,
    per_page: int = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List courses for a user

    `GET /api/v1/users/:user_id/courses`

    Returns a paginated list of active courses for this user. To view the course list for a user other than yourself, you must be either an observer of that user or an administrator.

    https://canvas.instructure.com/doc/api/courses.html#method.courses.user_index

    Returns:
        a list of Courses
    """
    method = 'GET'
    url = '/api/v1/users/{user_id}/courses'.format(user_id=user_id)
    query = [
        ('include', include),
        ('state', state),
        ('enrollment_state', enrollment_state),
        ('homeroom', homeroom),
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
        constructor=Course,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def get_user_progress(
    session,
    base_url,
    course_id,
    user_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get user progress

    `GET /api/v1/courses/:course_id/users/:user_id/progress`

    Return progress information for the user and course

    You can supply self as the user_id to query your own progress in a course. To query another user's progress, you must be a teacher in the course, an administrator, or a linked observer of the user.

    https://canvas.instructure.com/doc/api/courses.html#method.courses.user_progress

    NTU COOL does not seem to support this resource.

    Returns:
        a CourseProgress
    """
    raise NotImplementedError
    method = 'GET'
    url = '/api/v1/courses/{course_id}/users/{user_id}/progress'.format(course_id=course_id,
                                                                        user_id=user_id)
    query = []
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def list_students(
    session,
    base_url,
    course_id,
    per_page: int = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List students

    `GET /api/v1/courses/:course_id/students`

    Returns the paginated list of students enrolled in this course.

    DEPRECATED: Please use the course users endpoint and pass "student" as the enrollment_type.

    https://canvas.instructure.com/doc/api/courses.html#method.courses.students

    NTU COOL does not seem to support pagination.

    Returns:
        a list of Users
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/students'.format(course_id=course_id)
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
        constructor=User,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def list_users_in_course(
    session,
    base_url,
    course_id,
    scope: Literal['users', 'search_users'] = 'users',
    search_term: str = None,
    sort: Literal['username', 'last_login', 'email', 'sis_id'] = None,
    enrollment_type=None,
    enrollment_role: str = None,
    enrollment_role_id: int = None,
    include=None,
    user_id: str = None,
    user_ids=None,
    enrollment_state=None,
    per_page: int = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List users in course

    `GET /api/v1/courses/:course_id/users`

    `GET /api/v1/courses/:course_id/search_users`

    Returns the paginated list of users in this course. And optionally the user's enrollments in the course.

    https://canvas.instructure.com/doc/api/courses.html#method.courses.users

    NTU COOL sort=last_login
    {'errors': [{'message': 'An error occurred.', 'error_code': 'internal_server_error'}], 'error_report_id': error_report_id}

    Returns:
        a list of Users
    """
    if scope not in ('users', 'search_users'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/courses/{course_id}/{scope}'.format(course_id=course_id, scope=scope)
    query = [
        ('search_term', search_term),
        ('sort', sort),
        ('enrollment_type', enrollment_type),
        ('enrollment_role', enrollment_role),
        ('enrollment_role_id', enrollment_role_id),
        ('include', include),
        ('user_id', user_id),
        ('user_ids', user_ids),
        ('enrollment_state', enrollment_state),
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
        constructor=User,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def list_recently_logged_in_students(
    session,
    base_url,
    course_id,
    per_page: int = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List recently logged in students

    `GET /api/v1/courses/:course_id/recent_students`

    Returns the paginated list of users in this course, ordered by how recently they have logged in. The records include the 'last_login' field which contains a timestamp of the last time that user logged into canvas. The querying user must have the 'View usage reports' permission.

    https://canvas.instructure.com/doc/api/courses.html#method.courses.recent_students

    Returns:
        a list of Users
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/recent_students'.format(course_id=course_id)
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
        constructor=User,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def get_single_user(
    session,
    base_url,
    course_id,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get single user

    `GET /api/v1/courses/:course_id/users/:id`

    Return information on a single user.

    Accepts the same include[] parameters as the :users: action, and returns a single user with the same fields as that action.

    https://canvas.instructure.com/doc/api/courses.html#method.courses.user

    Returns:
        a User
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/users/{id}'.format(course_id=course_id, id=id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return User(data, session=session, base_url=base_url)


def search_for_content_share_users(
    session,
    base_url,
    course_id,
    search_term: str,
    per_page: int = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    Search for content share users

    `GET /api/v1/courses/:course_id/content_share_users`

    Returns a paginated list of users you can share content with. Requires the content share feature and the user must have the manage content permission for the course.

    https://canvas.instructure.com/doc/api/courses.html#method.courses.content_share_users

    Returns:
        a list of Users
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/content_share_users'.format(course_id=course_id)
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
        constructor=User,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def preview_processed_html(
    session,
    base_url,
    course_id,
    html: str = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Preview processed html

    `POST /api/v1/courses/:course_id/preview_html`

    Preview html content processed for this course

    https://canvas.instructure.com/doc/api/courses.html#method.courses.preview_html
    """
    method = 'POST'
    url = '/api/v1/courses/{course_id}/preview_html'.format(course_id=course_id)
    query = [
        ('html', html),
    ]
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def course_activity_stream(
    session,
    base_url,
    course_id,
    per_page: int = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    Course activity stream

    `GET /api/v1/courses/:course_id/activity_stream`

    Returns the current user's course-specific activity stream, paginated.

    For full documentation, see the API documentation for the user activity stream, in the user api.

    https://canvas.instructure.com/doc/api/courses.html#method.courses.activity_stream
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/activity_stream'.format(course_id=course_id)
    query = [
        ('page', page),
        ('per_page', per_page),
    ]
    return paginations.request_json_paginated(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        pagination=pagination,
        raise_for_error=raise_for_error,
    )


def course_activity_stream_summary(
    session,
    base_url,
    course_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Course activity stream summary

    `GET /api/v1/courses/:course_id/activity_stream/summary`

    Returns a summary of the current user's course-specific activity stream.

    For full documentation, see the API documentation for the user activity stream summary, in the user api.

    https://canvas.instructure.com/doc/api/courses.html#method.courses.activity_stream_summary
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/activity_stream/summary'.format(course_id=course_id)
    query = []
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def course_todo_items(
    session,
    base_url,
    course_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Course TODO items

    `GET /api/v1/courses/:course_id/todo`

    Returns the current user's course-specific todo items.

    For full documentation, see the API documentation for the user todo items, in the user api.

    https://canvas.instructure.com/doc/api/courses.html#method.courses.todo_items

    NTU COOL seems to support pagination.
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/todo'.format(course_id=course_id)
    query = []
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def get_course_settings(
    session,
    base_url,
    course_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get course settings

    `GET /api/v1/courses/:course_id/settings`

    Returns some of a course's settings.

    https://canvas.instructure.com/doc/api/courses.html#method.courses.api_settings
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/settings'.format(course_id=course_id)
    query = []
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def get_a_single_course(
    session,
    base_url,
    id,
    account_id=None,
    include=None,
    teacher_limit: int = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get a single course

    `GET /api/v1/courses/:id`

    `GET /api/v1/accounts/:account_id/courses/:id`

    Return information on a single course.

    Accepts the same include[] parameters as the list action plus:

    https://canvas.instructure.com/doc/api/courses.html#method.courses.show

    Returns:
        a Course
    """
    method = 'GET'
    if account_id is None:
        url = '/api/v1/courses/{id}'.format(id=id)
    else:
        url = '/api/v1/accounts/{account_id}/courses/{id}'.format(account_id=account_id, id=id)
    query = [
        ('include', include),
        ('teacher_limit', teacher_limit),
    ]
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return Course(data, session=session, base_url=base_url)


def get_effective_due_dates(
    session,
    base_url,
    course_id,
    assignment_ids=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get effective due dates

    `GET /api/v1/courses/:course_id/effective_due_dates`

    For each assignment in the course, returns each assigned student's ID and their corresponding due date along with some grading period data. Returns a collection with keys representing assignment IDs and values as a collection containing keys representing student IDs and values representing the student's effective due_at, the grading_period_id of which the due_at falls in, and whether or not the grading period is closed (in_closed_grading_period)

    The list of assignment IDs for which effective student due dates are requested. If not provided, all assignments in the course will be used.

    https://canvas.instructure.com/doc/api/courses.html#method.courses.effective_due_dates
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/effective_due_dates'.format(course_id=course_id)
    query = [
        (assignment_ids, assignment_ids),
    ]
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def permissions(
    session,
    base_url,
    course_id,
    permissions=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Permissions

    `GET /api/v1/courses/:course_id/permissions`

    Returns permission information for the calling user in the given course. See also the Account and Group counterparts.
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/permissions'.format(course_id=course_id)
    query = [
        ('permissions', permissions),
    ]
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def get_course_copy_status(
    session,
    base_url,
    course_id,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get course copy status

    `GET /api/v1/courses/:course_id/course_copy/:id`

    DEPRECATED: Please use the Content Migrations API

    Retrieve the status of a course copy

    API response field:
        id:
            The unique identifier for the course copy.
        created_at:
            The time that the copy was initiated.
        progress:
            The progress of the copy as an integer. It is null before the copying starts, and 100 when finished.
        workflow_state:
            The current status of the course copy. Possible values: "created", "started", "completed", "failed"
        status_url:
            The url for the course copy status API endpoint.

    https://canvas.instructure.com/doc/api/courses.html#method.content_imports.copy_course_status
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/course_copy/{id}'.format(course_id=course_id, id=id)
    query = []
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


class MediaComment(objects.Base):
    """
    https://canvas.instructure.com/doc/api/submissions.html#MediaComment
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('media_id', 'display_name')

    @property
    def content_type(self):
        return self.getattr('content-type')

    @property
    def display_name(self):
        return self.getattr('display_name')

    @property
    def media_id(self):
        return self.getattr('media_id')

    @property
    def media_type(self):
        return self.getattr('media_type')

    @property
    def url(self):
        return self.getattr('url')


class SubmissionComment(objects.Base):
    """
    https://canvas.instructure.com/doc/api/submissions.html#SubmissionComment
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('id', 'author_id', 'author_name')

    @property
    def id(self):
        return self.getattr('id')

    @property
    def author_id(self):
        return self.getattr('author_id')

    @property
    def author_name(self):
        return self.getattr('author_name')

    @property
    def author(self) -> 'UserDisplay':
        """Abbreviated user object UserDisplay (see users API)."""
        constructor_kwargs = {'session': self.session, 'base_url': self.base_url}
        return self.getattr('author',
                            constructor=UserDisplay,
                            constructor_kwargs=constructor_kwargs)

    @property
    def comment(self):
        return self.getattr('comment')

    @property
    def created_at(self):
        return self.getattr('created_at')

    @property
    def edited_at(self):
        return self.getattr('edited_at')

    @property
    def media_comment(self):
        return self.getattr('media_comment')


class Submission(objects.Base):
    """
    https://canvas.instructure.com/doc/api/submissions.html#Submission
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('id', 'assignment_id', 'attempt', 'submission_type', 'preview_url')

    @property
    def assignment_id(self):
        """The submission's assignment id"""
        return self.getattr('assignment_id')

    @property
    def assignment(self) -> Assignment:
        """The submission's assignment (see the assignments API) (optional)"""
        constructor_kwargs = {'session': self.session, 'base_url': self.base_url}
        return self.getattr('assignment',
                            constructor=Assignment,
                            constructor_kwargs=constructor_kwargs)

    @property
    def course(self) -> Course:
        """The submission's course (see the course API) (optional)"""
        constructor_kwargs = {'session': self.session, 'base_url': self.base_url}
        return self.getattr('course', constructor=Course, constructor_kwargs=constructor_kwargs)

    @property
    def attempt(self):
        """This is the submission attempt number."""
        return self.getattr('attempt')

    @property
    def body(self):
        """The content of the submission, if it was submitted directly in a text field."""
        return self.getattr('body')

    @property
    def grade(self):
        """
        The grade for the submission, translated into the assignment grading scheme
        (so a letter grade, for example).
        """
        return self.getattr('grade')

    @property
    def grade_matches_current_submission(self):
        """
        A boolean flag which is false if the student has re-submitted since the
        submission was last graded.
        """
        return self.getattr('grade_matches_current_submission')

    @property
    def html_url(self):
        """URL to the submission. This will require the user to log in."""
        return self.getattr('html_url')

    @property
    def preview_url(self):
        """URL to the submission preview. This will require the user to log in."""
        return self.getattr('preview_url')

    @property
    def score(self):
        """The raw score"""
        return self.getattr('score')

    @property
    def submission_comments(self):
        """Associated comments for a submission (optional)"""
        return self.getattr('submission_comments')

    @property
    def submission_type(self):
        """
        The types of submission ex:
        ('online_text_entry'|'online_url'|'online_upload'|'media_recording'|'student_annotation')
        """
        return self.getattr('submission_type')

    @property
    def submitted_at(self):
        """The timestamp when the assignment was submitted"""
        return self.getattr('submitted_at')

    @property
    def url(self):
        """The URL of the submission (for 'online_url' submissions)."""
        return self.getattr('url')

    @property
    def user_id(self):
        """The id of the user who created the submission"""
        return self.getattr('user_id')

    @property
    def grader_id(self):
        """
        The id of the user who graded the submission. This will be null for
        submissions that haven't been graded yet. It will be a positive number if a
        real user has graded the submission and a negative number if the submission
        was graded by a process (e.g. Quiz autograder and autograding LTI tools).
        Specifically autograded quizzes set grader_id to the negative of the quiz id.
        Submissions autograded by LTI tools set grader_id to the negative of the tool
        id.
        """
        return self.getattr('grader_id')

    @property
    def graded_at(self):
        return self.getattr('graded_at')

    @property
    def user(self) -> 'User':
        """The submissions user (see user API) (optional)"""
        constructor_kwargs = {'session': self.session, 'base_url': self.base_url}
        return self.getattr('user', constructor=User, constructor_kwargs=constructor_kwargs)

    @property
    def late(self):
        """Whether the submission was made after the applicable due date"""
        return self.getattr('late')

    @property
    def assignment_visible(self):
        """
        Whether the assignment is visible to the user who submitted the assignment.
        Submissions where `assignment_visible` is false no longer count towards the
        student's grade and the assignment can no longer be accessed by the student.
        `assignment_visible` becomes false for submissions that do not have a grade
        and whose assignment is no longer assigned to the student's section.
        """
        return self.getattr('assignment_visible')

    @property
    def excused(self):
        """
        Whether the assignment is excused.  Excused assignments have no impact on a
        user's grade.
        """
        return self.getattr('excused')

    @property
    def missing(self):
        """Whether the assignment is missing."""
        return self.getattr('missing')

    @property
    def late_policy_status(self):
        """
        The status of the submission in relation to the late policy. Can be late,
        missing, none, or null.
        """
        return self.getattr('late_policy_status')

    @property
    def points_deducted(self):
        """
        The amount of points automatically deducted from the score by the
        missing/late policy for a late or missing assignment.
        """
        return self.getattr('points_deducted')

    @property
    def seconds_late(self):
        """The amount of time, in seconds, that an submission is late by."""
        return self.getattr('seconds_late')

    @property
    def workflow_state(self):
        """The current state of the submission"""
        return self.getattr('workflow_state')

    @property
    def extra_attempts(self):
        """Extra submission attempts allowed for the given user and assignment."""
        return self.getattr('extra_attempts')

    @property
    def anonymous_id(self):
        """
        A unique short ID identifying this submission without reference to the owning
        user. Only included if the caller has administrator access for the current
        account.
        """
        return self.getattr('anonymous_id')

    @property
    def posted_at(self):
        """
        The date this submission was posted to the student, or nil if it has not been
        posted.
        """
        return self.getattr('posted_at')

    @property
    def read_status(self):
        """
        The read status of this submission for the given user (optional). Including
        read_status will mark submission(s) as read.
        """
        return self.getattr('read_status')

    @property
    def id(self):
        """
        This property is unclear. It may be the id of the submission or the quiz submission.
        """
        return self.getattr('id')

    @property
    def cached_due_date(self):
        return self.getattr('cached_due_date')

    @property
    def grading_period_id(self):
        return self.getattr('grading_period_id')

    @property
    def entered_grade(self):
        return self.getattr('entered_grade')

    @property
    def entered_score(self):
        return self.getattr('entered_score')

    @property
    def attachments(self):
        return self.getattr('attachments')

    @property
    def submission_history(self) -> list['Submission']:
        constructor_kwargs = {'session': self.session, 'base_url': self.base_url}
        return self.getattr('submission_history',
                            constructor=Submission,
                            constructor_kwargs=constructor_kwargs,
                            type='list')

    @property
    def group(self):
        """
        "group" will add group_id and group_name.

        https://canvas.instructure.com/doc/api/submissions.html#method.submissions_api.index
        """
        return self.getattr('group')

    @property
    def has_postable_comments(self):
        return self.getattr('has_postable_comments')

    @property
    def submission_data(self):
        return self.getattr('submission_data')


class SubmissionsGroupedByStudent(objects.Base):

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('user_id', 'section_id')

    @property
    def user_id(self):
        return self.getattr('user_id')

    @property
    def submissions(self) -> list[Submission]:
        constructor_kwargs = {'session': self.session, 'base_url': self.base_url}
        return self.getattr('submissions',
                            constructor=Submission,
                            constructor_kwargs=constructor_kwargs,
                            type='list')

    @property
    def computed_final_score(self):
        """
        `total_scores` requires the `grouped` argument.

        https://canvas.instructure.com/doc/api/submissions.html#method.submissions_api.for_students
        """
        return self.getattr('computed_final_score')

    @property
    def computed_current_score(self):
        """
        `total_scores` requires the `grouped` argument.

        https://canvas.instructure.com/doc/api/submissions.html#method.submissions_api.for_students
        """
        return self.getattr('computed_current_score')

    @property
    def section_id(self):
        return self.getattr('section_id')


def construct_submission_or_submissions_grouped_by_student(value, **kwargs):
    if 'submissions' in value:
        return SubmissionsGroupedByStudent(value, **kwargs)
    else:
        return Submission(value, **kwargs)


def submit_an_assignment():
    """
    Submit an assignment

    `POST /api/v1/courses/:course_id/assignments/:assignment_id/submissions`

    `POST /api/v1/sections/:section_id/assignments/:assignment_id/submissions`

    Make a submission for an assignment. You must be enrolled as a student in the course/section to do this.

    All online turn-in submission types are supported in this API. However, there are a few things that are not yet supported:

    https://canvas.instructure.com/doc/api/submissions.html#method.submissions.create
    """


def list_assignment_submissions(
    session,
    base_url,
    context: Literal['courses', 'sections'],
    context_id,
    assignment_id,
    include=None,
    grouped: Optional[bool] = None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List assignment submissions

    `GET /api/v1/courses/:course_id/assignments/:assignment_id/submissions`

    `GET /api/v1/sections/:section_id/assignments/:assignment_id/submissions`

    A paginated list of all existing submissions for an assignment.

    https://canvas.instructure.com/doc/api/submissions.html#method.submissions_api.index

    Returns:
        a list of Submissions
    """
    if context not in ('courses', 'sections'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/assignments/{assignment_id}/submissions'.format(
        context=context, context_id=context_id, assignment_id=assignment_id)
    query = [
        ('include', include),
        ('grouped', grouped),
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
        constructor=construct_submission_or_submissions_grouped_by_student,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def list_submissions_for_multiple_assignments(
    session,
    base_url,
    context: Literal['courses', 'sections'],
    context_id,
    student_ids=None,
    assignment_ids=None,
    grouped: Optional[bool] = None,
    post_to_sis: Optional[bool] = None,
    submitted_since=None,
    graded_since=None,
    grading_period_id: Optional[int] = None,
    workflow_state: Optional[Literal['submitted', 'unsubmitted', 'graded',
                                     'pending_review']] = None,
    enrollment_state: Optional[Literal['active', 'concluded']] = None,
    state_based_on_date: Optional[bool] = None,
    order: Optional[Literal['id', 'graded_at']] = None,
    order_direction: Optional[Literal['ascending', 'descending']] = None,
    include=None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List submissions for multiple assignments

    `GET /api/v1/courses/:course_id/students/submissions`

    `GET /api/v1/sections/:section_id/students/submissions`

    A paginated list of all existing submissions for a given set of students and assignments.

    Args:
        grouped: If this argument is present (including grouped=false), the response will be grouped by student, rather than a flat array of submissions.

    https://canvas.instructure.com/doc/api/submissions.html#method.submissions_api.for_students
    """
    if context not in ('courses', 'sections'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/students/submissions'.format(context=context,
                                                                       context_id=context_id)
    query = [
        ('student_ids', student_ids),
        ('assignment_ids', assignment_ids),
        ('grouped', grouped),
        ('post_to_sis', post_to_sis),
        ('submitted_since', submitted_since),
        ('graded_since', graded_since),
        ('grading_period_id', grading_period_id),
        ('workflow_state', workflow_state),
        ('enrollment_state', enrollment_state),
        ('state_based_on_date', state_based_on_date),
        ('order', order),
        ('order_direction', order_direction),
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
        constructor=construct_submission_or_submissions_grouped_by_student,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def get_a_single_submission(
    session,
    base_url,
    context: Literal['courses', 'sections'],
    context_id,
    assignment_id,
    user_id,
    include=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get a single submission

    `GET /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id`

    `GET /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id`

    Get a single submission, based on user id.

    https://canvas.instructure.com/doc/api/submissions.html#method.submissions_api.show
    """
    if context not in ('courses', 'sections'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/assignments/{assignment_id}/submissions/{user_id}'.format(
        context=context, context_id=context_id, assignment_id=assignment_id, user_id=user_id)
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
    return Submission(data, session=session, base_url=base_url)


def upload_file_to_submission(
    session,
    base_url,
    context: Literal['courses', 'sections'],
    context_id,
    assignment_id,
    user_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Upload a file

    `POST /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/files`

    `POST /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/files`

    Upload a file to a submission.

    This API endpoint is the first step in uploading a file to a submission as a student. See the File Upload Documentation for details on the file upload workflow.

    The final step of the file upload workflow will return the attachment data, including the new file id. The caller can then POST to submit the online_upload assignment with these file ids.

    https://canvas.instructure.com/doc/api/submissions.html#method.submissions_api.create_file
    """
    if context not in ('courses', 'sections'):
        raise ValueError
    method = 'POST'
    url = ('/api/v1/{context}/{context_id}/assignments/{assignment_id}/submissions/{user_id}/files'.
           format(context=context,
                  context_id=context_id,
                  assignment_id=assignment_id,
                  user_id=user_id))
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


def grade_or_comment_on_a_submission(
    session,
    base_url,
    context: Literal['courses', 'sections'],
    context_id,
    assignment_id,
    user_id,
    comment=None,
    include=None,
    submission=None,
    rubric_assessment=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Grade or comment on a submission

    `PUT /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id`

    `PUT /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id`

    Comment on and/or update the grading for a student's assignment submission. If any submission or rubric_assessment arguments are provided, the user must have permission to manage grades in the appropriate context (course or section).

    https://canvas.instructure.com/doc/api/submissions.html#method.submissions_api.update
    """
    if context not in ('courses', 'sections'):
        raise ValueError
    method = 'PUT'
    url = '/api/v1/{context}/{context_id}/assignments/{assignment_id}/submissions/{user_id}'.format(
        context=context, context_id=context_id, assignment_id=assignment_id, user_id=user_id)
    query = [
        ('comment', comment),
        ('include', include),
        ('submission', submission),
        ('rubric_assessment', rubric_assessment),
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


def list_gradeable_students(
    session,
    base_url,
    course_id,
    assignment_id,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List gradeable students

    `GET /api/v1/courses/:course_id/assignments/:assignment_id/gradeable_students`

    A paginated list of students eligible to submit the assignment. The caller must have permission to view grades.

    If anonymous grading is enabled for the current assignment and the allow_new_anonymous_id parameter is passed, the returned data will not include any values identifying the student, but will instead include an assignment-specific anonymous ID for each student.

    Section-limited instructors will only see students in their own sections.

    https://canvas.instructure.com/doc/api/submissions.html#method.submissions_api.gradeable_students

    Returns:
        a list of UserDisplays
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/assignments/{assignment_id}/gradeable_students'.format(
        course_id=course_id, assignment_id=assignment_id)
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
        constructor=UserDisplay,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def list_multiple_assignments_gradeable_students(
    session,
    base_url,
    course_id,
    assignment_ids=None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List multiple assignments gradeable students

    `GET /api/v1/courses/:course_id/assignments/gradeable_students`

    A paginated list of students eligible to submit a list of assignments. The caller must have permission to view grades for the requested course.

    Section-limited instructors will only see students in their own sections.

    https://canvas.instructure.com/doc/api/submissions.html#method.submissions_api.multiple_gradeable_students
    """
    method = 'GET'
    url = '/api/v1/courses/{course_id}/assignments/gradeable_students'.format(course_id=course_id)
    query = [
        ('assignment_ids', assignment_ids),
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
        constructor=UserDisplay,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def grade_or_comment_on_multiple_submissions(
    session,
    base_url,
    context: Literal['courses', 'sections'],
    context_id,
    assignment_id,
    grade_data=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Grade or comment on multiple submissions

    `POST /api/v1/courses/:course_id/submissions/update_grades`

    `POST /api/v1/courses/:course_id/assignments/:assignment_id/submissions/update_grades`

    `POST /api/v1/sections/:section_id/submissions/update_grades`

    `POST /api/v1/sections/:section_id/assignments/:assignment_id/submissions/update_grades`

    Update the grading and comments on multiple student's assignment submissions in an asynchronous job.

    The user must have permission to manage grades in the appropriate context (course or section).

    https://canvas.instructure.com/doc/api/submissions.html#method.submissions_api.bulk_update

    Returns:
        a Progress
    """
    if context not in ('courses', 'sections'):
        raise ValueError
    method = 'POST'
    if assignment_id is None:
        url = '/api/v1/{context}/{context_id}/submissions/update_grades'.format(
            context=context, context_id=context_id)
    else:
        url = '/api/v1/{context}/{context_id}/assignments/{assignment_id}/submissions/update_grades'.format(
            context=context, context_id=context_id, assignment_id=assignment_id)
    query = [
        ('grade_data', grade_data),
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


def mark_submission_as_read(
    session,
    base_url,
    context: Literal['courses', 'sections'],
    context_id,
    assignment_id,
    user_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Mark submission as read

    `PUT /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/read`

    `PUT /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/read`

    No request fields are necessary.

    On success, the response will be 204 No Content with an empty body.

    https://canvas.instructure.com/doc/api/submissions.html#method.submissions_api.mark_submission_read

    Returns:
        True on success
    """
    if context not in ('courses', 'sections'):
        raise ValueError
    method = 'PUT'
    url = ('/api/v1/{context}/{context_id}/assignments/{assignment_id}/submissions/{user_id}/read'.
           format(context=context,
                  context_id=context_id,
                  assignment_id=assignment_id,
                  user_id=user_id))
    query = []
    response, _ = utils.request(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
        return_response=True,
    )
    return response.status_code == 204


def mark_submission_as_unread(
    session,
    base_url,
    context: Literal['courses', 'sections'],
    context_id,
    assignment_id,
    user_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Mark submission as unread

    `DELETE /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/read`

    `DELETE /api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/read`

    No request fields are necessary.

    On success, the response will be 204 No Content with an empty body.

    https://canvas.instructure.com/doc/api/submissions.html#method.submissions_api.mark_submission_unread
    """
    if context not in ('courses', 'sections'):
        raise ValueError
    method = 'DELETE'
    url = ('/api/v1/{context}/{context_id}/assignments/{assignment_id}/submissions/{user_id}/read'.
           format(context=context,
                  context_id=context_id,
                  assignment_id=assignment_id,
                  user_id=user_id))
    query = []
    response, _ = utils.request(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
        return_response=True,
    )
    return response.status_code == 204


def submission_summary(
    session,
    base_url,
    context: Literal['courses', 'sections'],
    context_id,
    assignment_id,
    grouped: Optional[bool] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Submission Summary

    `GET /api/v1/courses/:course_id/assignments/:assignment_id/submission_summary`

    `GET /api/v1/sections/:section_id/assignments/:assignment_id/submission_summary`

    Returns the number of submissions for the given assignment based on gradeable students that fall into three categories: graded, ungraded, not submitted.

    https://canvas.instructure.com/doc/api/submissions.html#method.submissions_api.submission_summary
    """
    if context not in ('courses', 'sections'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/assignments/{assignment_id}/submission_summary'.format(
        context=context, context_id=context_id, assignment_id=assignment_id)
    query = [
        ('grouped', grouped),
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


class UserDisplay(objects.Base):
    """
    This mini-object is used for secondary user responses, when we just want to
    provide enough information to display a user.

    https://canvas.instructure.com/doc/api/users.html#UserDisplay
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    @property
    def id(self):
        """The ID of the user."""
        return self.getattr('id')

    @property
    def short_name(self):
        """
        A short name the user has selected, for use in conversations or other less
        formal places through the site.
        """
        return self.getattr('short_name')

    @property
    def avatar_image_url(self):
        """
        If avatars are enabled, this field will be included and contain a url to
        retrieve the user's avatar.
        """
        return self.getattr('avatar_image_url')

    @property
    def html_url(self):
        """URL to access user, either nested to a context or directly."""
        return self.getattr('html_url')

    @property
    def assignment_ids(self):
        """
        an extra assignment_ids field to indicate what assignments that user can submit

        https://canvas.instructure.com/doc/api/submissions.html#method.submissions_api.multiple_gradeable_students
        """
        return self.getattr('assignment_ids')


class AnonymousUserDisplay(objects.Simple):
    """
    This mini-object is returned in place of UserDisplay when returning student
    data for anonymous assignments, and includes an anonymous ID to identify a
    user within the scope of a single assignment.

    https://canvas.instructure.com/doc/api/users.html#AnonymousUserDisplay
    """

    def __init__(self, attributes: dict) -> None:
        super().__init__(attributes=attributes)

    @property
    def anonymous_id(self):
        """
        A unique short ID identifying this user within the scope of a particular
        assignment.
        """
        return self.getattr('anonymous_id')

    @property
    def avatar_image_url(self):
        """A URL to retrieve a generic avatar."""
        return self.getattr('avatar_image_url')


class User(objects.Base):
    """
    A Canvas user, e.g. a student, teacher, administrator, observer, etc.

    https://canvas.instructure.com/doc/api/users.html#User
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('id', 'name')

    @property
    def id(self):
        """The ID of the user."""
        return self.getattr('id')

    @property
    def name(self):
        """The name of the user."""
        return self.getattr('name')

    @property
    def sortable_name(self):
        """
        The name of the user that is should be used for sorting groups of users, such
        as in the gradebook.
        """
        return self.getattr('sortable_name')

    @property
    def short_name(self):
        """
        A short name the user has selected, for use in conversations or other less
        formal places through the site.
        """
        return self.getattr('short_name')

    @property
    def sis_user_id(self):
        """
        The SIS ID associated with the user.  This field is only included if the user
        came from a SIS import and has permissions to view SIS information.
        """
        return self.getattr('sis_user_id')

    @property
    def sis_import_id(self):
        """
        The id of the SIS import.  This field is only included if the user came from
        a SIS import and has permissions to manage SIS information.
        """
        return self.getattr('sis_import_id')

    @property
    def integration_id(self):
        """
        The integration_id associated with the user.  This field is only included if
        the user came from a SIS import and has permissions to view SIS information.
        """
        return self.getattr('integration_id')

    @property
    def login_id(self):
        """
        The unique login id for the user.  This is what the user uses to log in to
        Canvas.
        """
        return self.getattr('login_id')

    @property
    def avatar_url(self):
        """
        If avatars are enabled, this field will be included and contain a url to
        retrieve the user's avatar.
        """
        return self.getattr('avatar_url')

    @property
    def enrollments(self):
        """
        Optional: This field can be requested with certain API calls, and will return
        a list of the users active enrollments. See the List enrollments API for more
        details about the format of these records.
        """
        return self.getattr('enrollments')

    @property
    def email(self):
        """
        Optional: This field can be requested with certain API calls, and will return
        the users primary email address.
        """
        return self.getattr('email')

    @property
    def locale(self):
        """
        Optional: This field can be requested with certain API calls, and will return
        the users locale in RFC 5646 format.
        """
        return self.getattr('locale')

    @property
    def last_login(self):
        """
        Optional: This field is only returned in certain API calls, and will return a
        timestamp representing the last time the user logged in to canvas.
        """
        return self.getattr('last_login')

    @property
    def time_zone(self):
        """
        Optional: This field is only returned in certain API calls, and will return
        the IANA time zone name of the user's preferred timezone.
        """
        return self.getattr('time_zone')

    @property
    def bio(self):
        """Optional: The user's bio."""
        return self.getattr('bio')

    @property
    def created_at(self):
        return self.getattr('created_at')

    @property
    def custom_links(self):
        """
        "custom_links": Optionally include plugin-supplied custom links for each student,
        such as analytics information

        https://canvas.instructure.com/doc/api/courses.html#method.courses.users
        """
        return self.getattr('custom_links')

    @property
    def uuid(self):
        """
        "uuid": Optionally include the users uuid

        https://canvas.instructure.com/doc/api/courses.html#method.courses.users
        """
        return self.getattr('uuid')

    @property
    def effective_locale(self):
        """https://canvas.instructure.com/doc/api/users.html#method.users.api_show"""
        return self.getattr('effective_locale')

    @property
    def permissions(self):
        """https://canvas.instructure.com/doc/api/users.html#method.users.api_show"""
        return self.getattr('permissions')

    @property
    def observation_link_root_account_ids(self):
        """
        The returned observees will include an attribute "observation_link_root_account_ids", a list of ids for the root accounts the observer and observee are linked on. The observer will only be able to observe in courses associated with these root accounts.

        https://canvas.instructure.com/doc/api/user_observees.html#method.user_observees.index
        """
        return self.getattr('observation_link_root_account_ids')


def list_users_in_account(
    session,
    base_url,
    account_id,
    search_term: Optional[str] = None,
    enrollment_type: Optional[str] = None,
    sort: Optional[Literal['username', 'email', 'sis_id', 'last_login']] = None,
    order: Optional[Literal['asc', 'desc']] = None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List users in account

    `GET /api/v1/accounts/:account_id/users`

    A paginated list of of users associated with this account.

    https://canvas.instructure.com/doc/api/users.html#method.users.api_index

    Returns:
        a list of Users
    """
    method = 'GET'
    url = '/api/v1/accounts/{account_id}/users'.format(account_id=account_id)
    query = [
        ('search_term', search_term),
        ('enrollment_type', enrollment_type),
        ('sort', sort),
        ('order', order),
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
        constructor=User,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def list_the_activity_stream(
    session,
    base_url,
    endpoint: Optional[Literal['self']] = 'self',
    only_active_courses: Optional[bool] = None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List the activity stream

    `GET /api/v1/users/self/activity_stream`

    `GET /api/v1/users/activity_stream`

    Returns the current user's global activity stream, paginated.

    https://canvas.instructure.com/doc/api/users.html#method.users.activity_stream
    """
    if endpoint not in ('self', None):
        raise ValueError
    method = 'GET'
    if endpoint == 'self':
        url = '/api/v1/users/self/activity_stream'
    else:
        url = '/api/v1/users/activity_stream'
    query = [
        ('only_active_courses', only_active_courses),
        ('page', page),
        ('per_page', per_page),
    ]
    return paginations.request_json_paginated(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        pagination=pagination,
        raise_for_error=raise_for_error,
    )


def activity_stream_summary(
    session,
    base_url,
    params=None,
    raise_for_error: bool = True,
):
    """
    Activity stream summary

    `GET /api/v1/users/self/activity_stream/summary`

    Returns a summary of the current user's global activity stream.

    https://canvas.instructure.com/doc/api/users.html#method.users.activity_stream_summary
    """
    method = 'GET'
    url = '/api/v1/users/self/activity_stream/summary'
    query = []
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def list_the_todo_items(
    session,
    base_url,
    include=None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List the TODO items

    `GET /api/v1/users/self/todo`

    A paginated list of the current user's list of todo items.

    There is a limit to the number of items returned.

    The `ignore` and `ignore_permanently` URLs can be used to update the user's preferences on what items will be displayed. Performing a DELETE request against the `ignore` URL will hide that item from future todo item requests, until the item changes. Performing a DELETE request against the `ignore_permanently` URL will hide that item forever.

    https://canvas.instructure.com/doc/api/users.html#method.users.todo_items
    """
    method = 'GET'
    url = '/api/v1/users/self/todo'
    query = [
        ('include', include),
        ('page', page),
        ('per_page', per_page),
    ]
    return paginations.request_json_paginated(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        pagination=pagination,
        raise_for_error=raise_for_error,
    )


def list_counts_for_todo_items(
    session,
    base_url,
    include=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    List counts for todo items

    `GET /api/v1/users/self/todo_item_count`

    Counts of different todo items such as the number of assignments needing grading as well as the number of assignments needing submitting.

    There is a limit to the number of todo items this endpoint will count. It will only look at the first 100 todo items for the user. If the user has more than 100 todo items this count may not be reliable. The largest reliable number for both counts is 100.

    https://canvas.instructure.com/doc/api/users.html#method.users.todo_item_count
    """
    method = 'GET'
    url = '/api/v1/users/self/todo_item_count'
    query = [
        ('include', include),
    ]
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def list_upcoming_events(
    session,
    base_url,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List upcoming assignments, calendar events

    `GET /api/v1/users/self/upcoming_events`

    A paginated list of the current user's upcoming events.

    https://canvas.instructure.com/doc/api/users.html#method.users.upcoming_events

    NTU COOL does not seem to support pagination.
    """
    method = 'GET'
    url = '/api/v1/users/self/upcoming_events'
    query = [
        ('page', page),
        ('per_page', per_page),
    ]
    return paginations.request_json_paginated(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        pagination=pagination,
        raise_for_error=raise_for_error,
    )


def list_missing_submissions(
    session,
    base_url,
    user_id,
    include=None,
    filter=None,
    course_ids=None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List Missing Submissions

    `GET /api/v1/users/:user_id/missing_submissions`

    A paginated list of past-due assignments for which the student does not have a submission. The user sending the request must either be the student, an admin or a parent observer using the parent app

    https://canvas.instructure.com/doc/api/users.html#method.users.missing_submissions

    Returns:
        a list of Assignments
    """
    method = 'GET'
    url = '/api/v1/users/{user_id}/missing_submissions'.format(user_id=user_id)
    query = [
        ('include', include),
        ('filter', filter),
        ('course_ids', course_ids),
        ('page', page),
        ('per_page', per_page),
    ]
    return paginations.request_json_paginated(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        pagination=pagination,
        raise_for_error=raise_for_error,
    )


def show_user_details(
    session,
    base_url,
    id,
    include=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Show user details

    `GET /api/v1/users/:id`

    Shows details for user.

    Also includes an attribute "permissions", a non-comprehensive list of permissions for the user.

    https://canvas.instructure.com/doc/api/users.html#method.users.api_show
    """
    method = 'GET'
    url = '/api/v1/users/{id}'.format(id=id)
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
    return User(data, session=session, base_url=base_url)


def update_user_settings(
    session,
    base_url,
    id,
    method: Literal['GET', 'PUT'] = 'GET',
    manual_mark_as_read: Optional[bool] = None,
    release_notes_badge_disabled: Optional[bool] = None,
    collapse_global_nav: Optional[bool] = None,
    hide_dashcard_color_overlays: Optional[bool] = None,
    comment_library_suggestions_enabled: Optional[bool] = None,
    elementary_dashboard_disabled: Optional[bool] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Update user settings.

    `GET /api/v1/users/:id/settings`

    `PUT /api/v1/users/:id/settings`

    Update an existing user's settings.

    https://canvas.instructure.com/doc/api/users.html#method.users.settings

    Args:
        method: `GET` to get user settings. `PUT` to update user settings.
    """
    if method not in ('GET', 'PUT'):
        raise ValueError
    url = '/api/v1/users/{id}/settings'.format(id=id)
    query = [
        ('manual_mark_as_read', manual_mark_as_read),
        ('release_notes_badge_disabled', release_notes_badge_disabled),
        ('collapse_global_nav', collapse_global_nav),
        ('hide_dashcard_color_overlays', hide_dashcard_color_overlays),
        ('comment_library_suggestions_enabled', comment_library_suggestions_enabled),
        ('elementary_dashboard_disabled', elementary_dashboard_disabled),
    ]
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def get_custom_colors(
    session,
    base_url,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get custom colors

    `GET /api/v1/users/:id/colors`

    Returns all custom colors that have been saved for a user.

    https://canvas.instructure.com/doc/api/users.html#method.users.get_custom_colors
    """
    method = 'GET'
    url = '/api/v1/users/{id}/colors'.format(id=id)
    query = []
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def get_custom_color(
    session,
    base_url,
    id,
    asset_string,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get custom color

    `GET /api/v1/users/:id/colors/:asset_string`

    Returns the custom colors that have been saved for a user for a given context.

    The asset_string parameter should be in the format 'context_id', for example 'course_42'.

    https://canvas.instructure.com/doc/api/users.html#method.users.get_custom_color
    """
    method = 'GET'
    url = '/api/v1/users/{id}/colors/{asset_string}'.format(id=id, asset_string=asset_string)
    query = []
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def update_custom_color(
    session,
    base_url,
    id,
    asset_string,
    hexcode: str,
    params=None,
    raise_for_error: bool = True,
):
    """
    Update custom color

    `PUT /api/v1/users/:id/colors/:asset_string`

    Updates a custom color for a user for a given context. This allows colors for the calendar and elsewhere to be customized on a user basis.

    The asset string parameter should be in the format 'context_id', for example 'course_42'

    https://canvas.instructure.com/doc/api/users.html#method.users.set_custom_color
    """
    method = 'PUT'
    url = '/api/v1/users/{id}/colors/{asset_string}'.format(id=id, asset_string=asset_string)
    query = [
        ('hexcode', hexcode),
    ]
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def get_dashboard_positions(
    session,
    base_url,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get dashboard positions

    `GET /api/v1/users/:id/dashboard_positions`

    Returns all dashboard positions that have been saved for a user.

    https://canvas.instructure.com/doc/api/users.html#method.users.get_dashboard_positions
    """
    method = 'GET'
    url = '/api/v1/users/{id}/dashboard_positions'.format(id=id)
    query = []
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def update_dashboard_positions(
    session,
    base_url,
    id,
    dashboard_positions,
    params=None,
    raise_for_error: bool = True,
):
    """
    Update dashboard positions

    `PUT /api/v1/users/:id/dashboard_positions`

    Updates the dashboard positions for a user for a given context. This allows positions for the dashboard cards and elsewhere to be customized on a per user basis.

    The asset string parameter should be in the format 'context_id', for example 'course_42'

    https://canvas.instructure.com/doc/api/users.html#method.users.set_dashboard_positions

    Example:
    ```
    update_dashboard_positions(<session>, <base_url>, <id>, dashboard_positions={'course_42': 1})
    ```
    """
    method = 'PUT'
    url = '/api/v1/users/{id}/dashboard_positions'.format(id=id)
    query = [
        ('dashboard_positions', dashboard_positions),
    ]
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def get_a_users_most_recently_graded_submissions(
    session,
    base_url,
    id,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get a users most recently graded submissions

    `GET /api/v1/users/:id/graded_submissions`

    https://canvas.instructure.com/doc/api/users.html#method.users.user_graded_submissions

    NTU COOL seems to support pagination.
    """
    method = 'GET'
    url = '/api/v1/users/{id}/graded_submissions'.format(id=id)
    query = [
        ('page', page),
        ('per_page', per_page),
    ]
    return paginations.request_json_paginated(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        pagination=pagination,
        raise_for_error=raise_for_error,
    )


def get_user_profile(
    session,
    base_url,
    user_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get user profile

    `GET /api/v1/users/:user_id/profile`

    Returns user profile data, including user id, name, and profile pic.

    When requesting the profile for the user accessing the API, the user's calendar feed URL and LTI user id will be returned as well.

    https://canvas.instructure.com/doc/api/users.html#method.profile.settings

    Returns:
        a Profile
    """
    method = 'GET'
    url = '/api/v1/users/{user_id}/profile'.format(user_id=user_id)
    query = []
    return utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )


def list_avatar_options(
    session,
    base_url,
    user_id,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List avatar options

    `GET /api/v1/users/:user_id/avatars`

    A paginated list of the possible user avatar options that can be set with the user update endpoint. The response will be an array of avatar records. If the 'type' field is 'attachment', the record will include all the normal attachment json fields; otherwise it will include only the 'url' and 'display_name' fields. Additionally, all records will include a 'type' field and a 'token' field.

    https://canvas.instructure.com/doc/api/users.html#method.profile.profile_pics

    NTU COOL does not seem to support pagination.

    Returns:
        a list of Avatars
    """
    method = 'GET'
    url = '/api/v1/users/{user_id}/avatars'.format(user_id=user_id)
    query = [
        ('page', page),
        ('per_page', per_page),
    ]
    return paginations.request_json_paginated(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        pagination=pagination,
        raise_for_error=raise_for_error,
    )


def list_user_page_views(
    session,
    base_url,
    user_id,
    start_time=None,
    end_time=None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List user page views

    `GET /api/v1/users/:user_id/page_views`

    Return a paginated list of the user's page view history in json format, similar to the available CSV download. Page views are returned in descending order, newest to oldest.

    https://canvas.instructure.com/doc/api/users.html#method.page_views.index

    Returns:
        a list of PageViews
    """
    method = 'GET'
    url = '/api/v1/users/{user_id}/page_views'.format(user_id=user_id)
    query = [
        ('start_time', start_time),
        ('end_time', end_time),
        ('page', page),
        ('per_page', per_page),
    ]
    return paginations.request_json_paginated(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        pagination=pagination,
        raise_for_error=raise_for_error,
    )
