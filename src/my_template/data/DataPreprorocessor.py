from my_template.abc_interfaces.data_interfaces import BaseDataPreprocessor


class DataPreprocessor(BaseDataProcessor):
    def __init__(self) -> None:
        pass

    def _load_data(self, config: dict) -> None:
        """
        Load data from the specified path.
        """
        # Implement loading logic here
        pass
