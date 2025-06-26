import requests;

lon = input("Enter longituide:")
lat = input("Enter latitude:")

key = "api key" #Enter personal Api key generated from weatherapi here

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"

response = requests.get(url)

data = response.json()

if response.status_code == 200:
    print(" ")
    print(f"The WEATHER in {data["name"]} is: {data["weather"][0]["main"]} - {data["weather"][0]["description"]} with a TEMPERATURE of: {data["main"]["temp"]}K which feels like {data["main"]["feels_like"]}K");
else:
    print(print("Failed to retrieve data:", data.get("error", {}).get("message", "Unknown error")))