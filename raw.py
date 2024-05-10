import streamlit as st
import requests

def fetch_real_time_weather(api_key, location):
    query = f"weather {location}"
    url = f"https://serpapi.com/search.json?q={query}&hl=en&gl=in&api_key={api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            st.write(data)  # Log the full data for debugging
            if 'weather_results' in data:
                weather = data['weather_results']['forecast']['description']
                temperature = data['weather_results']['forecast']['temp']
                humidity = data['weather_results']['forecast']['humidity']
                wind_speed = data['weather_results']['forecast']['wind_speed']
                return {
                    "Weather": weather,
                    "Temperature": f"{temperature}°C",
                    "Humidity": f"{humidity}%",
                    "Wind Speed": f"{wind_speed} m/s"
                }
            else:
                return "Weather data not found in the API response."
        else:
            return "Failed to fetch weather data"
    except Exception as e:
        return f"An error occurred while fetching the weather data: {e}"

def main():
    st.title('Real-Time Weather App')
    api_key = '97bf3b7b0d40cfa920f42806d9f3e4d68bb442e925caecd9dcf2719117330101'
    location = st.text_input('Location', 'Enter a location here')
    
    if st.button('Fetch Weather'):
        if location:
            result = fetch_real_time_weather(api_key, location)
            if isinstance(result, dict):
                st.write(result)
            else:
                st.error(result)
        else:
            st.error("Please enter a location.")

if __name__ == "__main__":
    main()