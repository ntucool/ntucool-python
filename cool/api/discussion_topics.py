from typing import Literal, Optional, Union

from cool import utils
from cool.api import files, objects, paginations


class FileAttachment(objects.Simple):
    """
    A file attachment

    https://canvas.instructure.com/doc/api/discussion_topics.html#FileAttachment
    """

    def __init__(self, attributes: dict) -> None:
        super().__init__(attributes=attributes)

    @property
    def content_type(self):
        return self.getattr('content-type')

    @property
    def url(self):
        return self.getattr('url')

    @property
    def filename(self):
        return self.getattr('filename')

    @property
    def display_name(self):
        return self.getattr('display_name')


class Reply(objects.Base):
    """
    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics_api.replies
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('id', 'user_id', 'user_name')

    @property
    def id(self):
        """The unique identifier for the reply."""
        return self.getattr('id')

    @property
    def user_id(self):
        """The unique identifier for the author of the reply."""
        return self.getattr('user_id')

    @property
    def editor_id(self):
        """The unique user id of the person to last edit the entry, if different than user_id."""
        return self.getattr('editor_id')

    @property
    def user_name(self):
        """The name of the author of the reply."""
        return self.getattr('user_name')

    @property
    def message(self):
        """The content of the reply."""
        return self.getattr('message')

    @property
    def read_state(self):
        """The read state of the entry, “read” or “unread”."""
        return self.getattr('read_state')

    @property
    def forced_read_state(self):
        """Whether the read_state was forced (was set manually)"""
        return self.getattr('forced_read_state')

    @property
    def created_at(self):
        """The creation time of the reply, in ISO8601 format."""
        return self.getattr('created_at')

    @property
    def parent_id(self):
        return self.getattr('parent_id')

    @property
    def updated_at(self):
        return self.getattr('updated_at')

    @property
    def rating_count(self):
        return self.getattr('rating_count')

    @property
    def rating_sum(self):
        return self.getattr('rating_sum')

    @property
    def user(self):
        return self.getattr('user')

    @property
    def attachment(self):
        return self.getattr('attachment')

    @property
    def attachments(self):
        return self.getattr('attachments')


class Entry(objects.Base):
    """
    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics_api.entries
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('id', 'user_id')

    @property
    def id(self):
        """The unique identifier for the entry."""
        return self.getattr('id')

    @property
    def user_id(self):
        """The unique identifier for the author of the entry."""
        return self.getattr('user_id')

    @property
    def editor_id(self):
        """The unique user id of the person to last edit the entry, if different than user_id."""
        return self.getattr('editor_id')

    @property
    def user_name(self):
        """The name of the author of the entry."""
        return self.getattr('user_name')

    @property
    def message(self):
        """The content of the entry."""
        return self.getattr('message')

    @property
    def read_state(self):
        """The read state of the entry, “read” or “unread”."""
        return self.getattr('read_state')

    @property
    def forced_read_state(self):
        """Whether the read_state was forced (was set manually)"""
        return self.getattr('forced_read_state')

    @property
    def created_at(self):
        """The creation time of the entry, in ISO8601 format."""
        return self.getattr('created_at')

    @property
    def updated_at(self):
        """The updated time of the entry, in ISO8601 format."""
        return self.getattr('updated_at')

    @property
    def attachment(self):
        """JSON representation of the attachment for the entry, if any. Present only if there is an attachment."""
        return self.getattr('attachment')

    @property
    def attachments(self):
        """Deprecated. Same as attachment, but returned as a one-element array. Present only if there is an attachment."""
        return self.getattr('attachments')

    @property
    def recent_replies(self) -> list[Reply]:
        """The 10 most recent replies for the entry, newest first. Present only if there is at least one reply."""
        constructor_kwargs = {'session': self.session, 'base_url': self.base_url}
        return self.getattr('recent_replies',
                            constructor=Reply,
                            constructor_kwargs=constructor_kwargs,
                            type='list')

    @property
    def has_more_replies(self):
        """True if there are more than 10 replies for the entry (i.e., not all were included in this response). Present only if there is at least one reply."""
        return self.getattr('has_more_replies')

    @property
    def parent_id(self):
        return self.getattr('parent_id')

    @property
    def rating_count(self):
        return self.getattr('rating_count')

    @property
    def rating_sum(self):
        return self.getattr('rating_sum')

    @property
    def user(self):
        return self.getattr('user')


class DiscussionTopic(objects.Base):
    """
    A discussion topic

    https://canvas.instructure.com/doc/api/discussion_topics.html#DiscussionTopic
    """

    def __init__(self, attributes: dict, session=None, base_url: str = None) -> None:
        super().__init__(attributes=attributes, session=session, base_url=base_url)

    repr_names = ('id', 'title')

    @property
    def id(self):
        """The ID of this topic."""
        return self.getattr('id')

    @property
    def title(self):
        """The topic title."""
        return self.getattr('title')

    @property
    def message(self):
        """The HTML content of the message body."""
        return self.getattr('message')

    @property
    def html_url(self):
        """The URL to the discussion topic in canvas."""
        return self.getattr('html_url')

    @property
    def posted_at(self):
        """
        The datetime the topic was posted. If it is null it hasn't been posted yet.
        (see delayed_post_at)
        """
        return self.getattr('posted_at')

    @property
    def last_reply_at(self):
        """The datetime for when the last reply was in the topic."""
        return self.getattr('last_reply_at')

    @property
    def require_initial_post(self):
        """
        If true then a user may not respond to other replies until that user has made
        an initial reply. Defaults to false.
        """
        return self.getattr('require_initial_post')

    @property
    def user_can_see_posts(self):
        """Whether or not posts in this topic are visible to the user."""
        return self.getattr('user_can_see_posts')

    @property
    def discussion_subentry_count(self):
        """The count of entries in the topic."""
        return self.getattr('discussion_subentry_count')

    @property
    def read_state(self):
        """The read_state of the topic for the current user, 'read' or 'unread'."""
        return self.getattr('read_state')

    @property
    def unread_count(self):
        """The count of unread entries of this topic for the current user."""
        return self.getattr('unread_count')

    @property
    def subscribed(self):
        """Whether or not the current user is subscribed to this topic."""
        return self.getattr('subscribed')

    @property
    def subscription_hold(self):
        """
        (Optional) Why the user cannot subscribe to this topic. Only one reason will
        be returned even if multiple apply. Can be one of: 'initial_post_required':
        The user must post a reply first; 'not_in_group_set': The user is not in the
        group set for this graded group discussion; 'not_in_group': The user is not
        in this topic's group; 'topic_is_announcement': This topic is an announcement
        """
        return self.getattr('subscription_hold')

    @property
    def assignment_id(self):
        """
        The unique identifier of the assignment if the topic is for grading,
        otherwise null.
        """
        return self.getattr('assignment_id')

    @property
    def delayed_post_at(self):
        """The datetime to publish the topic (if not right away)."""
        return self.getattr('delayed_post_at')

    @property
    def published(self):
        """Whether this discussion topic is published (true) or draft state (false)"""
        return self.getattr('published')

    @property
    def lock_at(self):
        """The datetime to lock the topic (if ever)."""
        return self.getattr('lock_at')

    @property
    def locked(self):
        """Whether or not the discussion is 'closed for comments'."""
        return self.getattr('locked')

    @property
    def pinned(self):
        """Whether or not the discussion has been 'pinned' by an instructor"""
        return self.getattr('pinned')

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
    def user_name(self):
        """The username of the topic creator."""
        return self.getattr('user_name')

    @property
    def topic_children(self):
        """
        DEPRECATED An array of topic_ids for the group discussions the user is a part
        of.
        """
        return self.getattr('topic_children')

    @property
    def group_topic_children(self):
        """
        An array of group discussions the user is a part of. Fields include: id,
        group_id
        """
        return self.getattr('group_topic_children')

    @property
    def root_topic_id(self):
        """
        If the topic is for grading and a group assignment this will point to the
        original topic in the course.
        """
        return self.getattr('root_topic_id')

    @property
    def podcast_url(self):
        """If the topic is a podcast topic this is the feed url for the current user."""
        return self.getattr('podcast_url')

    @property
    def discussion_type(self):
        """
        The type of discussion. Values are 'side_comment', for discussions that only
        allow one level of nested comments, and 'threaded' for fully threaded
        discussions.
        """
        return self.getattr('discussion_type')

    @property
    def group_category_id(self):
        """
        The unique identifier of the group category if the topic is a group
        discussion, otherwise null.
        """
        return self.getattr('group_category_id')

    # @property
    # def attachments(self) -> list[files.File]:
    #     """Array of file attachments."""
    #     constructor_kwargs = {'session': self.session, 'base_url': self.base_url}
    #     return self.getattr('attachments',
    #                         constructor=files.File,
    #                         constructor_kwargs=constructor_kwargs,
    #                         type='list')

    @property
    def attachments(self):
        """Array of file attachments."""
        return self.getattr('attachments')

    @property
    def permissions(self):
        """The current user's permissions on this topic."""
        return self.getattr('permissions')

    @property
    def allow_rating(self):
        """Whether or not users can rate entries in this topic."""
        return self.getattr('allow_rating')

    @property
    def only_graders_can_rate(self):
        """Whether or not grade permissions are required to rate entries."""
        return self.getattr('only_graders_can_rate')

    @property
    def sort_by_rating(self):
        """Whether or not entries should be sorted by rating."""
        return self.getattr('sort_by_rating')

    @property
    def user_count(self):
        """
        https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics.index
        """
        return self.getattr('user_count')

    @property
    def context_code(self):
        """
        which course the announcement belongs to

        https://canvas.instructure.com/doc/api/announcements.html#method.announcements_api.index
        """
        return self.getattr('context_code')

    @property
    def created_at(self):
        return self.getattr('created_at')

    @property
    def position(self):
        return self.getattr('position')

    @property
    def podcast_has_student_posts(self):
        return self.getattr('podcast_has_student_posts')

    @property
    def is_section_specific(self):
        return self.getattr('is_section_specific')

    @property
    def can_unpublish(self):
        return self.getattr('can_unpublish')

    @property
    def can_lock(self):
        return self.getattr('can_lock')

    @property
    def comments_disabled(self):
        return self.getattr('comments_disabled')

    @property
    def author(self):
        return self.getattr('author')

    @property
    def url(self):
        return self.getattr('url')

    @property
    def can_group(self):
        return self.getattr('can_group')

    @property
    def todo_date(self):
        return self.getattr('todo_date')


def list_discussion_topics(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    include=None,
    order_by: Optional[Literal['position', 'recent_activity', 'title']] = None,
    scope: Optional[Literal['locked', 'unlocked', 'pinned', 'unpinned']] = None,
    only_announcements: Optional[bool] = None,
    filter_by: Optional[Literal['all', 'unread']] = None,
    search_term: Optional[str] = None,
    exclude_context_module_locked_topics: Optional[bool] = None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List discussion topics

    `GET /api/v1/courses/:course_id/discussion_topics`

    `GET /api/v1/groups/:group_id/discussion_topics`

    Returns the paginated list of discussion topics for this course or group.

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics.index

    Returns:
        a list of DiscussionTopics
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/discussion_topics'.format(context=context,
                                                                    context_id=context_id)
    query = [
        ('include', include),
        ('order_by', order_by),
        ('scope', scope),
        ('only_announcements', only_announcements),
        ('filter_by', filter_by),
        ('search_term', search_term),
        ('exclude_context_module_locked_topics', exclude_context_module_locked_topics),
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
        constructor=DiscussionTopic,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def create_a_new_discussion_topic(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    title: Optional[str] = None,
    message: Optional[str] = None,
    discussion_type: Optional[Literal['side_comment', 'threaded']] = None,
    published: Optional[bool] = None,
    delayed_post_at=None,
    allow_rating: Optional[bool] = None,
    lock_at=None,
    podcast_enabled: Optional[bool] = None,
    podcast_has_student_posts: Optional[bool] = None,
    require_initial_post: Optional[bool] = None,
    assignment=None,
    is_announcement: Optional[bool] = None,
    pinned: Optional[bool] = None,
    position_after: Optional[str] = None,
    group_category_id: Optional[int] = None,
    only_graders_can_rate: Optional[bool] = None,
    sort_by_rating: Optional[bool] = None,
    attachment=None,
    specific_sections: Optional[str] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Create a new discussion topic

    `POST /api/v1/courses/:course_id/discussion_topics`

    `POST /api/v1/groups/:group_id/discussion_topics`

    Create an new discussion topic for the course or group.

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics.create
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'POST'
    url = '/api/v1/{context}/{context_id}/discussion_topics'.format(context=context,
                                                                    context_id=context_id)
    query = [
        ('title', title),
        ('message', message),
        ('discussion_type', discussion_type),
        ('published', published),
        ('delayed_post_at', delayed_post_at),
        ('allow_rating', allow_rating),
        ('lock_at', lock_at),
        ('podcast_enabled', podcast_enabled),
        ('podcast_has_student_posts', podcast_has_student_posts),
        ('require_initial_post', require_initial_post),
        ('assignment', assignment),
        ('is_announcement', is_announcement),
        ('pinned', pinned),
        ('position_after', position_after),
        ('group_category_id', group_category_id),
        ('only_graders_can_rate', only_graders_can_rate),
        ('sort_by_rating', sort_by_rating),
        ('attachment', attachment),
        ('specific_sections', specific_sections),
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


def update_a_topic(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    topic_id,
    title: Optional[str] = None,
    message: Optional[str] = None,
    discussion_type: Optional[Literal['side_comment', 'threaded']] = None,
    published: Optional[bool] = None,
    delayed_post_at=None,
    lock_at=None,
    podcast_enabled: Optional[bool] = None,
    podcast_has_student_posts: Optional[bool] = None,
    require_initial_post: Optional[bool] = None,
    assignment=None,
    is_announcement: Optional[bool] = None,
    pinned: Optional[bool] = None,
    position_after: Optional[str] = None,
    group_category_id: Optional[int] = None,
    allow_rating: Optional[bool] = None,
    only_graders_can_rate: Optional[bool] = None,
    sort_by_rating: Optional[bool] = None,
    specific_sections: Optional[str] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Update a topic

    `PUT /api/v1/courses/:course_id/discussion_topics/:topic_id`

    `PUT /api/v1/groups/:group_id/discussion_topics/:topic_id`

    Update an existing discussion topic for the course or group.

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics.update
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'PUT'
    url = '/api/v1/{context}/{context_id}/discussion_topics/{topic_id}'.format(
        context=context, context_id=context_id, topic_id=topic_id)
    query = [
        ('title', title),
        ('message', message),
        ('discussion_type', discussion_type),
        ('published', published),
        ('delayed_post_at', delayed_post_at),
        ('lock_at', lock_at),
        ('podcast_enabled', podcast_enabled),
        ('podcast_has_student_posts', podcast_has_student_posts),
        ('require_initial_post', require_initial_post),
        ('assignment', assignment),
        ('is_announcement', is_announcement),
        ('pinned', pinned),
        ('position_after', position_after),
        ('group_category_id', group_category_id),
        ('allow_rating', allow_rating),
        ('only_graders_can_rate', only_graders_can_rate),
        ('sort_by_rating', sort_by_rating),
        ('specific_sections', specific_sections),
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


def delete_a_topic(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    topic_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Delete a topic

    `DELETE /api/v1/courses/:course_id/discussion_topics/:topic_id`

    `DELETE /api/v1/groups/:group_id/discussion_topics/:topic_id`

    Deletes the discussion topic. This will also delete the assignment, if it's an assignment discussion.

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics.destroy
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'DELETE'
    url = '/api/v1/{context}/{context_id}/discussion_topics/{topic_id}'.format(
        context=context, context_id=context_id, topic_id=topic_id)
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


def reorder_pinned_topics(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    order=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Reorder pinned topics

    `POST /api/v1/courses/:course_id/discussion_topics/reorder`

    `POST /api/v1/groups/:group_id/discussion_topics/reorder`

    Puts the pinned discussion topics in the specified order. All pinned topics should be included.

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics.reorder
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'POST'
    url = '/api/v1/{context}/{context_id}/discussion_topics/reorder'.format(context=context,
                                                                            context_id=context_id)
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


def update_an_entry(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    topic_id,
    id,
    message: Optional[str] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Update an entry

    `PUT /api/v1/courses/:course_id/discussion_topics/:topic_id/entries/:id`

    `PUT /api/v1/groups/:group_id/discussion_topics/:topic_id/entries/:id`

    Update an existing discussion entry.

    The entry must have been created by the current user, or the current user must have admin rights to the discussion. If the edit is not allowed, a 401 will be returned.

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_entries.update
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'PUT'
    url = '/api/v1/{context}/{context_id}/discussion_topics/{topic_id}/entries/{id}'.format(
        context=context, context_id=context_id, topic_id=topic_id, id=id)
    query = [
        ('message', message),
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


def delete_an_entry(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    topic_id,
    id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Delete an entry

    `DELETE /api/v1/courses/:course_id/discussion_topics/:topic_id/entries/:id`

    `DELETE /api/v1/groups/:group_id/discussion_topics/:topic_id/entries/:id`

    Delete a discussion entry.

    The entry must have been created by the current user, or the current user must have admin rights to the discussion. If the delete is not allowed, a 401 will be returned.

    The discussion will be marked deleted, and the user_id and message will be cleared out.

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_entries.destroy
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'DELETE'
    url = '/api/v1/{context}/{context_id}/discussion_topics/{topic_id}/entries/{id}'.format(
        context=context, context_id=context_id, topic_id=topic_id, id=id)
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


def get_a_single_topic(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    topic_id,
    include=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get a single topic

    `GET /api/v1/courses/:course_id/discussion_topics/:topic_id`

    `GET /api/v1/groups/:group_id/discussion_topics/:topic_id`

    Returns data on an individual discussion topic. See the List action for the response formatting.

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics_api.show
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/discussion_topics/{topic_id}'.format(
        context=context, context_id=context_id, topic_id=topic_id)
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
    return DiscussionTopic(data, session=session, base_url=base_url)


def get_the_full_topic(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    topic_id,
    include_new_entries=None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Get the full topic

    `GET /api/v1/courses/:course_id/discussion_topics/:topic_id/view`

    `GET /api/v1/groups/:group_id/discussion_topics/:topic_id/view`

    Return a cached structure of the discussion topic, containing all entries, their authors, and their message bodies.

    May require (depending on the topic) that the user has posted in the topic. If it is required, and the user has not posted, will respond with a 403 Forbidden status and the body 'require_initial_post'.

    In some rare situations, this cached structure may not be available yet. In that case, the server will respond with a 503 error, and the caller should try again soon.

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics_api.view
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/discussion_topics/{topic_id}/view'.format(
        context=context, context_id=context_id, topic_id=topic_id)
    query = [
        ('include_new_entries', include_new_entries),
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


def post_an_entry(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    topic_id,
    message: Optional[str] = None,
    attachment: Optional[str] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Post an entry

    `POST /api/v1/courses/:course_id/discussion_topics/:topic_id/entries`

    `POST /api/v1/groups/:group_id/discussion_topics/:topic_id/entries`

    Create a new entry in a discussion topic. Returns a json representation of the created entry (see documentation for 'entries' method) on success.

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics_api.add_entry
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'POST'
    url = '/api/v1/{context}/{context_id}/discussion_topics/{topic_id}/entries'.format(
        context=context, context_id=context_id, topic_id=topic_id)
    query = [
        ('message', message),
        ('attachment', attachment),
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


def duplicate_discussion_topic(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    topic_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Duplicate discussion topic

    `POST /api/v1/courses/:course_id/discussion_topics/:topic_id/duplicate`

    `POST /api/v1/groups/:group_id/discussion_topics/:topic_id/duplicate`

    Duplicate a discussion topic according to context (Course/Group)

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics_api.duplicate

    Returns:
        a DiscussionTopic
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'POST'
    url = '/api/v1/{context}/{context_id}/discussion_topics/{topic_id}/duplicate'.format(
        context=context, context_id=context_id, topic_id=topic_id)
    query = []
    data = utils.request_json(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_error=raise_for_error,
    )
    return DiscussionTopic(data, session=session, base_url=base_url)


def list_topic_entries(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    topic_id,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List topic entries

    `GET /api/v1/courses/:course_id/discussion_topics/:topic_id/entries`

    `GET /api/v1/groups/:group_id/discussion_topics/:topic_id/entries`

    Retrieve the (paginated) top-level entries in a discussion topic.

    May require (depending on the topic) that the user has posted in the topic. If it is required, and the user has not posted, will respond with a 403 Forbidden status and the body 'require_initial_post'.

    Will include the 10 most recent replies, if any, for each entry returned.

    If the topic is a root topic with children corresponding to groups of a group assignment, entries from those subtopics for which the user belongs to the corresponding group will be returned.

    Ordering of returned entries is newest-first by posting timestamp (reply activity is ignored).

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics_api.entries
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/discussion_topics/{topic_id}/entries'.format(
        context=context, context_id=context_id, topic_id=topic_id)
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
        constructor=Entry,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def post_a_reply(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    topic_id,
    entry_id,
    message: Optional[str] = None,
    attachment: Optional[str] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Post a reply

    `POST /api/v1/courses/:course_id/discussion_topics/:topic_id/entries/:entry_id/replies`

    `POST /api/v1/groups/:group_id/discussion_topics/:topic_id/entries/:entry_id/replies`

    Add a reply to an entry in a discussion topic. Returns a json representation of the created reply (see documentation for 'replies' method) on success.

    May require (depending on the topic) that the user has posted in the topic. If it is required, and the user has not posted, will respond with a 403 Forbidden status and the body 'require_initial_post'.

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics_api.add_reply
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'POST'
    url = ('/api/v1/{context}/{context_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies'.
           format(context=context, context_id=context_id, topic_id=topic_id, entry_id=entry_id))
    query = [
        ('message', message),
        ('attachment', attachment),
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


def list_entry_replies(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    topic_id,
    entry_id,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List entry replies

    `GET /api/v1/courses/:course_id/discussion_topics/:topic_id/entries/:entry_id/replies`

    `GET /api/v1/groups/:group_id/discussion_topics/:topic_id/entries/:entry_id/replies`

    Retrieve the (paginated) replies to a top-level entry in a discussion topic.

    May require (depending on the topic) that the user has posted in the topic. If it is required, and the user has not posted, will respond with a 403 Forbidden status and the body 'require_initial_post'.

    Ordering of returned entries is newest-first by creation timestamp.

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics_api.replies
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'GET'
    url = ('/api/v1/{context}/{context_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies'.
           format(context=context, context_id=context_id, topic_id=topic_id, entry_id=entry_id))
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
        constructor=Reply,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def list_entries(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    topic_id,
    ids=None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List entries

    `GET /api/v1/courses/:course_id/discussion_topics/:topic_id/entry_list`

    `GET /api/v1/groups/:group_id/discussion_topics/:topic_id/entry_list`

    Retrieve a paginated list of discussion entries, given a list of ids.

    May require (depending on the topic) that the user has posted in the topic. If it is required, and the user has not posted, will respond with a 403 Forbidden status and the body 'require_initial_post'.

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics_api.entry_list
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'GET'
    url = '/api/v1/{context}/{context_id}/discussion_topics/{topic_id}/entry_list'.format(
        context=context, context_id=context_id, topic_id=topic_id)
    query = [
        ('ids', ids),
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
        constructor=Entry,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )


def mark_topic_as_read(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    topic_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Mark topic as read

    `PUT /api/v1/courses/:course_id/discussion_topics/:topic_id/read`

    `PUT /api/v1/groups/:group_id/discussion_topics/:topic_id/read`

    Mark the initial text of the discussion topic as read.

    No request fields are necessary.

    On success, the response will be 204 No Content with an empty body.

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics_api.mark_topic_read
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'PUT'
    url = '/api/v1/{context}/{context_id}/discussion_topics/{topic_id}/read'.format(
        context=context, context_id=context_id, topic_id=topic_id)
    query = []
    response, _ = utils.request(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_status=raise_for_error,
    )
    return response.status_code == 204


def mark_topic_as_unread(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    topic_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Mark topic as unread

    `DELETE /api/v1/courses/:course_id/discussion_topics/:topic_id/read`

    `DELETE /api/v1/groups/:group_id/discussion_topics/:topic_id/read`

    Mark the initial text of the discussion topic as unread.

    No request fields are necessary.

    On success, the response will be 204 No Content with an empty body.

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics_api.mark_topic_unread
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'DELETE'
    url = '/api/v1/{context}/{context_id}/discussion_topics/{topic_id}/read'.format(
        context=context, context_id=context_id, topic_id=topic_id)
    query = []
    response, _ = utils.request(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_status=raise_for_error,
    )
    return response.status_code == 204


def mark_all_entries_as_read(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    topic_id,
    forced_read_state: Optional[bool] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Mark all entries as read

    `PUT /api/v1/courses/:course_id/discussion_topics/:topic_id/read_all`

    `PUT /api/v1/groups/:group_id/discussion_topics/:topic_id/read_all`

    Mark the discussion topic and all its entries as read.

    No request fields are necessary.

    On success, the response will be 204 No Content with an empty body.

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics_api.mark_all_read
    
    Replies will be marked as read as well.
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'PUT'
    url = '/api/v1/{context}/{context_id}/discussion_topics/{topic_id}/read_all'.format(
        context=context, context_id=context_id, topic_id=topic_id)
    query = [
        ('forced_read_state', forced_read_state),
    ]
    response, _ = utils.request(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_status=raise_for_error,
    )
    return response.status_code == 204


def mark_all_entries_as_unread(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    topic_id,
    forced_read_state: Optional[bool] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Mark all entries as unread

    `DELETE /api/v1/courses/:course_id/discussion_topics/:topic_id/read_all`

    `DELETE /api/v1/groups/:group_id/discussion_topics/:topic_id/read_all`

    Mark the discussion topic and all its entries as unread.

    No request fields are necessary.

    On success, the response will be 204 No Content with an empty body.

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics_api.mark_all_unread
    
    Replies will be marked as unread as well.
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'DELETE'
    url = '/api/v1/{context}/{context_id}/discussion_topics/{topic_id}/read_all'.format(
        context=context, context_id=context_id, topic_id=topic_id)
    query = [
        ('forced_read_state', forced_read_state),
    ]
    response, _ = utils.request(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_status=raise_for_error,
    )
    return response.status_code == 204


def mark_entry_as_read(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    topic_id,
    entry_id,
    forced_read_state: Optional[bool] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Mark entry as read

    `PUT /api/v1/courses/:course_id/discussion_topics/:topic_id/entries/:entry_id/read`

    `PUT /api/v1/groups/:group_id/discussion_topics/:topic_id/entries/:entry_id/read`

    Mark a discussion entry as read.

    No request fields are necessary.

    On success, the response will be 204 No Content with an empty body.

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics_api.mark_entry_read
    
    Replies can be marked as read as well.
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'PUT'
    url = ('/api/v1/{context}/{context_id}/discussion_topics/{topic_id}/entries/{entry_id}/read'.
           format(context=context, context_id=context_id, topic_id=topic_id, entry_id=entry_id))
    query = [
        ('forced_read_state', forced_read_state),
    ]
    response, _ = utils.request(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_status=raise_for_error,
    )
    return response.status_code == 204


def mark_entry_as_unread(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    topic_id,
    entry_id,
    forced_read_state: Optional[bool] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Mark entry as unread

    `DELETE /api/v1/courses/:course_id/discussion_topics/:topic_id/entries/:entry_id/read`

    `DELETE /api/v1/groups/:group_id/discussion_topics/:topic_id/entries/:entry_id/read`

    Mark a discussion entry as unread.

    No request fields are necessary.

    On success, the response will be 204 No Content with an empty body.

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics_api.mark_entry_unread

    Replies can be marked as unread as well.
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'DELETE'
    url = ('/api/v1/{context}/{context_id}/discussion_topics/{topic_id}/entries/{entry_id}/read'.
           format(context=context, context_id=context_id, topic_id=topic_id, entry_id=entry_id))
    query = [
        ('forced_read_state', forced_read_state),
    ]
    response, _ = utils.request(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_status=raise_for_error,
    )
    return response.status_code == 204


def rate_entry(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    topic_id,
    entry_id,
    rating: Optional[Literal[0, 1]] = None,
    params=None,
    raise_for_error: bool = True,
):
    """
    Rate entry

    `POST /api/v1/courses/:course_id/discussion_topics/:topic_id/entries/:entry_id/rating`

    `POST /api/v1/groups/:group_id/discussion_topics/:topic_id/entries/:entry_id/rating`

    Rate a discussion entry.

    On success, the response will be 204 No Content with an empty body.

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics_api.rate_entry
    
    Replies may be rated as well.
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'POST'
    url = ('/api/v1/{context}/{context_id}/discussion_topics/{topic_id}/entries/{entry_id}/rating'.
           format(context=context, context_id=context_id, topic_id=topic_id, entry_id=entry_id))
    query = [
        ('rating', rating),
    ]
    response, _ = utils.request(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_status=raise_for_error,
    )
    return response.status_code == 204


def subscribe_to_a_topic(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    topic_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Subscribe to a topic

    `PUT /api/v1/courses/:course_id/discussion_topics/:topic_id/subscribed`

    `PUT /api/v1/groups/:group_id/discussion_topics/:topic_id/subscribed`

    Subscribe to a topic to receive notifications about new entries

    On success, the response will be 204 No Content with an empty body

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics_api.subscribe_topic
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'PUT'
    url = '/api/v1/{context}/{context_id}/discussion_topics/{topic_id}/subscribed'.format(
        context=context, context_id=context_id, topic_id=topic_id)
    query = []
    response, _ = utils.request(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_status=raise_for_error,
    )
    return response.status_code == 204


def unsubscribe_from_a_topic(
    session,
    base_url,
    context: Literal['courses', 'groups'],
    context_id,
    topic_id,
    params=None,
    raise_for_error: bool = True,
):
    """
    Unsubscribe from a topic

    `DELETE /api/v1/courses/:course_id/discussion_topics/:topic_id/subscribed`

    `DELETE /api/v1/groups/:group_id/discussion_topics/:topic_id/subscribed`

    Unsubscribe from a topic to stop receiving notifications about new entries

    On success, the response will be 204 No Content with an empty body

    https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics_api.unsubscribe_topic
    """
    if context not in ('courses', 'groups'):
        raise ValueError
    method = 'DELETE'
    url = '/api/v1/{context}/{context_id}/discussion_topics/{topic_id}/subscribed'.format(
        context=context, context_id=context_id, topic_id=topic_id)
    query = []
    response, _ = utils.request(
        session,
        method,
        base_url,
        url,
        queries=[query, params],
        raise_for_status=raise_for_error,
    )
    return response.status_code == 204
