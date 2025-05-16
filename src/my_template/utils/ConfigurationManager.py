import yaml
import os
import sys
from .Config import *

class ConfigurationManager:
    def __init__(self,config_path : str):
        self._config_path = config_path
    
    def _load_config(self):
        with open(self._config_path,"r") as f:
            self._config = yaml.safe_load(f)
        
        self._model_config = ModelConfig()
        self._trainer_config = TrainerConfig()
        self._dataset_config = DatasetConfig()
        self._data_loader_config = DataLoaderConfig()
    
    @property
    def model_config(self)-> ModelConfig:
        return self._model_config

    @property
    def trainer_config(self) -> TrainerConfig:
        return self._trainer_config
    
    @property
    def dataset_config(self) -> DatasetConfig:
        return seld._dataset_config
    
    @property
    def data_loader_config(self) -> DataLoaderConfig:
        return self._data_loader_config