#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Define the CloudEndure module setup.

Note: To use the 'upload' functionality of this file, you must:

`$ pipenv install twine --dev`

"""

import io
import os
import sys
from shutil import rmtree
from typing import Dict, List

from setuptools import Command, find_packages, setup

# Package meta-data.
NAME: str = "cloudendure"
DESCRIPTION: str = "CloudEndure Python Client and CLI"
URL: str = "https://github.com/2ndWatch/cloudendure-python"
EMAIL: str = "mbeacom@2ndwatch.com, twarnock@2ndwatch.com"
AUTHOR: str = "Mark Beacom, Tom Warnock"
REQUIRES_PYTHON: str = ">=3.7.0"
VERSION: str = "0.1.2"

REQUIRED: List[str] = ["requests", "boto3", "fire"]
EXTRAS: Dict[str, List[str]] = {
    "test": [
        "coverage",
        "isort",
        "pytest",
        "pytest-cov",
        "pytest-isort",
        "pytest-sugar",
        "black",
        "pydocstyle",
        "pycodestyle",
        "bandit",
        "mypy",
        "twine",
        "moto",
    ]
}

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description: str = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.

about: Dict[str, str] = {}
if not VERSION:
    project_slug: str = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION


class UploadCommand(Command):
    """Support setup.py upload."""

    description: str = "Build and publish the package."
    user_options: List[str] = []

    @staticmethod
    def status(s):
        """Print things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel distribution…")
        sys_exec: str = sys.executable
        os.system(f"{sys_exec} setup.py sdist bdist_wheel")

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")
        sys.exit()


# Where the magic happens:
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    entry_points={
        "console_scripts": [
            "cloudendure=cloudendure.cloudendure:main",
            "ce=cloudendure.cloudendure:main",
        ]
    },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: MacOS :: MacOS 9",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft",
        "Operating System :: Microsoft :: MS-DOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows 8.1",
        "Operating System :: Microsoft :: Windows :: Windows 8",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Session",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Utilities",
    ],
    # $ setup.py publish support.
    cmdclass={"upload": UploadCommand},
)
