import requests
from datetime import datetime

api_key = 'a7c4a704fde6738c3d2187d2faf31366'
location = input("Enter the city name: ")

comp_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api_key
api_link = requests.get(comp_api_link)
api_data = api_link.json()

tempCity = ((api_data['main']['temp']) - 273.15)

weatherDescription = api_data['weather'][0]['description']

humidity = api_data['main']['humidity']

windSpeed = api_data['wind']['speed']

dateTime = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

file = open("WeatherData.txt", "w")

file.write("\n")

file.write("Weather Stats for - {}  || {}".format(location.upper(), dateTime))

file.write("\n")

file.write("Current temperature is: {:.2f} deg C".format(tempCity))

file.write("\n")

file.write("Current weather desc  :" + str(weatherDescription))

file.write("\n")

file.write("Current Humidity      :" + str(humidity) + "%")

file.write("\n")

file.write("Current wind speed    :" + str(windSpeed) + "kmph")

file.close()
