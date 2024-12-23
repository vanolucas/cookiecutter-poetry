# Args.
ARG PYTHON_IMAGE_VARIANT=latest

# Base image.
FROM python:$PYTHON_IMAGE_VARIANT

ARG UID=1000
ARG GID=1000
ARG USERNAME=user

# Create user.
RUN groupadd --gid $GID $USERNAME
RUN useradd --uid $UID --gid $GID --create-home --shell /bin/bash $USERNAME
USER $USERNAME

# Set working directory.
WORKDIR /usr/src/app

# Install Python dependencies.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project template and generator script.
COPY . .

# Launch the project generation script.
CMD [ "./run-cookiecutter.sh" ]
