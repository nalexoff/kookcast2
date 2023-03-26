import requests
import re

# Define the start and end markers for the forecast sections
START_MARKER_1 = 'Montauk Point NY to Sandy Hook NJ out 20 nm offshore, including\nLong Island Sound, the Long Island Bays, and New York Harbor'
END_MARKER_1 = 'ANZ350-262315-'
START_MARKER_2 = 'Moriches Inlet NY to Montauk Point NY out 20 nm-'
END_MARKER_2 = 'ANZ353-262315-'

# Function to extract a forecast section from the text, given start and end markers
def get_forecast_section(text, start_marker, end_marker):
    start_index = text.index(start_marker)
    end_index = text.index(end_marker, start_index)
    return text[start_index + len(start_marker):end_index]

# Function to extract and clean individual forecasts from a forecast section
def extract_clean_forecasts(forecast_section, skip_until_today=False, remove_prefix=''):
    forecasts = forecast_section.split('\n\n')
    forecasts = [f.strip() for f in forecasts if f.strip()]

    cleaned_forecasts = []
    for index, forecast in enumerate(forecasts):
        cleaned_forecast = re.sub('<[^<]+?>|\r\n|\n', ' ', forecast).strip()
        if skip_until_today:
            if cleaned_forecast.startswith("TODAY"):
                skip_until_today = False
        if not skip_until_today and cleaned_forecast:
            if index == 0 and remove_prefix:
                cleaned_forecast = cleaned_forecast.replace(remove_prefix, '', 1)
            cleaned_forecasts.append(cleaned_forecast)

    return cleaned_forecasts

# Function to parse the NDBC text given a URL
def parse_ndbc_text(url):
    response = requests.get(url)
    text = response.text

    # Extract the forecast sections
    forecast_section_1 = get_forecast_section(text, START_MARKER_1, END_MARKER_1)
    forecast_section_2 = get_forecast_section(text, START_MARKER_2, END_MARKER_2)

    # Extract and clean individual forecasts from the sections
    cleaned_forecasts_1 = extract_clean_forecasts(forecast_section_1, remove_prefix='ANZ300-262315- ')
    cleaned_forecasts_2 = extract_clean_forecasts(forecast_section_2, skip_until_today=True)

    return cleaned_forecasts_1, cleaned_forecasts_2

# Call the function and print the results
forecasts_1, forecasts_2 = parse_ndbc_text('https://www.ndbc.noaa.gov/data/Forecasts/FZUS51.KOKX.html')
print(forecasts_1, forecasts_2)