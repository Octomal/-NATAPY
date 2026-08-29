"""Public package interface for natapy."""

from .core import (
    Natapy,
    TextAnalyzer,
    extract_keywords,
    normalize,
    slugify,
    tokenize,
    to_camel_case,
    to_snake_case,
    word_frequency,
)

__all__ = [
    "Natapy",
    "TextAnalyzer",
    "extract_keywords",
    "normalize",
    "slugify",
    "tokenize",
    "to_camel_case",
    "to_snake_case",
    "word_frequency",
]

__version__ = "0.1.0"
