# src/preprocess.py
"""Text preprocessing utilities for resume and job description cleaning."""
import re

def clean_text(text: str) -> str:
    """
    Clean and normalize text by converting to lowercase, removing special characters,
    and normalizing whitespace.
    
    Args:
        text: Input text string
        
    Returns:
        Cleaned text string
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__}")
    
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()