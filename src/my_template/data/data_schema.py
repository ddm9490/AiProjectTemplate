# src/my_template/data/data_models.py
from pydantic import BaseModel, Field
from typing import Dict, Any, Literal
import torch

# Pydantic v2에서 torch.Tensor와 같은 임의 타입을 허용하는 일반적인 방법
# Pydantic v1의 Config 클래스 방식과 다름
# mypy 플러그인을 위해 Config 클래스도 유지


class Config:
    arbitrary_types_allowed = True


class ImageDataItem(BaseModel):
    """
    하나의 이미지 데이터 항목에 대한 Pydantic 스키마
    """

    image: torch.Tensor = Field(..., description="Image tensor (C, H, W)")
    label: torch.Tensor = Field(..., description="Label tensor (e.g., class ID)")
    image_id: str = Field(..., description="Unique ID for the image")
    metadata: Dict[str, Any] = Field(
        default_factory=dict, description="Optional additional metadata"
    )

    model_config = {"arbitrary_types_allowed": True}


class TextDataItem(BaseModel):
    """
    하나의 텍스트 데이터 항목에 대한 Pydantic 스키마
    """

    text: torch.Tensor = Field(..., description="Tokenized text tensor")
    sentiment: torch.Tensor = Field(..., description="Sentiment score tensor")
    text_id: str = Field(..., description="Unique ID for the text")
    language: Literal["en", "ko"] = "en"  # 특정 값으로 제한하는 예시
    metadata: Dict[str, Any] = Field(default_factory=dict)

    model_config = {"arbitrary_types_allowed": True}
