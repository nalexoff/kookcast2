from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a new Chrome browser instance
driver = webdriver.Chrome()

# Navigate to the SurfCaptain website
driver.get('https://surfcaptain.com/forecast/southampton-new-york')

# Find and click the summary-day-expand button
expand_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.summary-day-expand')))
expand_button.click()

# Wait for 10 seconds
time.sleep(10)

# Close the browser
driver.quit()
