import requests

payload = {
    "author": "",
    "createDateFrom": "",
    "createDateTo": "",
    "searchPhrase": "рейс",
    "skip": 0,
    "sortings": [],
    "take": 20,
}

try:
    response = requests.get("https://news.s7.ru/news", params=payload)
except ConnectionError:
    print("Проверьте подключение к сети")
else:
    response.json()