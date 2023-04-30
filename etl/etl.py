from typing import Dict, List


def transform(legacy_data: Dict[int, List[str]]) -> Dict[str, int]:
    return {
        letter.lower(): value
        for value, letters in legacy_data.items()
        for letter in letters
    }
