import requests
import os
import dotenv

dotenv.load_dotenv()
MAPBOX_TOKEN = os.getenv("MAPBOX_ACCESS_TOKEN")
MBTA_TOKEN = os.getenv("MBTA_API_KEY")


def get_lat_lng(place_name):
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{place_name}.json"
    params = {
        "access_token": MAPBOX_TOKEN,
        "limit": 1
    }

    response = requests.get(url, params=params)
    data = response.json()

    if not data["features"]:
        raise ValueError(f"No results found for '{place_name}'")

    lng, lat = data["features"][0]["geometry"]["coordinates"]
    return lat, lng


def get_nearest_mbta_stop(lat, lng):
    url = "https://api-v3.mbta.com/stops"

    headers = {
        "x-api-key": MBTA_TOKEN
    }

    params = {
        "filter[latitude]": lat,
        "filter[longitude]": lng,
        "sort": "distance",
        "page[limit]": 1
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if not data["data"]:
        raise ValueError("No nearby MBTA stops found")

    stop = data["data"][0]
    name = stop["attributes"]["name"]

    wheelchair = stop["attributes"]["wheelchair_boarding"] == 1

    return name, wheelchair


def find_stop_near(place_name):
    lat, lng = get_lat_lng(place_name)
    return get_nearest_mbta_stop(lat, lng)

def main():
    place = input("Enter a location: ")

    try:
        stop_name, accessible = find_stop_near(place)

        accessible_text = "Yes" if accessible else "No"

        print(f"Nearest stop to '{place}':")
        print(f"Stop name: {stop_name}")
        print(f"Wheelchair accessible: {accessible_text}")

    except Exception:
        print(f"Could not find a stop near '{place}'. Please try again.")


if __name__ == "__main__":
    main()