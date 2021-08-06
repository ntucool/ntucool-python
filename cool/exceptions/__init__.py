import json


class Error(Exception):

    def __init__(self, *args: object) -> None:
        self.args = args


class APIError(Error):
    """"""


class HTTPError(APIError):

    def __init__(
        self,
        *args: object,
        status_code=None,
        reason=None,
        data=None,
        request=None,
        response=None,
    ) -> None:
        super().__init__(*args)
        if response is not None:
            if status_code is None and hasattr(response, 'status_code'):
                status_code = response.status_code
            if reason is None and hasattr(response, 'reason'):
                reason = response.reason
            if request is None and hasattr(response, 'request'):
                request = response.request
        self.status_code = status_code
        self.reason = reason
        self.data = data
        self.response = response
        self.request = request


class WWWAuthenticateError(HTTPError):
    """
    If the token is deleted or expires, the application will get a 401 Unauthorized error from the API, in which case the application should perform the OAuth flow again to receive a new token. You can differentiate this 401 Unauthorized from other cases where the user simply does not have permission to access the resource by checking that the WWW-Authenticate header is set.

    https://canvas.instructure.com/doc/api/file.oauth.html#storing-access-tokens
    """


class JSONDecodeError(APIError, json.JSONDecodeError):
    """
    Exception raised when an API request responded with data being an invalid JSON document,
    especially when HTTPError is not raised.
    """
    __init__ = json.JSONDecodeError.__init__
