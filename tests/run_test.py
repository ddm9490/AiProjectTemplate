# tests/run_test.py

"""Run all tests, unit tests, or integration tests using pytest."""

import pytest


def run_all_test() -> None:
    """Run all tests in the tests directory."""

    pytest.main(["tests"])


def run_unit_test() -> None:
    """Run only unit tests in the tests/unit directory."""

    pytest.main(["tests/unit"])


def run_integration_test() -> None:
    """Run only integration tests in the tests/integration directory."""

    pytest.main(["tests/integration"])


if __name__ == "__main__":
    run_all_test()
