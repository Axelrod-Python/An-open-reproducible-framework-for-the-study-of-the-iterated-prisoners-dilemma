"""
A script to walk through all commits of a repository.

Works with `number_of_strategies.py` to get the number of strategies in the
library at each commit.
"""
from git import Repo
from tqdm import tqdm
import os
import subprocess


path_to_repo = "~/src/Axelrod"
repo = Repo(path_to_repo)

all_commits = [c for c in repo.iter_commits()]

git = repo.git


number_of_strategies = []
dates = []
git.checkout('master')

try:
    os.remove('data')
except OSError:
    pass

for c in tqdm(sorted(all_commits, key=lambda x:x.committed_date)):

    for rubbish in [".DS_Store",
                    "axelrod/.DS_Store",
                    "axelrod/tests/.DS_Store",
                    "axelrod/strategies/.DS_Store"]:  # Having to delete some files that were not in gitignore at the time of the commit
        try:
            os.remove(path_to_repo + rubbish)
        except OSError:
            pass

    git.checkout(c)

    try:
        subprocess.call(['python2', '-B', 'number_of_strategies.py',
            str(c.committed_date), c.hexsha, str(c.author)])
        dates.append(c.committed_date)

    except ImportError:
        pass

git.checkout('master')
