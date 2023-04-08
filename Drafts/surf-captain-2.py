from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

url = 'https://surfcaptain.com/forecast/southampton-new-york'

# Configure Chrome options
chrome_options = Options()
# chrome_options.add_argument('--headless')  # Uncomment to run Chrome in headless mode for faster execution

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Set an implicit wait time
driver.implicitly_wait(10)

# Navigate to the URL
driver.get(url)

try:
    # Interact with each summary-day-expand div one by one
    for index in range(1, 4):
        xpath = f'//*[@id="fcst-summary"]/div[2]/div/div/ul/li[{index}]/div[1]/div[3]/div'
        expand_div = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))

        # Move to the expand_div element
        actions = ActionChains(driver)
        actions.move_to_element(expand_div).perform()
        time.sleep(1)

        # Interact with the expand_div
        expand_div.click()
        print(f'Interacted with expand div {index}')
        time.sleep(1)  # Adjust the sleep time based on your requirements

finally:
    # Close the WebDriver
    driver.quit()
