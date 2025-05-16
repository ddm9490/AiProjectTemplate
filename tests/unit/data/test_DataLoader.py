from ...src.my_template.data import DataLoader
import pytest

@pytest.fixture
def my_dataloader_instance():
  instance = DataLoader()
  return instance