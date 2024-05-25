import os

# Read Cookiecutter configuration.
project_name = "{{ cookiecutter.__project_name_snake_case }}"
development_environment = "{{ cookiecutter.development_environment }}"
with_fastapi_api = int("{{ cookiecutter.with_fastapi_api }}")
with_streamlit_app: bool = {{ cookiecutter.with_streamlit_app }}
with_typer_cli = int("{{ cookiecutter.with_typer_cli }}")
is_application = "{{ cookiecutter.project_type == 'app' }}" == "True"

# Remove py.typed and Dependabot if not in strict mode.
if development_environment != "strict":
    os.remove(f"src/{project_name}/py.typed")
    os.remove(".github/dependabot.yml")

# Remove FastAPI if not selected.
if not with_fastapi_api:
    os.remove(f"src/{project_name}/api.py")
    os.remove("tests/test_api.py")

# Remove Streamlit app if not selected.
if not with_streamlit_app:
    os.remove(f"src/{project_name}/app.py")

# Remove Typer if not selected.
if not with_typer_cli:
    os.remove(f"src/{project_name}/cli.py")
    os.remove("tests/test_cli.py")
