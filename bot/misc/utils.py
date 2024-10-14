import requests

from core import db_helper


async def group_exist(group: str | int) -> bool:
    groups = requests.get(f"https://skxwave.pythonanywhere.com/api/v1/groups/")
    return True if group in groups.json()["result"] else False


async def send_user_info(telegram_id: int):
    user = await db_helper.find_user(telegram_id)
    result = f"Вибрана група: `{user.group}`"
    return result
