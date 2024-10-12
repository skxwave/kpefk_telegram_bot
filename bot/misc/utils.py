import requests


async def group_exist(group: str | int) -> bool:
    lessons = requests.get(
        f"https://skxwave.pythonanywhere.com/api/v1/schedule/{group}"
    )
    return True if lessons else False
