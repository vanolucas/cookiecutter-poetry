"""{{ cookiecutter.project_name }} App Main."""

import logging

# Initialize this module's logger.
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def main() -> None:
    """Run the {{ cookiecutter.project_name }} App."""
    logger.info("{{ cookiecutter.project_name }} App [start]")
    logger.info("{{ cookiecutter.project_name }} App [stop]")


if __name__ == "__main__":
    main()
