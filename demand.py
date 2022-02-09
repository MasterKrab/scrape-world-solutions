from datetime import datetime, timedelta
from config import BASE_URL
import requests

demands = []

current_date = datetime.now()

for i in range(7):
    current_date += timedelta(days=i)

    response = requests.post(f"{BASE_URL}/demand", json={
        "date": str(current_date),
        "temperature": 21
    })

    data = response.json()

    demands.append(data["demand"])

print(demands)
