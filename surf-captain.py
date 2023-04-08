# Import necessary modules and classes from the Selenium package
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

# Create a new instance of the Safari driver
driver = webdriver.Safari()

# Navigate to the Google homepage
driver.get("https://www.google.com")

# Wait for the search box to appear on the page
# We use the WebDriverWait class to wait for the presence of the search box element
# The first parameter is the driver instance, and the second parameter is the maximum wait time in seconds
# The presence_of_element_located() function returns a locator for the search box element
# We use the By class to specify that we are locating the element by its name attribute, which is "q"
# Once the search box element is present, we store it in the search_box variable for later use
search_box = WebDriverWait(driver, 10).until(
    presence_of_element_located((By.NAME, "q"))
)

# Type "cats and dogs" into the search box
# We use the send_keys() method to simulate typing into the search box element
# The argument passed to the method is the text to be typed, which in this case is "cats and dogs"
search_box.send_keys("cats and dogs")

# Submit the search query
# We use the submit() method to submit the search query and load the search results page
search_box.submit()

# Wait for the search results to load on the page
# We use the WebDriverWait class again to wait for the presence of the search results element
# The presence_of_element_located() function returns a locator for the search results element
# We use the By class to specify that we are locating the element by its ID attribute, which is "search"
# Once the search results element is present, we know that the search results have loaded, and we can move on
WebDriverWait(driver, 10).until(
    presence_of_element_located((By.ID, "search"))
)

# Close the browser
# We use the quit() method to close the browser and terminate the webdriver instance
driver.quit()
