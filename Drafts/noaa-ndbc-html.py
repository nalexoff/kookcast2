import requests

# Send a GET request to the website and retrieve the HTML content
url = 'https://www.ndbc.noaa.gov/data/Forecasts/FZUS51.KOKX.html'
response = requests.get(url)
html_content = response.text

# Print the HTML content of the page
print(html_content)