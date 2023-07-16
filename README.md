# Respiratory panel

Surveillance panel of viral reference sequences

## Contents

- `references` - contains reference fasta sequences
- `metadata.csv` - contains `curated` names for reference fasta sequences
- `nextclade_mapping.csv` - contains mapping of reference names and its segments onto nextclade tags

## Development

First, clone the repository:

```sh
git clone git@github.com:xsitarcik/respiratory_panel.git
```

Create your new branch, i.e. to add a new reference:

```sh
git checkout -b 'feat/new_reference'
```

Make some changes, add them and commit them with a appropriate commit message:

```sh
git add .
git commit -m 'feat: added a new reference XY'
git push --set-upstream origin feat/new_reference
```

At last, create a pull request and wait for approval.

Commit messages and PR names must follow [Conventional Commits spec](https://www.conventionalcommits.org/en/v1.0.0/). This is used for automatic versioning using [Semantic Versioning](https://semver.org/) and changelog creation.
