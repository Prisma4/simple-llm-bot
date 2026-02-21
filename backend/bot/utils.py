import base64
from io import BytesIO
from typing import List, Sequence

from aiogram.types import Message, PhotoSize


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


async def photos_to_base64(
    message: Message,
    photos: Sequence[PhotoSize] | None = None,
) -> list[str]:
    photos = photos or (message.photo or [])
    if not photos:
        return []

    result: list[str] = []

    for p in photos:
        tg_file = await message.bot.get_file(p.file_id)

        buf = BytesIO()
        await message.bot.download_file(tg_file.file_path, destination=buf)
        data = buf.getvalue()

        result.append(base64.b64encode(data).decode("utf-8"))

    return result


async def message_photo_to_base64(message: Message) -> str | None:
    photos = message.photo or []
    if not photos:
        return None
    return (await photos_to_base64(message, photos=[photos[-1]]))[0]
