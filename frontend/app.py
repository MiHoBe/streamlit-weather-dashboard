
import streamlit as st
from weather_api import ( WeatherApi )

st.set_page_config(
    page_title='Weather - Home Page',
    page_icon='☁️',
    menu_items={
        "About": "A Streamlit Weather Application to see current weather and next 7 days weather data",
        "Report a bug": "https://www.extremelycoolapp.com/bug"
    }
)

st.header('How\'s the Weather today? 🌤️')

country_set = ['India', 'UK', 'Spain']
country = st.selectbox("Select a Country", options=country_set)

cities = {
    "India": ["Mumbai", "New Delhi", "Bangalore", "Indore", "Chennai"],
    "UK": ["Liverpool", "Nottingham", "Leicester", "City of London", "Manchester", "Belfast"],
    "Spain": ["Madrid", "Seville", "Valencia", "Barcelona", "Zaragoza"]
}

city = st.selectbox("Select a City", cities[country])

# Create WeatherApi object
api_connection = WeatherApi(city)
data = api_connection.get_current_weather()

# Weather details
st.subheader('Current Weather')
st.markdown(f"""
        The current weather is <b>{data["current_weather"]}</b> °C,
        with wind speed of <b>{data["wind_speed"]}</b> kph.
        The current wind direction is <b>{data["wind_direction"]}</b>.
    """,
    unsafe_allow_html=True
)
st.markdown(
    f'Weather condition: <b>{data["temp_condition"]}</b>',
    unsafe_allow_html=True
)

st.subheader('Next 3 day forcast')
st.write(api_connection.get_seven_days_weather())

# Concluding remarks
st.write( 'Weather data source: [http://weatherapi.com](https://www.weatherapi.com)' )
st.write( 'Github repository: [streamlit-weather-dashboard](https://github.com/Mega-Barrel/streamlit-weather-dashboard)' )
