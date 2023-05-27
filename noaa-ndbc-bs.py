import requests
from bs4 import BeautifulSoup

def scrape(url, start_element=0, end_element=None):
    # Send a GET request to the URL
    response = requests.get(url)

    # If the GET request is successful, the status code will be 200
    if response.status_code == 200:
        # Get the content of the response
        page_content = response.content

        # Create a BeautifulSoup object and specify the parser
        soup = BeautifulSoup(page_content, 'html.parser')

        # Use the select() method to select all <p> tags
        p_tags = soup.select('p')

        # Create a list to store the text of each tag
        tag_texts = []

        # Loop through the list of tags, iterating over the elements in the range [start_element, end_element)
        for tag in p_tags[start_element:end_element]:
            # Get the text of the tag and add it to the list
            tag_texts.append(tag.get_text(separator='\n')) # The separator argument tells BeautifulSoup to replace <br> tags with a newline

        # Return the list of texts
        return tag_texts

# URL of the page you want to scrape
url = 'https://www.ndbc.noaa.gov/data/Forecasts/FZUS51.KOKX.html'

# Call the function with the URL and the range of elements you want, and assign the result to a variable
tag_texts = scrape(url, 6, 20)

# Now, tag_texts is a list of strings. You can use it in other functions or print it to check the result.
for i, text in enumerate(tag_texts):
    print(f"Element {i + 6}:")  # Adding 6 because we started from the 6th element
    print(text)
    print()