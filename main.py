import requests
import os
from dotenv import load_dotenv


load_dotenv()
api_key =  os.getenv("API_KEY")
url = "https://calendarific.com/api/v2/holidays"

months = [
    "января",
    "февраля",
    "марат",
    "апреля",
    "мая",
    "июня",
    "июля",
    "августа",
    "сентября",
    "октября",
    "ноября",
    "декабря",
]


params = {
    "api_key": api_key,
    "country": "RU",
    "year": 2025
}

response = requests.get(url, params=params)
response.raise_for_status()
holidays = response.json()["response"]["holidays"]

for holiday in holidays:
    month = holiday['date']["datetime"]["month"]
    print(f"Дата: {holiday['date']["datetime"]["day"]} {months[month-1]}\nНазвание праздника: {holiday["name"]}\nОписание: {holiday["description"]}\n\n")
