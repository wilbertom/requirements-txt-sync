import pytest

from functions_for_program import (
    requirements_used,
    verify_requirements,
    replace_requirements,
)


def test_requirements_used():
    with open("example.txt") as file:
        assert requirements_used(file) == {
            "influxdb": None,
            "requests": None,
            "sentry-sdk": None,
        }


def test_verify_requirements():
    assert verify_requirements({"Flask": "0.1.0"}, {"Flask": None}, "example.txt") == [
        "example.txt: Flask needs to be Flask==0.1.0"
    ]

    assert verify_requirements({}, {"Flask": None}, "example.txt") == [
        "example.txt: Flask should be uninstalled or added to root."
    ]


def test_replace_requirements():
    assert replace_requirements({"Flask": "0.1.0"}, {"Flask": "0.1.0"}) == [
        "Flask==0.1.0"
    ]
    assert replace_requirements({"Flask": "0.1.0"}, {"Flask": None}) == ["Flask==0.1.0"]
    assert replace_requirements(
        {"Flask": "0.1.0", "SQLAlchemy": "0.0.0"}, {"Flask": None, "SQLAlchemy": None}
    ) == ["Flask==0.1.0", "SQLAlchemy==0.0.0"]
    assert replace_requirements({"Flask": None}, {"Flask": "1.0.0"}) == ["Flask"]
