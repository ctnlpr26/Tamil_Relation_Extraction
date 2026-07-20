from typing import Dict, Any

class ReportGenerator:
    """
    Generates reports summarizing model performance.
    """
    
    def __init__(self):
        pass
        
    def generate_report(self, evaluation_results: Dict[str, Any], output_path: str) -> None:
        """
        Formats evaluation results and writes them to the output_path.
        """
        raise NotImplementedError("ReportGenerator.generate_report is not yet implemented.")
