# my_template/abc_interfaces/data_interfaces.py

"""Module for abstract base classes for data interfaces in the my_template package."""
from abc import ABC, abstractmethod


class BaseDataset(ABC):
    """
    Abstract base class for datasets in the my_template package.
    This class defines the interface for datasets used in machine learning tasks.
    Subclasses should implement the `__len__` and `__getitem__` methods.
    Attributes:
        data: The data contained in the dataset.
    Methods:
        __len__: Return the length of the dataset.
        __getitem__: Return a single data item from the dataset.
    Args:
        data: The data contained in the dataset.
    """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self, index: int):
        pass

    @abstractmethod
    def _set_config(self, config):
        """
        Set the configuration for the dataset.

        Args:
            config: Configuration object containing dataset parameters.
        """


class BaseDataProcessor(ABC):
    """
    Abstract base class for data processors in the my_template package.
    This class defines the interface for processing data.
    Subclasses should implement the `process_data` method.
    Attributes:
        None
    Methods:
        process_data: Process the data.
    Args:
        None
    """

    def __init__(self):
        pass

    @abstractmethod
    def process_data(self, data):
        """
        Process the data.

        Args:
            data: The data to be processed.

        Returns:
            Processed data.
        """

    @abstractmethod
    def save_processed_data(self, processed_data, save_path):
        """
        Save the processed data to a specified path.

        Args:
            processed_data: The data that has been processed.
            save_path: The path where the processed data should be saved.
        """

    @abstractmethod
    def _set_config(self, config):
        """
        Set the configuration for the data processor.

        Args:
            config: Configuration object containing data processing parameters.
        """
