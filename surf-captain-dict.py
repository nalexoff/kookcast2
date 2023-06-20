from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome WebDriver options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run browser in headless mode for faster execution (optional)

# Create a new instance of the Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the URL
url = "https://surfcaptain.com/forecast/southampton-new-york"
driver.get(url)

# Find all the elements with the class name "summary-day-expand"
buttons = driver.find_elements(By.CLASS_NAME, "summary-day-expand")

# Initialize an empty list to store the extracted dictionaries after each button interaction
extracted_dicts_list = []

# Define a function to extract data from the page after interacting with a button
def extract_data():
    # Find the specified elements and store the text in a dictionary
    summary_day_text = driver.find_element(By.CLASS_NAME, "summary-day-text").text
    day_summary_surf = driver.find_element(By.CSS_SELECTOR, ".large-6.day-summary-text.day-summary-surf").text
    day_summary_cond = driver.find_element(By.CSS_SELECTOR, ".large-6.day-summary-text.day-summary-cond").text
    day_hour_txt = driver.find_element(By.CSS_SELECTOR, "div[class^='day-hour-txt']").text
    wind_elements = [driver.find_element(By.XPATH, f"//tr[{i + 1}]/td[2]").text for i in range(5)]
    swell_elements = [driver.find_elements(By.CSS_SELECTOR, f"tr:nth-child({i + 1}) .hourly-swell") for i in range(5)]

    # Find all elements matching the CSS selector and store them in a list
    tide_elements = driver.find_elements(By.CSS_SELECTOR, ".cell.small-3.medium-4.large-3.day-details-value")

    # Extract text from the elements using their index
    am_lowtide_label = tide_elements[0].text
    am_lowtide_value = tide_elements[1].text
    am_lowtide = f"{am_lowtide_label}: {am_lowtide_value}"

    am_hightide_label = tide_elements[2].text
    am_hightide_value = tide_elements[3].text
    am_hightide = f"{am_hightide_label}: {am_hightide_value}"

    pm_lowtide_label = tide_elements[4].text
    pm_lowtide_value = tide_elements[5].text
    pm_lowtide = f"{pm_lowtide_label}: {pm_lowtide_value}"

    pm_hightide_label = tide_elements[6].text
    pm_hightide_value = tide_elements[7].text
    pm_hightide = f"{pm_hightide_label}: {pm_hightide_value}"

    extracted_dict = {
        "summary_day_text": summary_day_text,
        "day_summary_surf": day_summary_surf,
        "day_summary_cond": day_summary_cond,
        "day_hour_txt": day_hour_txt,
        "6am_wind": wind_elements[0],
        "9am_wind": wind_elements[1],
        "12pm_wind": wind_elements[2],
        "3pm_wind": wind_elements[3],
        "6pm_wind": wind_elements[4],
        "6am_swell": [swell.text for swell in swell_elements[0]],
        "9am_swell": [swell.text for swell in swell_elements[1]],
        "12pm_swell": [swell.text for swell in swell_elements[2]],
        "3pm_swell": [swell.text for swell in swell_elements[3]],
        "6pm_swell": [swell.text for swell in swell_elements[4]],
        "am_lowtide": am_lowtide,
        "am_hightide": am_hightide,
        "pm_lowtide": pm_lowtide,
        "pm_hightide": pm_hightide,
    }

    # Append the dictionary to the list
    extracted_dicts_list.append(extracted_dict)

    # Print the extracted dictionary for debugging purposes
    print(f"Extracted data after interacting with button {i + 1}: {extracted_dict}")

# Iterate through the first three buttons in the list of found elements and interact with them individually
for i, button in enumerate(buttons[:3]):
    # Perform your desired action with the button
    print(f"Interacting with button {i + 1}")

    # Use JavaScript to click the element
    driver.execute_script("arguments[0].click();", button)

    # Add wait time between button interactions
    time.sleep(3)  # Adjust the sleep time based on your requirements

    # Call the extract_data function to extract data from the page
    extract_data()

# Close the driver
driver.quit()

# You can now use the extracted_dicts_list variable to work with the extracted data
print("All extracted data:", extracted_dicts_list)

# sample for identifying variables per dictionary in the extracted_dicts_list list
data = extracted_dicts_list

day1_6am_wind = data[0]['6am_wind']
day2_6am_wind = data[1]['6am_wind']
day3_6am_wind = data[2]['6am_wind']

print(day1_6am_wind)
print(day2_6am_wind)
print(day3_6am_wind)
