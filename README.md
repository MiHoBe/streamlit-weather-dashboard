# streamlit-weather-dashboard
Weather Data dashboard which displays current temperature (C), and other details. Made using openweather API and Streamlit.

### Notes
- Uses weather API API to get current weather and 3-day forecast data.
- Still in development, so most of the locations are not mentioned.

## Weather API Token
Head over to [weatherapi](https://www.weatherapi.com/) site, and create a free account, and copy & paste API Key inside **.env** file

## .env file
Create a **.env** file inside the folder
Now open the **.env** file, add the **API token**, and close the file
```text
weather_api = "enter your key"
```

## Setup - virtualenv
Create a virtual environment using the following command to run the app.
```bash
virtualenv weather-env
```
Now activate the environment
```bash
weather-env/Scripts/activate
```

## Setup - Package installation
Run the PIP command to install app package dependencies
```bash
pip install -r requirements.txt
```

## Run the Weather-Update dashboard
```bash
streamlit run frontend/app.py
```

The Weather-Update app should now be running and will open the streamlit app in the browser.

Feel free to contribute to this project or report any issues you encounter. Happy coding!
