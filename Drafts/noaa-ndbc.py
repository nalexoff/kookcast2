# https://www.ndbc.noaa.gov/data/realtime2/ - looks like a good source of data for some but not all buoys
# buoy station 44017 I want to use went adrift on 1/21/23
# 44017	June 2023	Standard Maintenance
# can revisit this in June 2023 

import requests
import re

def parse_ndbc_text(url):
    # Make a GET request to the URL and retrieve the text content
    response = requests.get(url)
    text = response.text

    # Extract the first forecast section from the text
    start_marker = 'Montauk Point NY to Sandy Hook NJ out 20 nm offshore, including\nLong Island Sound, the Long Island Bays, and New York Harbor'
    end_marker = 'ANZ350-262315-'
    start_index = text.index(start_marker)
    end_index = text.index(end_marker, start_index)
    forecast_section_1 = text[start_index+len(start_marker):end_index]

    # Extract the second forecast section from the text
    start_marker_2 = 'Moriches Inlet NY to Montauk Point NY out 20 nm-'
    end_marker_2 = 'ANZ353-262315-'
    start_index_2 = text.index(start_marker_2, end_index)
    end_index_2 = text.index(end_marker_2, start_index_2)
    forecast_section_2 = text[start_index_2+len(start_marker_2):end_index_2]

    # Extract the individual forecasts using string manipulation for section 1
    forecasts_1 = forecast_section_1.split('\n\n')
    forecasts_1 = [f.strip() for f in forecasts_1 if f.strip()]

    # Extract the individual forecasts using string manipulation for section 2
    forecasts_2 = forecast_section_2.split('\n\n')
    forecasts_2 = [f.strip() for f in forecasts_2 if f.strip()]

    # Remove HTML tags, line breaks, and leading/trailing spaces from individual forecasts for section 1
    cleaned_forecasts_1 = []
    for forecast in forecasts_1:
        cleaned_forecast = re.sub('<[^<]+?>|\r\n|\n', ' ', forecast).strip()
        if cleaned_forecast:
            cleaned_forecasts_1.append(cleaned_forecast)

    # Remove HTML tags, line breaks, and leading/trailing spaces from individual forecasts for section 2
    cleaned_forecasts_2 = []
    skip_until_today = True
    for forecast in forecasts_2:
        cleaned_forecast = re.sub('<[^<]+?>|\r\n|\n', ' ', forecast).strip()
        if skip_until_today:
            if cleaned_forecast.startswith("TODAY"):
                skip_until_today = False
        if not skip_until_today and cleaned_forecast:
            cleaned_forecasts_2.append(cleaned_forecast)

    # Prepend the first forecast in cleaned_forecasts_2 to the list if it's not empty
    if cleaned_forecasts_2:
        cleaned_forecasts_2.insert(0, forecasts_2[0])

    # Return the list of cleaned forecasts for both sections
    return cleaned_forecasts_1, cleaned_forecasts_2

forecasts_1, forecasts_2 = parse_ndbc_text('https://www.ndbc.noaa.gov/data/Forecasts/FZUS51.KOKX.html')
print(forecasts_1, forecasts_2)

