# eed_package_template

## Creating a New Repository from This Template

1. In the EED-Solutions organization, create a new repository using this template and assign it a new name, such as `eed_my_new_package`.
2. Create a new branch (e.g., `repo_configuration`).
3. Delete the `uv.lock` file.
4. Update `project.toml` by renaming `eed-package-template` to your new package name (e.g., `eed-my-new-package`).
5. Set up a virtual environment using `uv`.
6. Install pre-commit hooks.
7. Add a note indicating the commit ID from which this repository was created, for example:
   ```
   - created from this template: https://github.com/EED-Solutions/eed_package_template/releases/tag/0.1.0
   ```
8. Rename the directory `src/eed_package_template` to match your new package name (e.g., `src/eed_my_new_package`).
9. Use VS Code's find and replace feature to update all instances of `eed_package_template` with your new package name.
10. Commit all changes, create a pull request, and ensure all CI pipelines pass.
11. Update repository settings as needed (e.g., import branch/tag rulesets, general settings). For more information, see [this guide](https://eed-solutions.atlassian.net/wiki/x/BIA8Mw) (private access). Rulesets are documented under ``.github\rulesets`` and can be imported.
12. Merge the pull request and create the initial release (e.g., `0.1.0`).

## Github actions

Workflows are centraly hosted in EED_Solutions/eed_gha_workflows.
Please check for more details here.

## Other

Test EED85-machine
