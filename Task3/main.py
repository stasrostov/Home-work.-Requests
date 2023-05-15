import requests
from datetime import datetime, timedelta

two_days_ago = datetime.now() - timedelta(days=2)
unix_two_days_ago = int(two_days_ago.timestamp())

url = f"https://api.stackexchange.com/2.3/questions?fromdate={unix_two_days_ago}&" \
      f"todate={int(datetime.now().timestamp())}&" \
      f"order=desc&sort=activity&tagged=Python&site=stackoverflow"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    for question in data['items']:
        print(f"Название: {question['title']}")
        print(f"Ссылка: {question['link']}")
        print()
else:
    print("Ошибка при выполнении запроса:", response.status_code)
