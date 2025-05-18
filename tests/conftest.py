import pytest

from src.my_template.data import *
from src.my_template.training import *
from src.my_template.utils import *
from src.my_template.models import *


@pytest.fixture
def test_utility_manager() -> UtilityManager:
    instance = UtilityManager()
    return instance

@pytest.fixture
def test_configuration_manager(test_utility_manager) -> ConfigurationManager:
    instance = ConfigurationManager(
        config_path = test_utility_manager.config_path
    )
    return instance
