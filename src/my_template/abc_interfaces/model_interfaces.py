# my_template/abc_interfaces/model_interfaces.py

"""Base model interface for PyTorch models."""

from abc import ABC,abstractmethod
from torch import Tensor
from torch.nn import Module

class BaseModel(Module, ABC):
    """
    Base interface for PyTorch models.
    This interface defines the basic structure for any model that will be implemented.
    It requires the implementation of a forward method that takes a Tensor as input
    and returns a Tensor as output.

    Attributes:
        None
    Methods:
        forward(data: Tensor) -> Tensor:
            Abstract method that must be implemented by subclasses.
            It defines the forward pass of the model, taking a Tensor as input
            and returning a Tensor as output.
    """

    def __init__(self):
        super().__init__()

    @abstractmethod
    def _build_specific_layers(self) -> None:
        """
        Abstract method to build specific layers of the model.
        This method should be implemented in subclasses to define the architecture
        of the model.
        """

    @abstractmethod
    def forward(self,data:Tensor) -> Tensor:
        """
        Abstract method for the forward pass of the model.
        Args:
            data (Tensor): Input data for the model.
        Returns:
            Tensor: Output of the model after processing the input data.
        
        """
    