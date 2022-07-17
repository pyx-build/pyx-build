import pyx_build
import os
import platform

class PyxBaseBuildScript:

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




        
        
