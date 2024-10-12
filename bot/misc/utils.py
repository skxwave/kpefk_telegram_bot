import requests


async def group_exist(group: str | int) -> bool:
    groups = requests.get(f"https://skxwave.pythonanywhere.com/api/v1/groups/")
    return True if group in groups.json()["result"] else False
