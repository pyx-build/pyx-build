import os
import requests
import pyx_build
from pyx_build.dsl import NoRepositoriesFoundException

def get_list_of_repositories() -> list:
    repo_names = os.listdir("local_project_cache/repositories")
    repo_urls = list()
    for repository_name in repo_names:
        if repository_name == "inactive" and len(repo_names) == 1:
            raise NoRepositoriesFoundException("No repositories found for downloading dependencies. They're either down or unreachable.")
        elif repository_name == "inactive":
            continue
        with open(f"local_project_cache/repositories/{repository_name}", 'r') as repo:
            repo_urls.append(repo)

    return repo_urls 

def pull(dep_name, version):
    for repo in get_list_of_repositories():
        request = requests.get(f"https://{repo}/packages/source/{list(dep_name)[0]}/{dep_name}/{dep_name}-{version}.tar.gz")
        if request.ok:
            open(f"{pyx_build.project_path}/dependencies/{dep_name}-{version}.tar.gz", 'wb').write(request.content)
            break
    




    
