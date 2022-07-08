import http.client
from os import stat
from tokenize import String

class RepositoryNotFoundException(Exception):

    _error_message = None

    def __init__(self, message, error):
        super().__init__(message)
        self._error_message = error

    def get_error(self):
        return self._error_message

    error = property(fget=get_error)


def repository(url, key, terminate_on_not_found = False) -> dict:
    request = http.client.HTTPConnection(url)
    request.request("HEAD", '')
    status = request.getresponse().status
    if status == 200:
        print(f"Repository {key} is available")
        return {key:url}
    elif terminate_on_not_found:
        print(f"Repository {key} is not available, status code {status}, skipping")
        return {key:None}
    else:
        exception = RepositoryNotFoundException(f"Repository {key} is not available and this repository has been marked as manadatory. Status {status}", f"No such URL, status {status}")
        print(exception.error)
        raise exception

