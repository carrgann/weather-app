import requests

api_key = 'f8ac3f19605ab0f18723a5dae525df29'

user_input = input("Enter city: ")

# using data from openweathermap.org
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == 404:
    print("No city found.")
else:
    # displays weather of chosen city
    weather = weather_data.json()['weather'][0]['main']

    # displays temperature
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather forecast in {user_input} today is {weather} with a temperature of {temp}°F.")

