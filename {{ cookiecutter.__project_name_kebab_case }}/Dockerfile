# Args.
ARG PYTHON_VERSION={{ cookiecutter.python_version }}



# Base image.
FROM {{ cookiecutter.__docker_image }} AS base

# Remove docker-clean so we can keep the apt cache in Docker build cache.
RUN rm /etc/apt/apt.conf.d/docker-clean

# Configure Python to print tracebacks on crash [1], and to not buffer stdout and stderr [2].
# [1] https://docs.python.org/3/using/cmdline.html#envvar-PYTHONFAULTHANDLER
# [2] https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUNBUFFERED
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1

# Create a non-root user and switch to it [1].
# [1] https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user
ARG UID=1000
ARG GID=$UID
RUN groupadd --gid $GID user && \
    useradd --create-home --gid $GID --uid $UID user --no-log-init && \
    chown user /opt/
USER user

# Create and activate a Python virtual environment.
ENV VIRTUAL_ENV /opt/{{ cookiecutter.__project_name_kebab_case }}-env
ENV PATH $VIRTUAL_ENV/bin:$PATH
RUN python -m venv $VIRTUAL_ENV

# Set the working directory: our project's directory.
WORKDIR /workspaces/{{ cookiecutter.__project_name_kebab_case }}/



# Poetry image.
FROM base AS poetry

USER root

# Install Poetry in separate venv so it doesn't pollute the main venv.
ENV POETRY_VERSION 1.8
ENV POETRY_VIRTUAL_ENV /opt/poetry-env
RUN --mount=type=cache,target=/root/.cache/pip/ \
    python -m venv $POETRY_VIRTUAL_ENV && \
    $POETRY_VIRTUAL_ENV/bin/pip install poetry~=$POETRY_VERSION && \
    ln -s $POETRY_VIRTUAL_ENV/bin/poetry /usr/local/bin/poetry

# Install compilers that may be required for certain packages or platforms.
RUN --mount=type=cache,target=/var/cache/apt/ \
    --mount=type=cache,target=/var/lib/apt/ \
    apt-get update && \
    apt-get install --no-install-recommends --yes build-essential

USER user

# Install the run time Python dependencies in the virtual environment.
COPY --chown=user:user poetry.lock* pyproject.toml /workspaces/{{ cookiecutter.__project_name_kebab_case }}/
RUN mkdir -p /home/user/.cache/pypoetry/ && \
    mkdir -p /home/user/.config/pypoetry/ && \
    mkdir -p src/{{ cookiecutter.__project_name_snake_case }}/ && \
    touch src/{{ cookiecutter.__project_name_snake_case }}/__init__.py && \
    touch README.md
RUN --mount=type=cache,uid=$UID,gid=$GID,target=/home/user/.cache/pypoetry/ \
    poetry install --only main --all-extras --no-interaction



# Dev image.
FROM poetry AS dev

# Install development tools: curl, nano, git, gpg, ssh, starship, sudo.
USER root
RUN --mount=type=cache,target=/var/cache/apt/ \
    --mount=type=cache,target=/var/lib/apt/ \
    apt-get update && \
    apt-get install --no-install-recommends --yes curl nano git gnupg ssh sudo && \
    sh -c "$(curl -fsSL https://starship.rs/install.sh)" -- "--yes" && \
    echo 'user ALL=(root) NOPASSWD:ALL' > /etc/sudoers.d/user && chmod 0440 /etc/sudoers.d/user
RUN git config --system --add safe.directory '*'
USER user

# Install the development Python dependencies in the virtual environment.
RUN --mount=type=cache,uid=$UID,gid=$GID,target=/home/user/.cache/pypoetry/ \
    poetry install --all-extras --no-interaction

# Setup git pre-commit hook.
COPY --chown=user:user .pre-commit-config.yaml /workspaces/{{ cookiecutter.__project_name_kebab_case }}/
RUN mkdir -p /opt/build/poetry/ && cp poetry.lock /opt/build/poetry/ && \
    git init && pre-commit install --install-hooks && \
    mkdir -p /opt/build/git/ && cp .git/hooks/commit-msg .git/hooks/pre-commit /opt/build/git/

# Configure the non-root user's shell with Starship prompt.
RUN echo 'eval "$(starship init bash)"' >> ~/.bashrc && \
    starship preset no-nerd-font -o ~/.config/starship.toml && \
    bash -c 'source ~/.bashrc'



# API image.
FROM base AS api

# Copy the virtual environment from the poetry stage.
COPY --from=poetry $VIRTUAL_ENV $VIRTUAL_ENV

# Copy the API source code to the working directory.
COPY --chown=user:user . .

# Expose the API.
ENTRYPOINT ["/opt/{{ cookiecutter.__project_name_kebab_case }}-env/bin/poe"]
CMD ["api"]
