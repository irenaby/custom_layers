# -----------------------------------------------------------------------------
# Copyright 2024 Sony Semiconductor Israel, Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------------
from packaging.requirements import Requirement
from packaging.version import parse
from importlib import metadata


class InstalledVersionMismatch(Exception):
    pass


class PackageNotFound(Exception):
    pass


def check_pip_requirement(requirement_string: str):
    """
    Check if the package is installed and meets the pip-style requirement string.

    Args:
        requirement_string: pip-style requirement string

    Raises:
        if the package is not installed or doesn't meet the requirement
    """
    requirement = Requirement(requirement_string)
    try:
        installed_ver = metadata.version(requirement.name)
    except metadata.PackageNotFoundError:
        raise PackageNotFound(requirement.name)

    if parse(installed_ver) not in requirement.specifier:
        raise InstalledVersionMismatch(f'Required {requirement_string}, installed version {installed_ver}')
