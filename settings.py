from datetime import date, timedelta

# --- Границы предыдущего месяца ---
today = date.today()
first_day_current = today.replace(day=1)
last_day_prev = first_day_current - timedelta(days=1)
first_day_prev = last_day_prev.replace(day=1)

WEBHOOK = ""

DATE_FROM = first_day_prev.strftime("%Y-%m-%dT00:00:00")
DATE_TO = last_day_prev.strftime("%Y-%m-%dT23:59:59")

# --- Название месяца на русском ---
MONTHS_RU = [
    "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
    "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь",
]

MONTH_NAME = MONTHS_RU[last_day_prev.month - 1]

# --- Общие фильтры для всех отчётов (воронка) ---
BASE_FILTER = {
    "filter[CATEGORY_ID]": 0,   # Общая воронка
}

# --- Должности для отбора сотрудников ---
POSITION_OKK = "колл-центр"
POSITION_MANAGER = "менеджер по работе с клиентами"

# --- Структура отчёта ---
# Ключ словаря = название колонки в отчёте.
# Поля внутри:
#   description  — что считаем (для вывода)
#   params       — фильтры запроса (без разбивки по менеджерам)
#   by_manager   — True, если нужно разбивать по менеджерам
#   count        — откуда брать число: "total" или "result"

REPORT = {
    'Передано менеджеру': {
        "description": "Все созданные сделки за месяц",
        "params": {
            "filter[>=DATE_CREATE]": DATE_FROM,
            "filter[<=DATE_CREATE]": DATE_TO,
            "filter[UF_CRM_1667463594]": "3",
        },
        "by_manager": True,
        "count": "total",
    },

    "Встреч состоялось": {
        "description": "Все созданные сделки за месяц, кроме стадии NEW",
        "params": {
            "filter[>=DATE_CREATE]": DATE_FROM,
            "filter[<=DATE_CREATE]": DATE_TO,
            "filter[UF_CRM_1667463594]": "3",
            "filter[!STAGE_ID]": "NEW",
        },
        "by_manager": True,
        "count": "total",
    },

    "Заключенных за месяц": {
        "description": "Успешно закрытые сделки по CLOSEDATE",
        "params": {
            "filter[>=CLOSEDATE]": DATE_FROM,
            "filter[<=CLOSEDATE]": DATE_TO,
            "filter[UF_CRM_1667463594]": "3",
            "filter[STAGE_SEMANTIC_ID]": "S",
        },
        "by_manager": True,
        "count": "total",
    },

    "Проваленных за месяц": {
        "description": "Проваленные сделки по CLOSEDATE",
        "params": {
            "filter[>=CLOSEDATE]": DATE_FROM,
            "filter[<=CLOSEDATE]": DATE_TO,
            "filter[UF_CRM_1667463594]": "3",
            "filter[STAGE_SEMANTIC_ID]": "F",
        },
        "by_manager": True,
        "count": "total",
    },
}