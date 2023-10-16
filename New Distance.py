import math

def haversine(lat1, lon1, lat2, lon2):

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    R = 6371.0

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    distance = R * c
    return distance

lat1 = -6.124804031015588
lon1 = 106.80046072808629
lat2 = -6.126961350988236
lon2 = 106.79094824289687

result = haversine(lat1, lon1, lat2, lon2)
print(f"Distance {result:.2f} km.")
