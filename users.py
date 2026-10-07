import requests
from settings import WEBHOOK, POSITION_OKK, POSITION_MANAGER


def _fetch_users() -> list[dict]:
    """Забирает всех активных пользователей."""
    url = WEBHOOK + "user.get"
    params = {
        "select[]": ["ID", "NAME", "LAST_NAME", "WORK_POSITION"],
        "filter[ACTIVE]": True,
    }
    response = requests.get(url, params=params)
    return response.json().get("result", [])


def _filter_by_position(users: list[dict], keyword: str) -> list[dict]:
    """Оставляет только тех, у кого должность содержит keyword."""
    result = []
    keyword = keyword.lower()
    for user in users:
        position = (user.get("WORK_POSITION") or "").lower()
        if keyword in position:
            result.append({
                "ID": user["ID"],
                "NAME": f"{user['NAME']} {user['LAST_NAME']}".strip(),
                "WORK_POSITION": user.get("WORK_POSITION") or "",
            })
    return result


def get_okk() -> list[dict]:
    """Возвращает список ОКК (колл-центр)."""
    return _filter_by_position(_fetch_users(), POSITION_OKK)


def get_managers() -> list[dict]:
    """Возвращает список менеджеров по работе с клиентами."""
    return _filter_by_position(_fetch_users(), POSITION_MANAGER)


# Если запускаешь файл напрямую — покажет оба списка
if __name__ == "__main__":
    print("=== ОКК ===")
    for u in get_okk():
        print(f"  ID: {u['ID']:>6} | {u['NAME']:>30} | {u['WORK_POSITION']}")

    print("\n=== Менеджеры ===")
    for u in get_managers():
        print(f"  ID: {u['ID']:>6} | {u['NAME']:>30} | {u['WORK_POSITION']}")