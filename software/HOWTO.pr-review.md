# HOWTO review incoming contributions

This guide aims to document how to review incoming contributions to the software list. Contributions can take two forms: issues and pull requests (PRs). This document focuses on the latter.

We try to steer potential contributors to PRs over issues, because PRs guide contributors to make the change they like to see. Issues move this effort from contributor to maintainer, which scales poorly when the volume of contributions increases.


## Finding new pull requests

  1. navigate to the [list of open pull requests](https://github.com/NCSC-NL/log4shell/pulls)
  2. filter the list of open PRs
    -  add `-review:changes_requested` to the filter at the top of the screen to see only unreviewed PRs
  3. open a PR
  4. perform a review

## Reviewing a pull request

  1. Open a PR
     - claim the PR by clicking _assign yourself_ under *Assignees* on the right side. 
     - review the PR title. It should be something like _"Add <vendor/product name>"_ (instead of "Update README.md"). The title should tell you what the author intended to change. You'll need this during your review.
  2. Navigate to the *Files changed* tab of the interface. This where the bulk of your review work happens.
  3. Review which files have changes.
     - does the PR include files outside the `software/` directory? Navigate to the *Conversation* tab and add the _CTI_ label (right side of the screen). If there are no changes to `software/` this concludes your review. Otherwise proceed in the *Files changed* tab.
  4. Check changes to the main tables in `software/README.md` against the following criteria:

     - For each row added or modified

| Column              | Review criteria |
|---------------------|-----------------|
| Vendor              | MUST be correctly alphabetically sorted with respect to other rows. |
| Product             | MUST be correctly alphabetically sorted with respect to other rows. SHOULD NOT start with the vendor name |
| Version             | MUST relate to the `Status` column: if `Status` is _Vulnerable_ or _Workaround_, `Version` indicates vulnerable version(s). If `Status` is _Fix_, `Version` indicates the version(s) in which the fix was introduced (no ranges). |
| Status CVE-2021-XXX | MUST use a status value as listed in the table at the top of the document. Status _Fix_ requires a released `Version` that includes the fix, otherwise list it as _Workaround_. |
| Links               | MUST refer to a vendor statement as the source for the row. This can either be a hyperlink to the vendor's website (in markdown-format \[link text\]\(https://example.org/url\)) or a hyperlink to an (provided) file in the `software/vendor-statements/` directory. URLs are preferred. Be sure to check any included vendor-statement files for the absence of personal data. |

     - For each row deleted, check the `Vendor` and `Product` against the Pull request title. Sometimes authors make their changes against a stale copy of the list. Their PR then effectively reverts recent changes. If this happens, ask the author to either fix the deletions, or open a new PR based of a non-stale version.

  5. Communicate feedback using the green _Review changes_ button in the upper right corner.
     - Select the _Request changes_ radio button if changes are necessary after the previous step. Otherwise the default of _Comment_ is fine.
     - Be sure to thank the author of a PR for their contribution, no matter how small.
     - You can also provide feedback on specific lines, by clicking the *+* symbol next to the line numbers. This can be helpful to the author when reviewing large PRs.
  6. No review comments? Proceed to merge the contribution.
  7. If you requested changes, unassign yourself. This allows other maintainers to pick improvements by the author in your absence.

## Merging a pull request

  1. Open a PR
  2. Check the merge indicator near the bottom of the screen:
     - if it states _This branch has no conflicts with the base branch_, your merge will be simple
     - alternatively, you need to resolve a conflict.
  3. Merge use _Rebase and merge_ if you can (note that this button is a dropdown which remembers your last selection)
     - Alternatively, use _Squash and merge_ when the author of the PR used additional commits to improve their contribution. This is especially relevant when they redacted information, say by blurring personal data in a `software/vendor-statements/' screenshot.
