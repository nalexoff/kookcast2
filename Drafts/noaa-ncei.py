# this works but probably not useful for me: "updated daily where possible and are usually available one to two days after the date and time of the observation."
import requests
import json
from datetime import datetime

url = "https://www.ncei.noaa.gov/cdo-web/api/v2/data"
headers = {"token": "LeRhYpFmZmwpAzFDJicsMqEntqNgiCqU"}

today = datetime.today().strftime('%Y-%m-%d')

params = {
    "datasetid": "GHCND",
    "stationid": "GHCND:USW00014719", #this stationid is for Gabreski airport in Westhampton, NY
    "startdate": today, #can change this to YY-MM-DD format to get data from a specific date
    "enddate": today, #can change this to YY-MM-DD format to get data from a specific date
    "limit": 1000
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    
    if 'results' in data and data['results']:
        pretty_data = json.dumps(data, indent=2)
        print(pretty_data)
    else:
        print("No data available for today")
else:
    print(f"Error: {response.status_code}")
