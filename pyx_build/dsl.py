import requests
import pathlib
import os


class NoRepositoriesFoundException(Exception):

    def __init__(self, message):
        super().__init__(message)

class RepositoryNotFoundException(Exception):

    _error_message = None

    def __init__(self, message, error):
        super().__init__(message)
        self._error_message = error

    def get_error(self):
        return self._error_message

    error = property(fget=get_error)


def repository(url, key, terminate_on_not_found = False) -> dict:
    status = requests.get(url).status_code
    if pathlib.Path("local_project_cache/repositories").is_dir() == False:
        os.mkdir("local_project_cache")
        os.mkdir('local_project_cache/repositories')
        os.mkdir('local_project_cache/repositories/inactive')
    if status == 200:
        print(f"Repository {key} is available")
        open(f"local_project_cache/repositories/{key}", 'w').write(url)
    elif terminate_on_not_found == False:
        print(f"Repository {key} is not available, status code {status}, skipping")
        open(f"local_project_cache/repositories/inactive/{key}", 'w').write(url)        
    else:
        exception = RepositoryNotFoundException(f"Repository {key} is not available and this repository has been marked as manadatory. Status {status}", f"No such URL, status {status}")
        print(exception.error)
        raise exception

