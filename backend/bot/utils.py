import re
from typing import List


def split_message(text: str, max_length: int = 4096) -> List[str]:
    if len(text) <= max_length:
        return [text]

    return [text[i:i + max_length] for i in range(0, len(text), max_length)]


def parse_allowed_users_ids(id_str: str, delimiter: str = ",") -> List[int] | None:
    str_list = [v.strip() for v in id_str.split(delimiter)]
    id_list = []

    for v in str_list:
        try:
            id_list.append(int(v))
        except ValueError:
            pass

    if id_list:
        return id_list


def escape_markdown(text: str) -> str:
    return re.sub(r'([\\_*`\[\]()~>#+\-.!|])', r'\\\1', text)
