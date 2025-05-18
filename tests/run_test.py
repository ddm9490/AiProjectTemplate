
import pytest

def run_all_test() -> None:
    pytest.main(["tests"])

def run_unit_test() -> None:
    pytest.main(["tests/unit"])

def run_integration_test() -> None:
    pytest.main(["tests/integration"])
if __name__ == "__main__":
    run_test()