"""Core text-processing helpers for natapy."""

from __future__ import annotations

import re
from collections import Counter

STOPWORDS = {
    "a",
    "about",
    "above",
    "after",
    "again",
    "against",
    "all",
    "am",
    "an",
    "and",
    "any",
    "are",
    "as",
    "at",
    "be",
    "because",
    "been",
    "before",
    "being",
    "below",
    "between",
    "both",
    "but",
    "by",
    "can",
    "did",
    "do",
    "does",
    "doing",
    "down",
    "during",
    "each",
    "few",
    "for",
    "from",
    "further",
    "had",
    "has",
    "have",
    "having",
    "he",
    "her",
    "here",
    "hers",
    "herself",
    "him",
    "himself",
    "his",
    "how",
    "i",
    "if",
    "in",
    "into",
    "is",
    "it",
    "its",
    "itself",
    "just",
    "me",
    "more",
    "most",
    "my",
    "myself",
    "no",
    "nor",
    "not",
    "of",
    "off",
    "on",
    "once",
    "only",
    "or",
    "other",
    "our",
    "ours",
    "ourselves",
    "out",
    "over",
    "own",
    "same",
    "she",
    "should",
    "so",
    "some",
    "such",
    "than",
    "that",
    "the",
    "their",
    "theirs",
    "them",
    "themselves",
    "then",
    "there",
    "these",
    "they",
    "this",
    "those",
    "through",
    "to",
    "too",
    "under",
    "until",
    "up",
    "very",
    "was",
    "we",
    "were",
    "what",
    "when",
    "where",
    "which",
    "while",
    "who",
    "whom",
    "why",
    "will",
    "with",
    "you",
    "your",
    "yours",
    "yourself",
    "yourselves",
}


def normalize(text: str, *, lower: bool = True, collapse_whitespace: bool = True, strip_punctuation: bool = False) -> str:
    """Return a normalized version of a string."""
    if text is None:
        raise TypeError("text must not be None")
    value = str(text)
    if lower:
        value = value.lower()
    if collapse_whitespace:
        value = re.sub(r"\s+", " ", value).strip()
    if strip_punctuation:
        value = re.sub(r"[^\w\s]", " ", value)
        value = re.sub(r"\s+", " ", value).strip()
    return value


def tokenize(text: str, *, lower: bool = True, strip_punctuation: bool = True) -> list[str]:
    """Tokenize a string into non-empty word tokens."""
    normalized = normalize(text, lower=lower, collapse_whitespace=True, strip_punctuation=strip_punctuation)
    return normalized.split()


def _as_text(value: str) -> str:
    if value is None:
        raise TypeError("value must not be None")
    return str(value)


def word_frequency(text: str, *, lower: bool = True, exclude_stopwords: bool = False) -> dict[str, int]:
    """Count word occurrences in text."""
    words = tokenize(text, lower=lower, strip_punctuation=True)
    if exclude_stopwords:
        words = [word for word in words if word not in STOPWORDS]
    return dict(Counter(words))


def extract_keywords(text: str, *, limit: int = 5, exclude_stopwords: bool = True) -> list[str]:
    """Return the most frequent keywords in a text, preserving first-seen order within ties."""
    words = tokenize(text, lower=True, strip_punctuation=True)
    if exclude_stopwords:
        words = [word for word in words if word not in STOPWORDS]
    counts = Counter(words)
    order = {word: index for index, word in enumerate(words) if word in counts}
    return [
        word
        for word, _ in sorted(counts.items(), key=lambda item: (-item[1], order[item[0]]))[:limit]
    ]


def slugify(value: str) -> str:
    """Convert text into a kebab-case slug."""
    normalized = normalize(_as_text(value), lower=True, collapse_whitespace=True, strip_punctuation=True)
    return normalized.replace(" ", "-")


def to_snake_case(value: str) -> str:
    """Convert text to snake_case."""
    text = _as_text(value)
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", text)
    text = text.replace("-", "_").replace(" ", "_")
    text = re.sub(r"[^0-9A-Za-z_]", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text.lower()


def to_camel_case(value: str) -> str:
    """Convert snake_case or kebab-case text to camelCase."""
    snake_case = to_snake_case(_as_text(value))
    parts = [part for part in snake_case.split("_") if part]
    if not parts:
        return ""
    return parts[0] + "".join(part[:1].upper() + part[1:] for part in parts[1:])


class Natapy:
    """Simple text-analysis wrapper around the public natapy helpers."""

    def __init__(self, text: str):
        self.text = _as_text(text)

    def normalize(self, *, lower: bool = True, collapse_whitespace: bool = True, strip_punctuation: bool = False) -> str:
        return normalize(self.text, lower=lower, collapse_whitespace=collapse_whitespace, strip_punctuation=strip_punctuation)

    def tokenize(self, *, lower: bool = True, strip_punctuation: bool = True) -> list[str]:
        return tokenize(self.text, lower=lower, strip_punctuation=strip_punctuation)

    def word_frequency(self, *, lower: bool = True, exclude_stopwords: bool = False) -> dict[str, int]:
        return word_frequency(self.text, lower=lower, exclude_stopwords=exclude_stopwords)

    def keywords(self, *, limit: int = 5, exclude_stopwords: bool = True) -> list[str]:
        return extract_keywords(self.text, limit=limit, exclude_stopwords=exclude_stopwords)

    def __str__(self) -> str:
        return self.text

    def __repr__(self) -> str:
        return f"Natapy({self.text!r})"


class TextAnalyzer(Natapy):
    """Compatibility alias for a text analyzer object."""

    pass
