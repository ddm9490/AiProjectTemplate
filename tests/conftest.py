import pytest

# from src.my_template.data import DataLoader, DataPreprocessor,
# from DataVisualizer, Dataset
# from src.my_template.training import Evaluator, Trainer, TrainVisualizer
# from src.my_template.training import PipeLine, Tuner, ExperimentManager
from src.my_template.utils import UtilityManager, ConfigurationManager
# from src.my_template.models import Model


@pytest.fixture
def test_utility_manager() -> UtilityManager:
    instance = UtilityManager()
    return instance


@pytest.fixture
def test_configuration_manager(test_utility_manager) -> ConfigurationManager:
    instance = ConfigurationManager(
        config_path=test_utility_manager.config_path
    )
    return instance


