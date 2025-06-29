import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

CITY = 'Ahmedabad'
API_KEY = '88283f2cc6fc98ba2b3e6f5a854f60ec'
UNITS = 'metric'
API_URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units={UNITS}'

response = requests.get(API_URL)
data = response.json()

print(data)

dates = []
temps = []
if "list" in data:
    for entry in data['list']:
        date_text = entry['dt_txt']
        temp = entry['main']['temp']
        
        dates.append(datetime.strptime(date_text, '%Y-%m-%d %H:%M:%S'))
        temps.append(temp)

plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=temps, marker='o', color='b')
plt.title(f'Temperature Forecast for {CITY}', fontsize=16)
plt.xlabel('Date and Time')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
