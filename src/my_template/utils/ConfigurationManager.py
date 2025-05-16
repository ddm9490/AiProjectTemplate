import yaml
import os
import sys
from .Config import *

class ConfigurationManager:
    def __init__(self,config_path : str):
        self._config_path = config_path
    
    def _load_config(self):
        pass
    
    @property
    def model_config(self)-> ModelConfig:
        pass

    @property
    def trainer_config(self) -> TrainerConfig:
        pass
    
    @property
    def dataset_config(self) -> DatasetConfig:
        pass
    
    @property
    def data_loader_config(self) -> DataLoaderConfig:
        pass