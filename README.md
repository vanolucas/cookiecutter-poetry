[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/vanolucas/cookiecutter-poetry)

# 🍪 Poetry Cookiecutter

A modern [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for scaffolding Python packages and apps.

## 🎁 Features

- 🧑‍💻 Quick and reproducible development environments with VS Code's [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers), PyCharm's [Docker Compose interpreter](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html#docker-compose-remote), and [GitHub Codespaces](https://github.com/features/codespaces)
- 🌈 Cross-platform support for Linux, macOS (Apple silicon and Intel), and Windows
- 🐚 Modern shell prompt with [Starship](https://github.com/starship/starship)
- 📦 Packaging and dependency management with [Poetry](https://github.com/python-poetry/poetry)
- 🚚 Installing from and publishing to private package repositories and [PyPI](https://pypi.org/)
- ⚡️ Task running with [Poe the Poet](https://github.com/nat-n/poethepoet)
- ✍️ Code formatting with [Ruff](https://github.com/charliermarsh/ruff)
- ✅ Code linting with [Pre-commit](https://pre-commit.com/), [Mypy](https://github.com/python/mypy), and [Ruff](https://github.com/charliermarsh/ruff)
- 🏷 Optionally follows the [Conventional Commits](https://www.conventionalcommits.org/) standard to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/) with [Commitizen](https://github.com/commitizen-tools/commitizen)
- 💌 Verified commits with [GPG](https://gnupg.org/)
- 🧪 Test coverage with [Coverage.py](https://github.com/nedbat/coveragepy)
- 🏗 Scaffolding updates with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and [Cruft](https://github.com/cruft/cruft)
- 🧰 Dependency updates with [Dependabot](https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/about-dependabot-version-updates)
- 🗄️ Option to deploy a [PostgreSQL](https://www.postgresql.org/) SQL database Docker container and the [Adminer](https://www.adminer.org/) Web interface to manage it.

## ✨ Using

### Creating a new Python project

To create a new Python project with this template:

1. Install the latest [Cruft](https://github.com/cruft/cruft) and [Cookiecutter](https://github.com/cookiecutter/cookiecutter) in your [Python environment](https://github.com/pyenv/pyenv-virtualenv) with:

   ```sh
   pip install --upgrade "cruft>=2.12.0" "cookiecutter>=2.1.1"
   ```

2. [Create a new repository](https://github.com/new) for your Python project, then clone it locally.
3. Run the following command in the parent directory of the cloned repository to apply the Poetry Cookiecutter template:

   ```sh
   cruft create -f https://github.com/vanolucas/cookiecutter-poetry
   ```

   <details>

   <summary>⚠️ If your repository name ≠ the project's slugified name</summary>

   If your repository name differs from your project's slugified name (see `project_name` in the [Template parameters](https://github.com/vanolucas/cookiecutter-poetry#-template-parameters) below), you will need to copy the scaffolded project into the repository with:

      ```sh
      cp -r {project-name}/ {repository-name}/
      ```

   </details>

### Updating your Python project

To update your Python project to the latest template version:

1. Update the project while verifying the existing template parameters and setting any new parameters, if there are any:

   ```sh
   cruft update --cookiecutter-input
   ```

2. If any of the file updates failed, resolve them by inspecting the corresponding `.rej` files.

## 🤓 Template parameters

| Parameter                                                                 | Description                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `project_type` <br> ["package", "app"]                                    | Whether the project is a publishable Python package or a deployable Python app.                                                                                                                                                                                                                                                     |
| `project_name` <br> "Spline Reticulator"                                  | The name of the project. Will be slugified to `snake_case` for importing and `kebab-case` for installing. For example, `My Package` will be `my_package` for importing and `my-package` for installing.                                                                                                                             |
| `project_description` <br> "A Python package that reticulates splines."   | A single-line description of the project.                                                                                                                                                                                                                                                                                           |
| `project_url` <br> "<https://github.com/user/spline-reticulator>"         | The URL to the project's repository.                                                                                                                                                                                                                                                                                                |
| `author_name` <br> "John Smith"                                           | The full name of the primary author of the project.                                                                                                                                                                                                                                                                                 |
| `author_email` <br> "<john@example.com>"                                  | The email address of the primary author of the project.                                                                                                                                                                                                                                                                             |
| `python_version` <br> "3.12"                                              | The minimum Python version that the project requires.                                                                                                                                                                                                                                                                               |
| `development_environment` <br> ["simple", "strict"]                       | Whether to configure the development environment with a focus on simplicity or with a focus on strictness. In strict mode, additional [Ruff rules](https://beta.ruff.rs/docs/rules/) are added, and tools such as [Mypy](https://github.com/python/mypy) and [Pytest](https://github.com/pytest-dev/pytest) are set to strict mode. |
| `with_conventional_commits` <br> ["0", "1"]                               | If "1", [Commitizen](https://github.com/commitizen-tools/commitizen) will verify that your commits follow the [Conventional Commits](https://www.conventionalcommits.org/) standard. In return, `cz bump` may be used to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/).   |
| `with_fastapi_api` <br> ["0", "1"]                                        | If "1", [FastAPI](https://github.com/tiangolo/fastapi) is added as a run time dependency, FastAPI API stubs and tests are added, a `poe api` command for serving the API is added.                                                                                                                                                  |
| `with_streamlit_app` <br> [false, true]                                        | If `true`, [Streamlit](https://streamlit.io/) is added as a run time dependency and a sample Streamlit app is created.                                                                                                                                                  |
| `with_typer_cli` <br> ["0", "1"]                                          | If "1", [Typer](https://github.com/tiangolo/typer) is added as a run time dependency, Typer CLI stubs and tests are added, the package itself is registered as a CLI.                                                                                                                                                               |
| `private_package_repository_name` <br> "Private Package Repository"       | Optional name of a private package repository to install packages from and publish this package to.                                                                                                                                                                                                                                 |
| `private_package_repository_url` <br> "<https://pypi.example.com/simple>" | Optional URL of a private package repository to install packages from and publish this package to. Make sure to include the `/simple` suffix. For instance, when using a GitLab Package Registry this value should be of the form `https://gitlab.com/api/v4/projects/` `{project_id}` `/packages/pypi/simple`.                     |
| `with_postgresql` <br> [false, true] | Enable a Docker container with PostgreSQL running. The PostgreSQL data will be stored in a Docker volume.                     |
| `postgresql_server` <br> "db" | PostgreSQL server name. (Only used if `with_postgresql` is `true`.)                     |
| `postgresql_user` <br> "db" | PostgreSQL admin username. (Only used if `with_postgresql` is `true`.)                     |
| `postgresql_password` <br> "db" | PostgreSQL admin user password. (Only used if `with_postgresql` is `true`.)                     |
| `postgresql_db_name` <br> "db" | Name of the database to create in the PostgreSQL server. (Only used if `with_postgresql` is `true`.)                     |
| `postgresql_forward_port` <br> "5432" | Port to expose the PostgreSQL server. (Only used if `with_postgresql` is `true`.)                     |
| `with_adminer` <br> [false, true] | Enable a Docker container with the Adminer SQL database management Web interface.                     |
| `adminer_forward_port` <br> "51003" | Port to expose the HTTP server for the Adminer database management Web interface. (Only used if `with_adminer` is `true`.)                     |
