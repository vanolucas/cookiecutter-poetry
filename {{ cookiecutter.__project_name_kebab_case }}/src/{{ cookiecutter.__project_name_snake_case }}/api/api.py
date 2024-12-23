"""{{ cookiecutter.project_name }} API."""

import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

import coloredlogs
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from {{ cookiecutter.__project_name_snake_case }}.api.request import EchoRequest
from {{ cookiecutter.__project_name_snake_case }}.api.response import EchoResponse

API_TITLE = "{{ cookiecutter.project_name }} API"
ROUTES_PREFIX = "/api/v1"


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Handle FastAPI startup and shutdown events."""
    # Startup events:
    # - Remove all handlers associated with the root logger object.
    for handler in logging.root.handlers:
        logging.root.removeHandler(handler)
    # - Add coloredlogs' colored StreamHandler to the root logger.
    coloredlogs.install()
    yield
    # Shutdown events.


# FastAPI app.
app = FastAPI(title=API_TITLE, lifespan=lifespan)
router = APIRouter()

# CORS middleware settings.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins
    allow_credentials=True,  # Allow cookies and authentication
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


# Endpoint: echo.
@app.post("/echo")
async def echo_endpoint(request: EchoRequest) -> EchoResponse:
    """Echo the provided message."""
    return EchoResponse(message=request.message)


# Uvicorn entry point so that we can also just run this file to serve the API.
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
