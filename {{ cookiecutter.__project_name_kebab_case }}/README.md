# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## ✨ Using

### Run the App

To run this {{ cookiecutter.project_name }} app, run:

```sh
./start.sh app prod
```

This is equivalent to running the following inside the dev container:

```sh
poe app
```

### Serve the API

To serve this {{ cookiecutter.project_name }} API, run:

```sh
./start.sh api prod
```

This is equivalent to running the following inside the dev container:

```sh
poe api
```

## 🛠 Contributing

### Requirements

1. Install [Docker](https://docs.docker.com/).
2. Install [VS Code](https://code.visualstudio.com/).
3. Install [Dev Containers VS Code extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

### Open the project

1. Open this directory in VS Code.
2. Run the VS Code command "_Dev Containers: Reopen in Container_" (<kbd>Ctrl/⌘</kbd> + <kbd>⇧</kbd> + <kbd>P</kbd> to search VS Code commands).

### Project dev commands

Useful Poetry commands that you can run inside the dev environment:

- `poe`: list available tasks to run on this project.
    - `poe lint`: perform all code checks.
    - `poe test`: run all Pytest unit tests.
- `poetry add {package}`: add a Python dependency (adds it to `pyproject.toml` and `poetry.lock`).
    - Add `--group dev` to install it as a dev-only dependency.
- `poetry update`: upgrade all dependencies to the latest version allowed by `pyproject.toml`.
- `poetry install`: resolve and install all dependencies.

Automated changelog with [Commitizen](https://github.com/commitizen-tools/commitizen):

- `cz bump`: bumps the project version, updates the `CHANGELOG.md` and creates a git tag.

### Update all dependencies

One-liner to update all dependencies and commit:

```sh
poetry update && poetry install && git commit -m "chore(deps): update" -- pyproject.toml poetry.lock
```

### Commit

- Commits must follow the [Conventional Commits](https://www.conventionalcommits.org/) standard.
- You can skip the commit hooks (that run the code checks) using `--no-verify`.
    - Example: `git commit -m "feat: some feature" --no-verify`
