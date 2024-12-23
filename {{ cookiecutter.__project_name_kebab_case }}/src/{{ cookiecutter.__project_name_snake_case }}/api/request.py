"""{{ cookiecutter.project_name }} API requests."""

from pydantic import BaseModel


class EchoRequest(BaseModel):
    """Echo request.

    A request to the /echo endpoint.
    """

    message: str = "Hey!"
