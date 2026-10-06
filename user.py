import os
import requests
from settings import WEBHOOK


def get_managers() -> list[dict]:
    """Возвращает список активных менеджеров по работе с клиентами."""
    url = WEBHOOK + "user.get"

    params = {
        "select[]": ["ID", "NAME", "LAST_NAME", "WORK_POSITION"],
        "filter[ACTIVE]": True,
    }

    response = requests.get(url, params=params)
    users = response.json().get("result", [])

    managers = []
    for user in users:
        position = (user.get("WORK_POSITION") or "").lower()
        if "менеджер по работе с клиентами" in position:
            managers.append({
                "ID": user["ID"],
                "NAME": f"{user['NAME']} {user['LAST_NAME']}".strip(),
            })

    return managers


# Если запускаешь файл напрямую — покажет список (удобно для отладки)
if __name__ == "__main__":
    managers = get_managers()
    print(f"Найдено менеджеров: {len(managers)}")
    for m in managers:
        print(f"  ID: {m['ID']:>6} | {m['NAME']}")