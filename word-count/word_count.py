import re
from typing import Dict

WORD_PATTERN = r"[a-z0-9]+(?:'[a-z0-9]+)?"


def count_words(sentence: str) -> Dict[str, int]:
    words = re.findall(WORD_PATTERN, sentence.lower())

    return {word: words.count(word) for word in set(words)}
