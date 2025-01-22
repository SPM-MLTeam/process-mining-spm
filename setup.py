from os import path
from platform import system

from typing import Iterable

from setuptools import setup

LIB_TITLE = "sberpm"
PATH_SEPARATOR = "\\" if system() == "Windows" else "/"
ROOT_PATH = path.abspath(path.dirname(__file__))

def get_readme_description() -> str:
    """
    Load README description
    """
    with open(path.join(f"{ROOT_PATH}{PATH_SEPARATOR}", "README.md"), encoding="utf-8") as f:
        description = f.read()

    return description

setup(
    name="sberpm",
    version="3.4.0",
    description="Library that is intended to operate with various process mining tasks.",
    long_description=get_readme_description(),
    long_description_content_type="text/markdown",
    author="Sberbank Process Mining Team",
    author_email="spm.ml.team@gmail.com",
    
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ]
)
