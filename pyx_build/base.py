from pyx_build.dsl import repository
import os
import platform

class PyxBaseBuildScript:

    _repositories = list()
    
    def repositories(self):
        self.add_repository(repository("https://pypi.org", "pypi", True))
        os.mkdir("local_project_cache/repositories")

        for repository in self._repositories:
            for element in repository:
                with open(f"local_project_cache/repositories/{element}") as repo:
                    repo.write(repository[element])

    def add_repositories(self, repository_list):
        for repo_dict in repository_list:
            for element in repo_dict:
                self._repositories.append({element:repo_dict[element]})

    def build_distributed_executables():
        return True

    def build(build_distributed_executable):
        if build_distributed_executable:
            # TODO: Build native application using PyInstaller, Py2Exe and Py2App
            print(f"Building native application for {platform.system()}")
        else:
            # TODO: Build egg package
            print("Building egg package with namespace")

    def run():
        # Compile and run
        print("Compiling and running project")




        
        
