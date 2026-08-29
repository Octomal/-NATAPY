# NATAPY

NATAPY is a compact Python utility package for common text-processing tasks such as normalization, tokenization, frequency analysis, and keyword extraction.

## Features

- Normalize whitespace and punctuation in text input
- Tokenize strings into clean word lists
- Count word frequencies, optionally ignoring common stopwords
- Extract keyword summaries from text content
- Convert identifiers between snake_case, camelCase, and slug forms

## Quick example

```python
from natapy import Natapy, extract_keywords, slugify

text = "Natural Language Processing is fun and practical."
print(Natapy(text).tokenize())
print(extract_keywords(text, limit=3))
print(slugify("Natural Language Processing"))
```

## Installation

```bash
python -m pip install .
```

## License

MIT
