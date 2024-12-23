"""Test {{ cookiecutter.project_name }} API."""

import httpx
from fastapi.testclient import TestClient

from {{ cookiecutter.__project_name_snake_case }}.api.api import app
from {{ cookiecutter.__project_name_snake_case }}.api.request import EchoRequest
from {{ cookiecutter.__project_name_snake_case }}.api.response import EchoResponse

client = TestClient(app)


def test_echo_successful() -> None:
    """Test that echoing a message is successful."""
    message = "Sample message."
    payload = EchoRequest(message=message)

    response = client.post("/echo", json=payload.model_dump())

    assert httpx.codes.is_success(response.status_code)
    echo_response = EchoResponse(**response.json())
    assert echo_response.message == message
