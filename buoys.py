# problem: need to retrieve buoy data from the web
# identify sources of buoy data relevant to me  
# identify refresh rate of the data
# determine how to retrieve the data
# determine how to store the data - suggested by AP
# determine how to use the data - suggested by AP
# *** Copilot is even helping with problem framing. I hadn't considered some of these other aspects of handling the data, but they are valuable contributions. ***
 
#NOAA API token: LeRhYpFmZmwpAzFDJicsMqEntqNgiCqU
#NOAA API documentation: https://www.ncdc.noaa.gov/cdo-web/webservices/v2

#'requests' library to make HTTP requests to the API endpoint.

import requests

# Set the API endpoint URL and authorization token
url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data'
token = '<your_token_here>'

# Set the parameters for the API request
params = {
    'datasetid': 'GHCND',
    'locationid': 'ZIP:28801',
    'startdate': '2021-01-01',
    'enddate': '2021-01-31',
    'datatypeid': 'TMIN',
    'limit': 1000
}

# Set the headers for the API request
headers = {
    'token': token
}

# Make the API request using the requests library
response = requests.get(url, params=params, headers=headers)

# Check the response status code to ensure the request was successful
if response.status_code == 200:
    # Process the API response data
    data = response.json()
    # do something with data...
else:
    print('API request failed with status code:', response.status_code)
