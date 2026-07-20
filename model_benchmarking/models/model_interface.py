from abc import ABC, abstractmethod
from typing import List, Dict, Any

class ModelInterface(ABC):
    """
    Abstract base class defining the interface for all models used in relation extraction benchmarking.
    """
    
    @abstractmethod
    def load_model(self) -> None:
        """Loads the model and tokenizer/weights."""
        pass
        
    @abstractmethod
    def extract_relations(self, text: str, entity_pairs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Extracts relations between given entity pairs in the text.
        
        Args:
            text: The input sentence/text.
            entity_pairs: List of dicts representing entity pairs to check, e.g., [{'entity1': '...', 'entity2': '...'}]
            
        Returns:
            List of dicts representing extracted relations, e.g., [{'entity1': '...', 'entity2': '...', 'relation': '...'}]
        """
        pass
