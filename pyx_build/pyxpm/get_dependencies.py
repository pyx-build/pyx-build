import os
import pathlib
import requests
import pyx_build
import tarfile
from pyx_build.dsl import NoRepositoriesFoundException, DependencyNotFoundException


def get_list_of_repositories() -> list:
    repo_names = os.listdir("local_project_cache/repositories")
    repo_urls = list()
    for repository_name in repo_names:
        if repository_name == "inactive" and len(repo_names) == 1:
            raise NoRepositoriesFoundException("No repositories found for downloading dependencies. They're either down or unreachable.")
        elif repository_name == "inactive":
            continue
        with open(f"local_project_cache/repositories/{repository_name}", 'r') as repo:
            repo_urls.append(repo.read())

    return repo_urls 

def pull(dep_name, version):
    for repo in get_list_of_repositories():
        path = f"dependencies/{dep_name}-{version}"
        if pathlib.Path(path).is_dir():
            break

        print(f"Downloading {repo}/packages/source/{list(dep_name)[0]}/{dep_name}/{dep_name}-{version}.tar.gz")
        request = requests.get(f"{repo}/packages/source/{list(dep_name)[0]}/{dep_name}/{dep_name}-{version}.tar.gz", stream=True)

        if request.ok:
            with open(f"{pyx_build.project_path}/dependencies/{dep_name}-{version}.tar.gz", 'wb') as file:
                file.write(request.content)
                tarfile.TarFile.open(f"{pyx_build.project_path}/dependencies/{dep_name}-{version}.tar.gz").extractall(f"dependencies/")
                file.close()
                os.remove(f"dependencies/{dep_name}-{version}.tar.gz")
            break

        else:
            raise DependencyNotFoundException(f"The dependency {dep_name}-{version} was not found in any repository")


    





    
