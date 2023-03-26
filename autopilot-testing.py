# create a variable that holds wind speed information
wind_speed = 0
# create a variable that holds wind direction information
wind_direction = 0
# create a variable that holds the current heading
heading = 0

#create a class with the attributes of wind speed and wind direction
#this class is called "wind3"
class Wind3:
    def __init__(self, wind_speed, wind_direction):
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction

#import the python module beautiful soup
#this module is used to parse html
from bs4 import BeautifulSoup
#import the python module urllib2
#this module is used to open urls
import urllib2

# The error message "Import 'bs4' could not be resolved from source" typically means that the Python interpreter cannot find the 'bs4' package that you are trying to import.
#pip install beautifulsoup4

# create a variable that stores the information received from an http request to the url
# the url is: http://weather.gc.ca/windsock/data/windsock_data_e.html
# the information is in html format
html = urllib2.urlopen("http://weather.gc.ca/windsock/data/windsock_data_e.html").read()
# create a variable that stores the information received from the html parser
# the html parser is beautiful soup
soup = BeautifulSoup(html, "html.parser")

#create a variable that stores the information received from the html parser
#the html parser is beautiful soup
#the information is stored in a table
#the table is identified by the class "table table-striped table-hover"
table = soup.find("table", {"class": "table table-striped table-hover"})
