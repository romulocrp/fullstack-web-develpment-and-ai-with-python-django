from distutils.core import setup
from setuptools import find_packages

setup(
        name="python-practice",
        version="0.0.1",
        description="Practice for python exercises on the course, starting a module to\
             add tests and create module to use the answers.",
        package_dir={
            "tests": "tests"
            }
        )