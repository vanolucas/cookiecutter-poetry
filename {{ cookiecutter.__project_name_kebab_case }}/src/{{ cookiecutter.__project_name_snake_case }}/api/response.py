"""{{ cookiecutter.project_name }} API responses."""

from pydantic import BaseModel


class EchoResponse(BaseModel):
    """Echo response.

    A response of the /echo endpoint.
    """

    message: str
