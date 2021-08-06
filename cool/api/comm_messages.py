from typing import Literal, Optional, Union

from cool import utils
from cool.api import objects, paginations


class CommMessage(objects.Simple):
    """
    https://canvas.instructure.com/doc/api/comm_messages.html#CommMessage
    """

    def __init__(self, attributes: dict) -> None:
        super().__init__(attributes=attributes)

    @property
    def id(self):
        """The ID of the CommMessage."""
        return self.getattr('id')

    @property
    def created_at(self):
        """The date and time this message was created"""
        return self.getattr('created_at')

    @property
    def sent_at(self):
        """The date and time this message was sent"""
        return self.getattr('sent_at')

    @property
    def workflow_state(self):
        """
        The workflow state of the message. One of 'created', 'staged', 'sending',
        'sent', 'bounced', 'dashboard', 'cancelled', or 'closed'
        """
        return self.getattr('workflow_state')

    @property
    def from_(self):
        """The address that was put in the 'from' field of the message"""
        return self.getattr('from')

    @property
    def from_name(self):
        """The display name for the from address"""
        return self.getattr('from_name')

    @property
    def to(self):
        """The address the message was sent to:"""
        return self.getattr('to')

    @property
    def reply_to(self):
        """The reply_to header of the message"""
        return self.getattr('reply_to')

    @property
    def subject(self):
        """The message subject"""
        return self.getattr('subject')

    @property
    def body(self):
        """The plain text body of the message"""
        return self.getattr('body')

    @property
    def html_body(self):
        """The HTML body of the message."""
        return self.getattr('html_body')


def list_of_commmessages_for_a_user(
    session,
    base_url,
    user_id: str,
    start_time=None,
    end_time=None,
    per_page: Optional[int] = None,
    page=None,
    pagination: Union[bool, Literal['current']] = True,
    params=None,
    raise_for_error: bool = True,
):
    """
    List of CommMessages for a user

    `GET /api/v1/comm_messages`

    Retrieve a paginated list of messages sent to a user.

    https://canvas.instructure.com/doc/api/comm_messages.html#method.comm_messages_api.index

    Returns:
        a list of CommMessages
    """
    method = 'GET'
    url = '/api/v1/comm_messages'
    query = [
        ('user_id', user_id),
        ('start_time', start_time),
        ('end_time', end_time),
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
        constructor=CommMessage,
        constructor_kwargs=constructor_kwargs,
        raise_for_error=raise_for_error,
    )
