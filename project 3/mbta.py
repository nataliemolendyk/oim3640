import os
import requests
import dotenv
import math

dotenv.load_dotenv()

MAPBOX_TOKEN = os.getenv("MAPBOX_ACCESS_TOKEN")
MBTA_TOKEN = os.getenv("MBTA_API_KEY")


def get_lat_lng(place_name):
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{place_name}.json"

    params = {
        "access_token": MAPBOX_TOKEN,
        "limit": 1
    }

    r = requests.get(url, params=params)
    data = r.json()

    if not data.get("features"):
        raise ValueError("No location found")

    lng, lat = data["features"][0]["geometry"]["coordinates"]
    return float(lat), float(lng)


def haversine(lat1, lng1, lat2, lng2):
    R = 3958.8

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)

    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lng2 - lng1)

    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def get_nearest_mbta_stop(lat, lng):
    headers = {"x-api-key": MBTA_TOKEN}

    
    routes_url = "https://api-v3.mbta.com/routes"
    routes_params = {"filter[type]": 2}

    r = requests.get(routes_url, headers=headers, params=routes_params)
    routes = r.json().get("data", [])

    if not routes:
        raise ValueError("No commuter rail routes found")

    nearest = None
    min_dist = float("inf")

    
    for route in routes:
        route_id = route["id"]

        stops_url = "https://api-v3.mbta.com/stops"

        r = requests.get(
            stops_url,
            headers=headers,
            params={"filter[route]": route_id}
        )

        stops = r.json().get("data", [])

        for stop in stops:
            a = stop["attributes"]

            if a["latitude"] is None or a["longitude"] is None:
                continue

            d = haversine(lat, lng, a["latitude"], a["longitude"])

            if d < min_dist:
                min_dist = d
                nearest = {
                    "name": a["name"],
                    "lat": a["latitude"],
                    "lng": a["longitude"],
                    "wheelchair": a["wheelchair_boarding"] == 1
                }

    if not nearest:
        raise ValueError("No commuter rail station found"

    return nearest

def find_stop_near(place_name):
    lat, lng = get_lat_lng(place_name)
    stop = get_nearest_mbta_stop(lat, lng)

    return lat, lng, stop