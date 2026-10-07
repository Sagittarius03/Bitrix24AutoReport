from settings import DATE_FROM, DATE_TO

# ============================================================
# ЕДИНЫЙ ФИЛЬТР
# ============================================================
# В каждом блоке params автоматически подставится:
#   filter[ASSIGNED_BY_ID] = ID текущего менеджера
#
# Поле "entity":
#   "deal" — crm.deal.list
#   "lead" — crm.lead.list
#
# Ты дополняешь params своими фильтрами (STATUS_ID, STAGE_ID и т.д.)
# ============================================================

REPORT = [
    # -------------------- СДЕЛКИ --------------------
    {
        "title": "Общее количество сделок",
        "entity": "deal",
        "params": {
            "filter[>=DATE_CREATE]": DATE_FROM,
            "filter[<=DATE_CREATE]": DATE_TO,
        },
    },
    {
        "title": "Успех",
        "entity": "deal",
        "params": {
            "filter[>=CLOSEDATE]": DATE_FROM,
            "filter[<=CLOSEDATE]": DATE_TO,
            "filter[STAGE_SEMANTIC_ID]": "S",
        },
    },
    {
        "title": "Провалено",
        "entity": "deal",
        "params": {
            "filter[>=CLOSEDATE]": DATE_FROM,
            "filter[<=CLOSEDATE]": DATE_TO,
            "filter[STAGE_SEMANTIC_ID]": "F",
        },
    },
    {
        "title": "Общее - Алексей",
        "entity": "deal",
        "params": {
            "filter[>=DATE_CREATE]": DATE_FROM,
            "filter[<=DATE_CREATE]": DATE_TO,
            "filter[UF_CRM_1667463594]": "3",
            # "filter[STAGE_SEMANTIC_ID]": "F",
        },
    },
    {
        "title": "Успех - Алексей",
        "entity": "deal",
        "params": {
            "filter[>=CLOSEDATE]": DATE_FROM,
            "filter[<=CLOSEDATE]": DATE_TO,
            "filter[UF_CRM_1667463594]": "3",
            "filter[STAGE_SEMANTIC_ID]": "S",
        },
    },
    {
        "title": "Провалено - Алексей",
        "entity": "deal",
        "params": {
            "filter[>=CLOSEDATE]": DATE_FROM,
            "filter[<=CLOSEDATE]": DATE_TO,
            "filter[UF_CRM_1667463594]": "3",
            "filter[STAGE_SEMANTIC_ID]": "F",
        },
    },
    {
        "title": "Общее - Татьяна",
        "entity": "deal",
        "params": {
            "filter[>=DATE_CREATE]": DATE_FROM,
            "filter[<=DATE_CREATE]": DATE_TO,
            "filter[UF_CRM_1667463594]": "1",
            # "filter[STAGE_SEMANTIC_ID]": "F",
        },
    },
    {
        "title": "Успех - Татьяна",
        "entity": "deal",
        "params": {
            "filter[>=CLOSEDATE]": DATE_FROM,
            "filter[<=CLOSEDATE]": DATE_TO,
            "filter[UF_CRM_1667463594]": "1",
            "filter[STAGE_SEMANTIC_ID]": "S",
        },
    },
    {
        "title": "Провалено - Татьяна",
        "entity": "deal",
        "params": {
            "filter[>=CLOSEDATE]": DATE_FROM,
            "filter[<=CLOSEDATE]": DATE_TO,
            "filter[UF_CRM_1667463594]": "1",
            "filter[STAGE_SEMANTIC_ID]": "F",
        },
    },
    {
        "title": "Сделок с лида",
        "entity": "deal",
        "params": {
            "filter[>=DATE_CREATE]": DATE_FROM,
            "filter[<=DATE_CREATE]": DATE_TO,
            "filter[UF_CRM_1724841062395]": "1"
            # "filter[SOURCE_ID]": "LEAD",
        },
    },
    {
        "title": "С лида Успех",
        "entity": "deal",
        "params": {
            "filter[>=CLOSEDATE]": DATE_FROM,
            "filter[<=CLOSEDATE]": DATE_TO,
            "filter[UF_CRM_1724841062395]": "1",
            # "filter[SOURCE_ID]": "LEAD",
            "filter[STAGE_SEMANTIC_ID]": "S",
        },
    },
    {
        "title": "С лида Провалено",
        "entity": "deal",
        "params": {
            "filter[>=CLOSEDATE]": DATE_FROM,
            "filter[<=CLOSEDATE]": DATE_TO,
            "filter[UF_CRM_1724841062395]": "1",
            # "filter[SOURCE_ID]": "LEAD",
            "filter[STAGE_SEMANTIC_ID]": "F",
        },
    },

    # -------------------- ЛИДЫ --------------------
    {
        "title": "ЛИДЫ",
        "entity": "header",
    },
    {
        "title": "Принято",
        "entity": "lead",
        "params": {
            "filter[>=DATE_CREATE]": DATE_FROM,
            "filter[<=DATE_CREATE]": DATE_TO,
            "filter[STATUS_ID]": "NEW",
        },
    },
    {
        "title": "Конвертировано",
        "entity": "lead",
        "params": {
            "filter[>=DATE_CREATE]": DATE_FROM,
            "filter[<=DATE_CREATE]": DATE_TO,
            "filter[STATUS_ID]": "CONVERTED",
        },
    },
    {
        "title": "Забраковано",
        "entity": "lead",
        "params": {
            "filter[>=DATE_CREATE]": DATE_FROM,
            "filter[<=DATE_CREATE]": DATE_TO,
            "filter[STATUS_ID]": "JUNK",
        },
    },
    {
        "title": "В работе",
        "entity": "lead",
        "params": {
            "filter[>=DATE_CREATE]": DATE_FROM,
            "filter[<=DATE_CREATE]": DATE_TO,
            "filter[STATUS_ID]": "IN_PROCESS",
        },
    },
]