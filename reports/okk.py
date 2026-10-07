from settings import DATE_FROM, DATE_TO

REPORT = {
    "Передано менеджеру": {
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
        "description": "Все созданные сделки, кроме стадии NEW",
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