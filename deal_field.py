

import os

import requests# Загружаем переменные окружения из .env файла

# Ваш webhook (замените на свой)
WEBHOOK = "https://legion21.bitrix24.kz/rest/1266/vdqzgs171axjcmb8/"

# Метод API, который хотим вызвать
method = "crm.deal.fields"

# Полный URL = webhook + метод
url = WEBHOOK + method

params = {
    # "select[]": ["NAME", "LAST_NAME",],
    # "filter[ACTIVE]": True,
}

response = requests.get(url, params=params)
data: dict = response.json()

# print(data['result'])
# for key in data["result"]:
print(data["result"]["UF_CRM_63EDE1F7087FA"])
# print(data["result"])