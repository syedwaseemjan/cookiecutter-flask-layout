"""Reject names that would break the generated Python package or TOML."""

import re
import sys

PACKAGE_RE = re.compile(r"^[a-z][a-z0-9_]*$")
SLUG_RE = re.compile(r"^[a-z][a-z0-9]+(?:-[a-z0-9]+)*$")
RESERVED = {"flask", "tests", "migrations", "app", "config"}


def reject_unsafe(label, value):
    if any(char in value for char in '"\n\r\\'):
        print(f"ERROR: {label} cannot contain quotes, backslashes, or newlines.")
        sys.exit(1)


package_name = "{{ cookiecutter.package_name }}"
project_slug = "{{ cookiecutter.project_slug }}"

reject_unsafe("full_name", "{{ cookiecutter.full_name }}")
reject_unsafe("email", "{{ cookiecutter.email }}")
reject_unsafe("project_name", "{{ cookiecutter.project_name }}")
reject_unsafe("project_short_description", "{{ cookiecutter.project_short_description }}")
reject_unsafe("package_name", package_name)
reject_unsafe("project_slug", project_slug)

if not PACKAGE_RE.fullmatch(package_name) or package_name in RESERVED:
    print(
        f"ERROR: {package_name!r} is not a usable Python package name. "
        "Use a short lowercase name such as flaskapp."
    )
    sys.exit(1)

if not SLUG_RE.fullmatch(project_slug):
    print(
        f"ERROR: {project_slug!r} is not a valid project slug. "
        "Use lowercase words separated by single hyphens."
    )
    sys.exit(1)

if "{{ cookiecutter.python_version }}" not in {"3.12", "3.13"}:
    print("ERROR: python_version must be 3.12 or 3.13.")
    sys.exit(1)
