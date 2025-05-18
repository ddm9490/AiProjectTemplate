from ....src.my_template.utils import UtilityManager
import pytest

@pytest.fixture
def my_test_instance() -> UtilityManager:
  instance = UtilityManager()
  return instance

def test_set_seed(my_test_instance) -> None:
  my_test_instance.set_seed(42)

def test_root_path(my_test_instance) -> None:
  print(my_test_instance.root_path)

def test_config_path(my_test_instance) -> None:
  print(my_test_instance.config_path)
