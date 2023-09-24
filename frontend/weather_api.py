import os
import requests
from datetime import datetime
from dotenv import load_dotenv

class WeatherApi():
    
    def __init__(self, place):
        load_dotenv()
        self.query = place
        self.dt = datetime.now().date()
        self._key = self.get_api_key()
        self.api_url = "http://api.weatherapi.com/v1/"
        self.query_key = f"key={self._key}&q={self.query}"

    def get_api_key(self):
        """
        Returns the API key from environment variable.
        """
        API_KEY = os.environ.get('weather_api')
        if not API_KEY:
            raise ValueError('API key is not available.')
        else:
            return API_KEY

    def get_current_weather(self):
        """
        Method to Make a call to weather API
        """
        url = f"{self.api_url}current.json?{self.query_key}&dt={self.dt}"
        resp = requests.get(url=url)
        
        # Return the JSON data if status code is 200
        if resp.status_code == 200:
            data = resp.json()
            json_data = {
                'place': data['location']['name'],
                'current_weather': data['current']['temp_c'],
                'wind_speed': data['current']['wind_kph'],
                'wind_direction': data['current']['wind_dir'],
                'temp_condition': data['current']['condition']['text']
            }
            return json_data
        else:
            return 'Uh ooh, something went wrong while retriving data. Please check your input'
    
    def get_seven_days_weather(self):
        """
        Method to get next 7 days forecast data
        """
        url = f"{self.api_url}forecast.json?{self.query_key}&days=3"
        resp = requests.get(url)
        
        # return the JSON data if status code is 200
        if resp.status_code == 200:
            data = resp.json()
            return data['forecast']
        else:
            return 'Uh ooh, something went wrong while retriving data. Please check your input.'
