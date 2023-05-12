from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY
import requests
import json


def get_photo(city, state):
    # Create a dictionary for the headers to use in the request
    # Create the URL for the request with the city and state
    # Make the request
    # Parse the JSON response
    # Return a dictionary that contains a `picture_url` key and
    #   one of the URLs for one of the pictures in the response
    url = "https://api.pexels.com/v1/search"
    headers = {"Authorization": PEXELS_API_KEY}
    params = {
        "per_page": 1,
        "query": city + " " + state
        }
    response = requests.get(url, params=params, headers=headers)
    content = json.loads(response.content)

    return {"picture_url": content["photos"][0]["src"]["original"]}


# def get_weather(city, state):
#     url = "http://api.openweathermap.org/geo/1.0/direct"
#     headers = {"appid": OPEN_WEATHER_API_KEY}
#     params = {
#         "q": city + "," + state,
#         "limit": 1,
#         }
#     response = requests.get(url, params=params, headers=headers)
#     content = json.loads(response.content)
#     latitude = content["lat"]
#     longitude = content["lon"]
#     url = "https://api.openweathermap.org/data/2.5/weather"
#     headers = {"appid": OPEN_WEATHER_API_KEY}
#     params = {
#         "lat": latitude,
#         "lon": longitude,
#         "units": "imperial",
#     }
#     response = requests.get(url, params=params, headers=headers)
#     content = json.loads(response.content)

#     temperature = content["main"]["temp"]
#     description = content["weather"][0]["description"]
#     weather = {"temperature": temperature, "description": description}
#     return weather
