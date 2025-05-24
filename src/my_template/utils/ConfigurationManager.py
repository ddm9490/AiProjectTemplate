"""Utility class to manage configuration settings for the model, trainer, dataset, and data loader."""
# import os 
# import sys
import yaml
from .Config import ModelConfig, TrainerConfig, DatasetConfig, DataLoaderConfig

class ConfigurationManager:
    def __init__(self,config_path : str):
        self._config_path = config_path
        self._config = None
        self._model_config = None
        self._trainer_config = None
        self._dataset_config = None
        self._data_loader_config = None
    
    def _load_config(self):
        with open(self._config_path,"r",encoding = "utf-8") as f:
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
        return self._dataset_config
    
    @property
    def data_loader_config(self) -> DataLoaderConfig:
        return self._data_loader_config