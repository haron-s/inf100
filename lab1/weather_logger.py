import requests
from pathlib import Path
import json

url = "https://api.met.no/weatherapi/nowcast/2.0/complete?lat=60.3894&lon=5.33"
response = requests.get(url, headers={"User-Agent": "no.uib.ii.inf100"})
data = response.json()

air_temp = data['properties']['timeseries'][0]['data']['instant']['details']['air_temperature']
time = data['properties']['timeseries'][0]['time']

print(time)
print(air_temp)

new_entry = {
  "time": time,
  "air_temp": air_temp
}

content = Path("weather_log.json").read_text(encoding="utf-8")
data = json.loads(content)

data.append(new_entry)

content = json.dumps(data, indent=2)
Path("weather_log.json").write_text(content, encoding="utf-8")

