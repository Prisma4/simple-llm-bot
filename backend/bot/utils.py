from typing import List


def split_message(text: str, max_length: int = 4096) -> List[str]:
    if len(text) <= max_length:
        return [text]

    return [text[i:i + max_length] for i in range(0, len(text), max_length)]
