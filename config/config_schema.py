# config/config_schema.py
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any


class TrainingConfig(BaseModel):
    epochs: int = 10
    batch_size: int = 32
    learning_rate: float = 0.001
    optimizer: str = "Adam"
    loss_function: str = "CrossEntropyLoss"
    callbacks: List[str] = []  # Callback 이름 목록


class DataConfig(BaseModel):
    dataset_name: str = "ImageNet"
    data_path: str = "data/raw/"
    num_workers: int = 4
    transformations: List[str] = []  # 트랜스포메이션 이름 목록


class ModelConfig(BaseModel):
    model_name: str = "ResNet18"
    num_classes: int = 1000
    pretrained: bool = True
    embedding_dim: Optional[int] = None


class UtilityConfig(BaseModel):
    device: str = "auto"  # "cpu", "cuda", "auto"
    seed: int = 42
    logging: bool = True
    logging_level: str = "INFO"
    save_model: bool = True
    save_path: str = "checkpoints/"
    checkpoint_frequency: int = 5  # 에폭마다 체크포인트 저장 빈도


class MainConfig(BaseModel):
    # 메인 설정 스키마
    project_name: str = "MyMLProject"

    training: TrainingConfig = Field(default_factory=TrainingConfig)
    data: DataConfig = Field(default_factory=DataConfig)
    model: ModelConfig = Field(default_factory=ModelConfig)
    utility: UtilityConfig = Field(default_factory=UtilityConfig)
    # 추가적인 섹션 (예: evaluation, inference 등)


# Hydra와 연동 시 MainConfig를 로드하여 사용
