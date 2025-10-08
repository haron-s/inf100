from pathlib import Path
from math import sin, cos, asin, sqrt, radians
import json

content = Path("points.json").read_text(encoding="utf-8")
data = json.loads(content)

#posisjon 1
lon1 = data['features'][0]['geometry']['coordinates'][0]
lat1 = data['features'][0]['geometry']['coordinates'][1]

#posisjon 2
lon2 = data['features'][1]['geometry']['coordinates'][0]
lat2 = data['features'][1]['geometry']['coordinates'][1]

earth_radius = 6371000  # meter
phi1 = radians(lat1)
lam1 = radians(lon1)
phi2 = radians(lat2)
lam2 = radians(lon2)

a = sin((phi2 - phi1) / 2)**2 + cos(phi1) * cos(phi2) * sin((lam2 - lam1) / 2)**2
result = 2 * earth_radius * asin(sqrt(a))
print(result)