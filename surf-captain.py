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

# Initialize an empty list to store the extracted text after each button interaction
extracted_text_list = []

# Iterate through the first three buttons in the list of found elements and interact with them individually
for i, button in enumerate(buttons[:3]):
    # Perform your desired action with the button
    print(f"Interacting with button {i + 1}")
    button.click()

    # Add wait time between button interactions
    time.sleep(3)  # Adjust the sleep time based on your requirements

    # Add the code to extract the text from the newly displayed information
    text_element = driver.find_element(By.CSS_SELECTOR, ".large-6.day-summary-text.day-summary-surf")

    # Get the text from the element and store it in the list
    extracted_text = text_element.text
    extracted_text_list.append(extracted_text)

    # Print the extracted text for debugging purposes
    print(f"Extracted text after interacting with button {i + 1}: {extracted_text}")

# Close the driver
driver.quit()

# You can now use the extracted_text_list variable to work with the extracted text
print("All extracted text:", extracted_text_list)
