from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome WebDriver options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run browser in headless mode for faster execution (optional)

# Create a new instance of the Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the URL
url = "https://surfcaptain.com/forecast/southampton-new-york"
driver.get(url)

# Find all the elements with the class name "summary-day-expand"
buttons = driver.find_elements(By.CLASS_NAME, "summary-day-expand")

# Iterate through the first three buttons in the list of found elements and interact with them individually
for i, button in enumerate(buttons[:3]):
    # Perform your desired action with the button
    print(f"Interacting with button {i + 1}")
    button.click()

    # Add wait time between button interactions
    time.sleep(3)  # Adjust the sleep time based on your requirements

    # Add any other interaction or data extraction code here

# Close the driver
driver.quit()
