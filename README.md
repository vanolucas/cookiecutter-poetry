# 🍪 cookiecutter-poetry

A cookiecutter to quickly generate new VS Code **Python** and **FastAPI** projects with Poetry, MyPy, Ruff and other development tools ready to go.

## 🎁 Features

- 🧑‍💻 Quick and reproducible development environments with VS Code's [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers).
- 📦 Packaging and dependency management with [Poetry](https://github.com/python-poetry/poetry).
- ⚡️ Task running with [Poe the Poet](https://github.com/nat-n/poethepoet).
- ✍️ Code formatting with [Ruff](https://github.com/charliermarsh/ruff).
- ✅ Code linting with [Pre-commit](https://pre-commit.com/), [Mypy](https://github.com/python/mypy), and [Ruff](https://github.com/charliermarsh/ruff).
- 🏷 [Conventional Commits](https://www.conventionalcommits.org/) standard to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/) with [Commitizen](https://github.com/commitizen-tools/commitizen).
- 🧪 Test coverage with [Coverage.py](https://github.com/nedbat/coveragepy).
- 🗄️ Optionally deploy a [PostgreSQL](https://www.postgresql.org/) SQL database [Docker container](https://hub.docker.com/_/postgres) and the [Adminer](https://www.adminer.org/) Web interface to manage it.

## ✨ Usage

### Requirements

- [Docker](https://docs.docker.com/) Engine

### Generate a new project

To generate a new project directory inside the specified dir:

```sh
./generate-project.sh dir/where/project/dir/will/be/created
```

This will launch the cookiecutter project creation assistant in a Docker container. Follow its instructions to setup the project.

## 🤓 Template parameters

- `project_name`
- `project_description`
- `author_name`
- `author_email`
- `project_url`
- `python_version`
- `with_postgresql` [false, true]: whether or not to run a PostgreSQL database Docker container alongside the dev container. The PostgreSQL data will be stored in a Docker volume. The following parameters are only relevant when `with_postgresql` is `true`:
    - `postgresql_server`: name of the PostgreSQL service/container.
    - `postgresql_user`: name of the PostgreSQL admin user.
    - `postgresql_password`: password of the PostgreSQL admin user.
    - `postgresql_db_name`: name of the database to create in PostgreSQL.
    - `postgresql_forward_port`: host port to expose the PostgreSQL server on.
- `with_adminer` [false, true]: whether or not to run an Adminer container alongside the dev container. Provides a Web UI to manage the PostgreSQL database.
    - `adminer_forward_port`: host port to expose the Adminer web UI on (only relevant when `with_adminer` is `true`).

## 📥 Patch this template with changes from upstream repo

Add the upstream repo as a new remote:

```sh
git remote add "upstream" git@github.com:superlinear-ai/poetry-cookiecutter.git
```

Create a new branch where we will pull the latest upstream changes:

```sh
git checkout -b upstream-updates
```

Pull changes from the upstream repo to the current branch:

```sh
git pull --no-rebase upstream main
```

A merge conflict may occur. Resolve the conflict then commit to conclude the merge.

We can then open a pull request from the `upstream-updates` branch to `main`.
