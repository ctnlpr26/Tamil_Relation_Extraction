from typing import List, Dict, Any

def calculate_precision(tp: int, fp: int) -> float:
    """Calculates precision given true positives and false positives."""
    if tp + fp == 0:
        return 0.0
    return tp / (tp + fp)

def calculate_recall(tp: int, fn: int) -> float:
    """Calculates recall given true positives and false negatives."""
    if tp + fn == 0:
        return 0.0
    return tp / (tp + fn)

def calculate_f1(precision: float, recall: float) -> float:
    """Calculates F1 score given precision and recall."""
    if precision + recall == 0.0:
        return 0.0
    return 2 * (precision * recall) / (precision + recall)
