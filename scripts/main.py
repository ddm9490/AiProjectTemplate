import hydra
from omegaconf import DictConfig
import os
import sys


from my_template.utils.ConfigurationManager import ConfigurationManager


@hydra.main(config_path="config", config_name="config.yaml", version_base="1.3")
def main(cfg: DictConfig) -> None:
    """
    Hydra의 메인 엔트리 포인트입니다. 여기서 설정이 로드되고
    ConfigurationManager에게 전달됩니다.
    """
    # ⭐️ 로드된 DictConfig (cfg)를 ConfigurationManager에 전달
    config_manager = ConfigurationManager(cfg_omega=cfg)

    # ConfigurationManager를 통해 Pydantic 타입의 설정 객체들을 가져옵니다.
    main_cfg = config_manager.main_config
    model_cfg = config_manager.model_config
    training_cfg = config_manager.training_config
    data_cfg = config_manager.data_config
    utility_cfg = config_manager.utility_config
    print(f"Project Name: {main_cfg.project_name}")
    print(f"Model Name: {model_cfg.model_name}")
    print(f"Batch Size: {training_cfg.batch_size}")
    print(f"Dataset Path: {data_cfg.data_path}")
    print(f"Utility Log Level: {utility_cfg.logging_level}")


if __name__ == "__main__":
    main()
