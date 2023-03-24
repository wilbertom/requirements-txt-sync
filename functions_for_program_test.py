import pytest

from functions_for_program import requirements_used, verify_requirements


def test_requirements_used():
    with open("example.txt") as file:
        assert requirements_used(file) == {
            "flask": "2.7",
            "pyOpenSSL": "0.13.1",
            "python-dateutil": "1.5",
            "pytz": "2013.6",
            "scipy": "0.13.0b1",
            "virtualenv": None,
        }


def test_verify_requirements():
    assert verify_requirements({"Flask": "0.1.0"}, {"Flask": None}) == [
        "Flask needs to be 0.1.0"
    ]
    assert verify_requirements({"Flask": "0.0.0", "SQLAlchemy": "0.0.0"}, {}) == [
        "Flask is missing",
        "SQLAlchemy is missing",
    ]
    assert verify_requirements({"Flask": None}, {}) == ["Flask is missing"]
    assert verify_requirements({}, {"Flask": None}) == [
        "Flask should be uninstalled or added to root"
    ]
