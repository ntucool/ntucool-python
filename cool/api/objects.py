import collections.abc
import json
import keyword

from typing import Any, final, TypedDict

import requests


class Simple:

    def __init__(self, attributes: dict = None) -> None:
        attributes = {} if attributes is None else attributes
        self.attributes = attributes

        # debug
        if hasattr(self, 'repr_names'):
            missing_names = []
            for name in self.repr_names:
                if not hasattr(self, name):
                    missing_names.append(name)
            if missing_names != []:
                obj = self
                raise RuntimeError(
                    '{!r} object does not have some attributes: {!r} in repr_names'.format(
                        obj, missing_names))

    def __repr__(self) -> str:
        if not hasattr(self, 'repr_names'):
            return super().__repr__()
        format_string = self.__class__.__name__
        info = []
        for name in self.repr_names:
            if hasattr(self, name):
                info.append(f'{name}={getattr(self, name)!r}')
        format_string += '(' + ', '.join(info) + ')'
        return format_string

    def __eq__(self, o: object) -> bool:
        if isinstance(o, self.__class__):
            return self.attributes == o.attributes
        return super().__eq__(o)

    def __contains__(self, o: object) -> bool:
        return o in self.attributes

    def __iter__(self) -> collections.abc.Iterator[str]:
        return iter(self.attributes)

    def __getitem__(self, k: str):
        return self.attributes[k]

    def getattr(self, name, constructor=None, constructor_kwargs=None, type='single') -> Any:
        if type not in ('single', 'list'):
            raise ValueError
        if name in self.attributes:
            value = self.attributes[name]
            # hasattr is implemented by calling getattr(object, name) and seeing whether it raises an AttributeError or not.
            # avoid raising AttributeError
            if value is not None and constructor is not None:
                try:
                    constructor_kwargs = {} if constructor_kwargs is None else constructor_kwargs
                    if type == 'single':
                        value = constructor(value, **constructor_kwargs)
                    elif type == 'list':
                        value = [constructor(v, **constructor_kwargs) for v in value]
                except AttributeError as error:
                    raise RuntimeError(error)
            return value
        else:
            obj = self.__class__.__name__
            raise AttributeError('{!r} object has no attribute {!r}'.format(obj, name))

    def get_properties(self) -> dict[str, Any]:
        properties = {}
        for key in self.attributes:
            name = key.replace('-', '_').replace('?', '')
            if keyword.iskeyword(name):
                name = name + '_'
            if (hasattr(self.__class__, name) and
                    isinstance(getattr(self.__class__, name), property) and hasattr(self, name)):
                properties[name] = getattr(self, name)
            else:
                properties[key] = self.attributes[key]
        return properties


class Interface:

    def __init__(self, session=None, base_url: str = None) -> None:
        self._session: requests.Session = session
        self._base_url = base_url

    @property
    def session(self):
        return self._session

    @session.setter
    def session(self, value):
        self._session = value
        if hasattr(self, 'interfaces'):
            for interface in self.interfaces:
                interface.session = value

    @property
    def base_url(self):
        return self._base_url

    @base_url.setter
    def base_url(self, value):
        self._base_url = value
        if hasattr(self, 'interfaces'):
            for interface in self.interfaces:
                interface.base_url = value

    def __repr__(self) -> str:
        if not hasattr(self, 'repr_names'):
            return super().__repr__()
        format_string = self.__class__.__name__
        info = [f'{name}={getattr(self, name)!r}' for name in self.repr_names]
        format_string += '(' + ', '.join(info) + ')'
        return format_string


class Base(Simple, Interface):

    def __init__(self, attributes: dict = None, session=None, base_url: str = None) -> None:
        Simple.__init__(self, attributes=attributes)
        Interface.__init__(self, session=session, base_url=base_url)
        # debug
        missing_keys = []
        for key in attributes:
            name = key.replace('-', '_').replace('?', '')
            if keyword.iskeyword(name):
                name = name + '_'
            if hasattr(self, name):
                if (self.__class__.__name__, key, name) in (
                    ('File', 'user', 'user'),
                    ('File', 'usage_rights', 'usage_rights'),
                    ('Module', 'items', 'items'),
                    ('ModuleItem', 'content_details', 'content_details'),
                    ('ModuleItem', 'completion_requirement', 'completion_requirement'),
                    ('ModuleItemSequence', 'items', 'items'),
                    ('ModuleItemSequence', 'modules', 'modules'),
                    ('ModuleItemSequenceNode', 'prev', 'prev'),
                    ('ModuleItemSequenceNode', 'current', 'current'),
                    ('ModuleItemSequenceNode', 'next', 'next'),
                    ('Quiz', 'permissions', 'permissions'),
                    ('Section', 'students', 'students'),
                    ('Feature', 'feature_flag', 'feature_flag'),
                    ('Assignment', 'score_statistics', 'score_statistics'),
                    ('Assignment', 'all_dates', 'all_dates'),
                    ('Assignment', 'lock_info', 'lock_info'),
                    ('Assignment', 'rubric', 'rubric'),
                    ('RubricCriteria', 'ratings', 'ratings'),
                    ('Submission', 'assignment', 'assignment'),
                    ('Submission', 'course', 'course'),
                    ('Submission', 'user', 'user'),
                    ('Submission', 'submission_history', 'submission_history'),
                    ('SubmissionsGroupedByStudent', 'submissions', 'submissions'),
                    ('QuizSubmissionsResponse', 'quiz_submissions', 'quiz_submissions'),
                    ('QuizSubmissionsResponse', 'submissions', 'submissions'),
                    ('QuizSubmissionsResponse', 'quizzes', 'quizzes'),
                    ('QuizSubmissionsResponse', 'users', 'users'),
                    ('QuizSubmissionQuestionsResponse', 'quiz_submission_questions',
                     'quiz_submission_questions'),
                    ('QuizSubmissionQuestionsResponse', 'quiz_questions', 'quiz_questions'),
                    ('QuizQuestion', 'answers', 'answers'),
                    ('QuizSubmissionQuestion', 'answers', 'answers'),
                    ('Entry', 'recent_replies', 'recent_replies'),
                    ('DiscussionTopic', 'attachments', 'attachments'),
                ):
                    continue
                if getattr(self, name) != self.attributes[key]:
                    raise RuntimeError(
                        '{} has attribute {!r} but differs from the value in its attributes'.format(
                            self,
                            name,
                        ))
            else:
                missing_keys.append(key)
        if missing_keys != []:
            raise RuntimeError('{} missing keys: {!r}\nattributes keys: {!r}'.format(
                self,
                tuple(missing_keys),
                tuple(self.attributes),
            ))


class Meta(TypedDict):
    primaryCollection: str


class CompoundDocument(Simple):
    """
    https://canvas.instructure.com/doc/api/file.compound_documents.html
    """

    def __init__(self, attributes: dict) -> None:
        super().__init__(attributes=attributes)

    @property
    @final
    def meta(self) -> Meta:
        return self.getattr('meta')

    @property
    @final
    def links(self):
        return self.getattr('links')


class Encoder(json.JSONEncoder):

    def default(self, o: Any) -> Any:
        if isinstance(o, Simple):
            return o.attributes
        return super().default(o)
