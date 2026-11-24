# Maintaining and releasing this Copier template

This guide is for maintainers of `eed_package_template`. The generated package
README is in `README.md.jinja`; this guide is template-maintainer documentation
and is excluded from generated repositories.

## CI workflow roles

- `template-ci.yml` runs in this repository. It renders a sample project and
  validates the generated project.
- `ci.yml.jinja` renders as `.github/workflows/ci.yml` in generated
  repositories. That workflow calls the reusable Ruff, pytest, and coverage
  workflows in
  [`eed_gha_workflows`](https://github.com/EED-Solutions/eed_gha_workflows).
- The generated workflow and the shared reusable workflows pin their
  dependencies to exact `eed_gha_workflows` release tags. Keep the references
  consistent when upgrading the shared workflow version.

## Releasing shared CI changes through the template

The shared workflow release and template release are separate versions.
Release candidates are used to validate the shared workflows through a
Copier-generated canary before publishing a stable shared-workflow tag.

1. Make changes to the actions and reusable workflows in
   `eed_gha_workflows`. Its own pull-request CI runs Ruff directly; it must not
   depend on a shared-workflow release tag that does not exist yet.
2. Merge the shared-workflow changes, wait for the `main` Ruff CI to pass, and
   create an immutable shared-workflow prerelease tag on that exact `main`
   commit, for example `1.0.0-rc.1`. Mark it as a prerelease on GitHub. Never
   move or reuse a published tag.
3. Create and push a feature branch in `eed_package_template`. Update the
   shared-workflow references in both `ci.yml.jinja` and `template-ci.yml` to
   the candidate tag. Keep the generated ruleset's required status-check
   names aligned with the generated CI jobs.
4. Run the template's Copier-validation workflow on the PR. In the dedicated
   `eed_gha_workflow_testing` repository, update from the pushed template
   branch:

   ```bash
   copier update --trust --vcs-ref <template-branch>
   ```

   Open a PR in the canary repository. Verify that generated Ruff, the pytest
   matrix, and coverage jobs all resolve and pass.
5. After the candidate passes, create the stable shared-workflow tag (for
   example, `1.0.0`) on the same commit as the successful candidate tag. Do
   not rename or move the prerelease tag. Update the template branch
   references from the candidate tag to the stable tag, then repeat the
   template and canary validation from that branch.
6. Once the stable shared-workflow reference passes in the canary, merge the
   template PR and wait for Copier-validation CI to pass on `main`.
7. Create a template prerelease tag on the tested template `main` commit, such
   as `<next-template-version>-rc.1` (for example, `0.2.0-rc.1`). In the
   canary repository, update from that exact template tag:

   ```bash
   copier update --trust --vcs-ref <template-prerelease-tag>
   ```

   Verify all generated CI jobs pass, merge the canary PR, and wait for CI on
   its `main` branch.
8. If the canary passes and the template source has not changed, create the
   final template tag (for example, `0.2.0`) on the same commit as the
   prerelease. Do not rename or move the prerelease tag. Update the canary to
   the final tag and verify it before broad rollout.
9. Update the remaining Copier-generated repositories from the final template
   tag. Use a PR for each repository and wait for its CI before merging.

If a canary check fails, fix the layer responsible and repeat the validation.
A fix to `eed_gha_workflows` requires a new candidate tag (for example,
`1.0.0-rc.2`) on the corrected commit and an updated template reference. A
template fix requires another template prerelease (for example,
`<next-template-version>-rc.2`). Do not overwrite an existing release or
prerelease tag.

## Related documentation

The shared actions, reusable workflow interfaces, and shared release policy
are documented in the
[`eed_gha_workflows` README](https://github.com/EED-Solutions/eed_gha_workflows#readme).
