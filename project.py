import requests

API_KEY = '91e6216d5d55bd105c0cc9118bb6c75a'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def get_weather(city_name):
    complete_url = f'{BASE_URL}q={city_name}&appid={API_KEY}&units=metric'
    response = requests.get(complete_url)
    data = response.json()
    return data

def display_weather(weather_data):
    main_info = weather_data['main']
    weather = weather_data['weather'][0]

    print(f"Weather in {weather_data['name']}:")
    print(f"Temperature: {main_info['temp']}°C")
    print(f"Condition: {weather['description']}")

if __name__ == '__main__':
    city = input("Enter city name: ")
    weather_data = get_weather(city)

    if weather_data['cod'] == 200:
        display_weather(weather_data)
    else:
        print("City not found.")
