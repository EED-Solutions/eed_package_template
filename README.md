# eed_package_template

## How to create a new Repo from that template

1. create a new repository in the EED-Solutions organisation using this template ang give it new name ``eed_my_new_package``.

2. create a new branch (e.g. ``repo_configuration``)


3. delete uv.lock file
4. update project.toml - rename ``eed-package-template`` to ``eed-my-new-package``
5. set up virtual environment using env
6. install pre-commits
7. add a note from wich commit id this repo was created.

e.g.:
``- created from this template: https://github.com/EED-Solutions/eed_package_template/releases/tag/0.1.0``
8. rename the ``src/eed_package_template`` to ``eed_my_new_package``.
9. use vscode to find and replace ``eed_package_template`` with ``eed_my_new_package``
10. commit all changes, create pr and check if all ci-pipelines are passing
11. update settings (e.g. import branch/tag rulesets, general ..), see https://eed-solutions.atlassian.net/wiki/x/BIA8Mw (privatge Access) for mor infos
11. merge and create a release 0.1.0


## other

test EED85-machine
