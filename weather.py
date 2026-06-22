import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"Temperature: {temperature}°C, Condition: {description}")
    else:
        print("Error fetching weather data. Please check the city name and API key.")

api_key = "f79e78adc911a136fc1cc1d095735a2a"
user_city = input("Enter the city name: ")
get_weather(user_city, api_key)