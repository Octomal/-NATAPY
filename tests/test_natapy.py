from natapy import (
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


def test_normalize_and_tokenize() -> None:
    text = "  Hello, WORLD!  hello  "
    assert normalize(text) == "hello, world! hello"
    assert tokenize(text) == ["hello", "world", "hello"]


def test_word_frequency_and_keywords() -> None:
    text = "Python is great, and Python is fast. Great performance matters."
    assert word_frequency(text, exclude_stopwords=True) == {
        "python": 2,
        "great": 2,
        "fast": 1,
        "performance": 1,
        "matters": 1,
    }
    assert extract_keywords(text, limit=3) == ["python", "great", "fast"]


def test_case_conversions() -> None:
    assert to_snake_case("NaturalLanguageParser") == "natural_language_parser"
    assert to_snake_case("natural-language parser") == "natural_language_parser"
    assert to_camel_case("natural_language_parser") == "naturalLanguageParser"
    assert slugify("Natural Language Parser!") == "natural-language-parser"


def test_natapy_object() -> None:
    analyzer = Natapy("Natural language processing is fun.")
    assert analyzer.normalize() == "natural language processing is fun."
    assert analyzer.tokenize() == ["natural", "language", "processing", "is", "fun"]
    assert analyzer.keywords(limit=2) == ["natural", "language"]

    alias = TextAnalyzer("Summary of important terms")
    assert alias.word_frequency(exclude_stopwords=True)["important"] == 1
