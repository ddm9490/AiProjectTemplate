from abc import ABC, abstractmethod


class BaseDataLoader(ABC):
    def __init__(self, config):
        self.set_config(config)
        self.load_data()

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def set_config(self):
        pass


class BaseDataset(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self):
        pass


class BaseDataProcessor(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def process_data(self, data):
        pass
