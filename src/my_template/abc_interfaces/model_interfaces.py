from abc import ABC,abstractmethod
from torch import Tensor

class BaseModel(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def forward(self,data:Tensor) -> Tensor:
        pass
    