from my_template.abc_interfaces.model_interfaces import BaseNeuralModel
import torch


class Model(BaseNeuralModel):
    def __init__(self) -> None:
        super().__init__()
        self._build_specific_layers()

    def _build_specific_layers(self) -> None:
        """
        Build specific layers of the model.
        This method should be implemented in subclasses to define the architecture
        of the model.
        """
        # Example: Define layers here
        # self.layer1 = nn.Linear(in_features, out_features)
        pass

    def forward(self, data: torch.Tensor) -> torch.Tensor:
        pass
