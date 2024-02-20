import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        description = weather_data['weather'][0]['description']

        print(f"Weather in {location}:")
        print("Temperature: {:.2f} degrees Celsius".format(temperature))
        print("Humidity: {}%".format(humidity))
        print("Wind Speed: {} m/s".format(wind_speed))
        print("Description: {}".format(description))
    else:
        print(f"Failed to retrieve weather data. Status code: {response.status_code}")

if __name__ == "__main__":
    api_key = '5d6a9b8e75833eb63849bfa9b96af52b'
    user_input = input("Enter the city name or zip code: ")
    get_weather(api_key, user_input)
