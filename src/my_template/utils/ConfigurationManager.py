"""Utility class to manage configuration settings for the model, trainer, dataset, and data loader."""

from config.config_schema import ModelConfig, TrainingConfig, DataConfig, UtilityConfig, MainConfig
from typing import Optional
from omegaconf import DictConfig


class ConfigurationManager:
    def __init__(self, cfg_omega: DictConfig) -> None:
        self._main_config: MainConfig = MainConfig.model_validate(cfg_omega)

    @property
    def model_config(self) -> ModelConfig:
        return self._main_config.model

    @property
    def training_config(self) -> TrainingConfig:
        return self._main_config.training

    @property
    def data_config(self) -> DataConfig:
        return self._main_config.data

    @property
    def utility_config(self) -> UtilityConfig:
        return self._main_config.utility
