import os
import requests

from settings import REPORT, BASE_FILTER, DATE_FROM, DATE_TO, MONTH_NAME, WEBHOOK
from user import get_managers



url = WEBHOOK + "crm.deal.list"


# --- Получаем менеджеров "на лету" ---
print("Загружаем менеджеров из Bitrix24...")
managers = get_managers()
print(f"Найдено менеджеров: {len(managers)}")


def get_count(params: dict, mode: str) -> int:
    response = requests.get(url, params=params)
    data = response.json()
    if mode == "total":
        return data.get("total", 0)
    return len(data.get("result", []))


def build_params(extra_filter: dict) -> dict:
    params = {**BASE_FILTER, **extra_filter}
    params["select[]"] = ["ID"]
    return params


# --- Собираем результаты ---
results = {
    "period": f"{DATE_FROM[:10]} — {DATE_TO[:10]}",
    "metrics": {},
    "managers": [m["NAME"] for m in managers],
}

for report_name, config in REPORT.items():
    metric = {"ИТОГО": 0, "по_менеджерам": {}}

    if not config["by_manager"]:
        metric["ИТОГО"] = get_count(build_params(config["params"]), config["count"])
    else:
        total = 0
        for manager in managers:
            params = {**config["params"], "filter[ASSIGNED_BY_ID]": manager["ID"]}
            count = get_count(build_params(params), config["count"])
            metric["по_менеджерам"][manager["NAME"]] = count
            total += count
        metric["ИТОГО"] = total

    results["metrics"][report_name] = metric
    print(f"  ✓ {report_name}: {metric['ИТОГО']}")


# --- Генерируем Excel ---
from excel_report import generate_excel
output = f"Алексей - Отчет за {MONTH_NAME}.xlsx"
generate_excel(results, output_path=output)
print("Готово.")