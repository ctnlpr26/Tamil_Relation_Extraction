from typing import Any
from .model_interface import ModelInterface

class ModelLoader:
    """
    Factory class to load and return instances of supported models implementing ModelInterface.
    """
    
    @staticmethod
    def load(model_name: str, **kwargs: Any) -> ModelInterface:
        """
        Loads the specified model by name.
        
        Args:
            model_name: The name/identifier of the model to load.
            **kwargs: Additional configuration parameters for the model.
            
        Returns:
            An instance of ModelInterface.
        """
        raise NotImplementedError("ModelLoader.load is not yet implemented.")
