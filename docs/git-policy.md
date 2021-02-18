# Project Git Policies
### Updated 2021-02-17

## Branching

The ATMOS project uses the trunk-based development model for branching. This means that branches should be kept close to `master` and should be constrained to single features, topics, or bugfixes.

Each user should create and checkout a new local branch whenever they wish to begin work on a new topic. Branch names should follow the grammar:

```bnf
<branch-name> = <username> "/" <feature> "-" <topic>
              | <username> "/" <feature>
```
*(i.e. username and feature name are required, topic is optional)*

For example:
`janedoe/main-menu` or `abc123/main-menu-delete-something-old`

In keeping with the trunk-based model, branches should be created **directly** from the most recent commit to `master`. Branches created from other branches should be avoided unless there is a strong justification.

When work on a topic has been completed, the user's local branch should then be pushed to the remote (Github) and the user should create a new Pull Request (see below).

## Committing

A good rule of thumb is to make a commit after doing 15 minutes of work. However, this is only a guideline, not a rule. It will make sense in many cases to commit more or less frequently.

Commit messages should be very **concise** - no paragraphs, just short, single-sentence summaries of the changes that were made. **No justification** is required in commit messages. Justification for changes should come in the Pull Request description.

## Pull Requests

A PR description should have at least one section: A **summary** of changes and the justifications for those changes. An **other notes** section containing further thoughts and considerations for future work can be helpful if the person making the PR has more to say about future work or other miscellaneous considerations related to the PR.

Assigning a PR to someone directly is not necessary but is good practice as it will encourage that person to take ownership of reviewing the proposed changes and then actually approving the merge.

