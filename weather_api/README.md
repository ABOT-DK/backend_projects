# 🌦️ Weather Info Fetcher

This is a simple Python project that fetches and displays real-time weather information using geographic coordinates (latitude and longitude). It uses the [OpenWeatherMap API](https://openweathermap.org/api) and the `requests` library to retrieve weather data.

---

## 📌 Features

- User input for latitude and longitude
- Retrieves real-time weather data
- Displays:
  - Location name
  - Main weather condition
  - Weather description
  - Temperature in Kelvin
  - Human perception of temperature in Kelvin
- Handles errors gracefully

---

## 🧠 How It Works

- Prompts the user to enter **latitude** and **longitude**
- Sends a `GET` request to the **OpenWeatherMap API**
- Parses the returned **JSON data**
- Displays the **weather details** for the specified location

---

## 📄 Usage

```bash
python weather_fetcher.py
```

You'll be prompted:

```yaml
Enter longitude:
Enter latitude:
```

### Example Output:

```text
The WEATHER in Accra is: Rain - moderate rain with a TEMPERATURE of: 299.82K which feels like 300.15K
```

---

## 🔐 API Key

You must replace the `key` variable with your **personal API key** from [OpenWeatherMap](https://openweathermap.org/):

```python
key = "your_api_key_here"
```

---

## 📄 License

This project is **open source** and free to use for educational purposes.

---

## 🤝 Acknowledgements

- [OpenWeatherMap API](https://openweathermap.org/api)
- [Requests library documentation](https://docs.python-requests.org/)
