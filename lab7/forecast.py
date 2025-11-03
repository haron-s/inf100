import requests

def weather_in_bergen_next_hour():
    url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.390794&lon=5.326107"
    response = requests.get(url, headers={"User-Agent": "inf100.ii.uib.no hasun3150"})
    data = response.json()

    weather_code = data["properties"]["timeseries"][0]["data"]["next_1_hours"]["summary"]["symbol_code"]
    print(f'Været i Bergen neste time: {weather_code}') 
    return weather_code

weather_in_bergen_next_hour()