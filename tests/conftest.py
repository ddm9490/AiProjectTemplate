# my_template/tests/conftest.py

"""Module for pytest fixtures for the my_template package."""

import pytest

from my_template.utils import UtilityManager, ConfigurationManager

# from my_template.data import DataLoader, DataProcessor, DataVisualizer, Dataset
# from my_template.training import Evaluator, Trainer, TrainVisualizer, \
# PipeLine, Tuner, ExperimentManager
# from my_template.models import Model


@pytest.fixture
def test_utility_manager() -> UtilityManager:
    """
    Fixture for the UtilityManager instance.

    Returns:
        UtilityManager: An instance of UtilityManager.
    """

    instance = UtilityManager()
    return instance


@pytest.fixture
def test_configuration_manager(utility_manager: UtilityManager) -> ConfigurationManager:
    """
    Fixture for the ConfigurationManager instance.

    Args:
        utility_manager (UtilityManager): An instance of UtilityManager.

    Returns:
        ConfigurationManager: An instance of ConfigurationManager.
    """

    instance = ConfigurationManager()
    return instance
