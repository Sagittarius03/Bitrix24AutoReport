import requests
from settings import WEBHOOK, DATE_FROM, DATE_TO, MONTH_NAME, BASE_FILTER
from users import get_okk, get_managers

from reports import okk as report_okk
from reports import managers as report_managers

from excel_report import generate_excel_cards, generate_excel_rows


DEAL_URL = WEBHOOK + "crm.deal.list"
LEAD_URL = WEBHOOK + "crm.lead.list"


def count(url: str, params: dict) -> int:
    """Отправляет запрос, возвращает total."""
    response = requests.get(url, params=params)
    data = response.json()
    return data.get("total", 0)


def build_params(extra: dict) -> dict:
    """Добавляет select[] к фильтру."""
    params = {**BASE_FILTER, **extra}
    params["select[]"] = ["ID"]
    return params


# ============================================================
# 1. ОТЧЁТЫ ОКК (карточки + таблица)
# ============================================================
def run_okk_reports():
    print("\n=== Отчёты ОКК ===")
    okk_users = get_okk()
    managers = get_managers()
    manager_names = [m["NAME"] for m in managers]

    for okk in okk_users:
        print(f"\n[{okk['NAME']}]")

        results = {
            "period": f"{DATE_FROM[:10]} — {DATE_TO[:10]}",
            "metrics": {},
            "managers": manager_names,
        }

        for metric_name, config in report_okk.REPORT.items():
            metric = {"ИТОГО": 0, "по_менеджерам": {}}

            for manager in managers:
                params = {
                    **config["params"],
                    "filter[ASSIGNED_BY_ID]": manager["ID"],
                    "filter[UF_CRM_1667463594]": okk["ID"],
                }
                c = count(DEAL_URL, build_params(params))
                metric["по_менеджерам"][manager["NAME"]] = c
                metric["ИТОГО"] += c

            results["metrics"][metric_name] = metric
            print(f"  ✓ {metric_name}: {metric['ИТОГО']}")

        filename = f"{okk['NAME']} - Отчет за {MONTH_NAME}.xlsx"
        generate_excel_cards(results, output_path=filename)


# ============================================================
# 2. ОТЧЁТЫ МЕНЕДЖЕРОВ (сделки + лиды в одном файле)
# ============================================================
def run_manager_reports():
    print("\n=== Отчёты менеджеров ===")
    managers = get_managers()
    period = f"{DATE_FROM[:10]} — {DATE_TO[:10]}"

    for manager in managers:
        print(f"\n[{manager['NAME']}]")
        rows = []

        for line in report_managers.REPORT:
            entity = line["entity"]

            # Разделитель — просто добавляем в rows, не считаем
            if entity == "header":
                rows.append({"title": line["title"], "value": None, "header": True})
                print(f"  ── {line['title']} ──")
                continue

            # Обычная метрика — считаем
            entity_url = DEAL_URL if entity == "deal" else LEAD_URL
            params = {
                **line["params"],
                "filter[ASSIGNED_BY_ID]": manager["ID"],
            }
            c = count(entity_url, build_params(params))
            rows.append({"title": line["title"], "value": c})
            print(f"  ✓ {line['title']}: {c}")

        filename = f"{manager['NAME']} - Отчет за {MONTH_NAME}.xlsx"
        generate_excel_rows(
            title=f"Отчёт менеджера: {manager['NAME']}",
            period=period,
            rows=rows,
            output_path=filename,
        )

# ============================================================
# ТОЧКА ВХОДА
# ============================================================
if __name__ == "__main__":
    try:
        run_okk_reports()
        run_manager_reports()
        print("\nВсе отчёты готовы.")
    except Exception as e:
        print(f"\nОшибка: {e}")

    input("\nНажмите ENTER, чтобы закрыть")