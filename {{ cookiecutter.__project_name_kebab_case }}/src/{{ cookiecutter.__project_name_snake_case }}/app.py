"""Streamlit app."""

from importlib.metadata import version

import streamlit as st

st.title(f"{{ cookiecutter.__project_name_kebab_case }} v{version('{{ cookiecutter.__project_name_kebab_case }}')}")
