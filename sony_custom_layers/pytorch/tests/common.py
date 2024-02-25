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
import subprocess as sp
import sys


def get_git_repo_root():
    p = sp.run(['git', 'rev-parse', '--show-toplevel'], stdout=sp.PIPE, check=True, text=True)
    return p.stdout.strip()


def exec_in_clean_process(code: str, check: bool):
    gitroot = get_git_repo_root()
    command = f'{sys.executable} -c "{code}"'
    p = sp.run(command, shell=True, check=check, stdout=sp.PIPE, stderr=sp.PIPE, env={'PYTHONPATH': gitroot})
    return p
