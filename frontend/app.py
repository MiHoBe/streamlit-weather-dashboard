
import streamlit as st
import plotly.graph_objects as go
from datetime import ( datetime )
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
next_3_day_data = api_connection.get_three_days_weather()

st.info('Note, Time displayed is in IST Timezone.')

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

graph, hourly_data = st.tabs(['Graph', 'Hourly Data'])

with graph:
    # Create traces
    time_now = datetime.now()

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x = next_3_day_data['date'], 
            y = next_3_day_data['temp_c'],
            mode = 'lines',
            name = 'Hourly Temp (°C)'
        )
    )

    fig.add_trace(
        go.Scatter(
            x = next_3_day_data['date'], 
            y = next_3_day_data['feels_like'],
            mode = 'lines',
            name = 'Feels Like (°C)'
        )
    )

    # Add current Time line
    fig.add_vline(
        x = time_now, 
        line_color = "green",
        opacity = 0.4
    )

    # Update chart layout
    fig.update_layout(
        title = "Hourly Weather Forecast",
        xaxis_title = "Date",
        yaxis_title = "Temperature °C",
        hovermode = "x"
    )

    st.plotly_chart(fig, use_container_width=True)

with hourly_data:
    st.write(next_3_day_data)

# Concluding remarks
st.write( 'Weather data source: [http://weatherapi.com](https://www.weatherapi.com)' )
st.write( 'Github repository: [streamlit-weather-dashboard](https://github.com/Mega-Barrel/streamlit-weather-dashboard)' )
