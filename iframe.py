import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the URL and maximize the window
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")  # Example dynamic page URL

# Wait for the "Start" button to be clickable and click it
start_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Start']"))
)
start_button.click()

# Wait for the "Hello World!" message to appear after dynamic loading
hello_world_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h4[text()='Hello World!']"))
)

# Print the message after it appears
print(hello_world_message.text)

# Optionally, refresh the page and repeat the actions
driver.refresh()

# Wait for the "Start" button to be clickable again after the page refresh
start_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Start']"))
)
start_button.click()

# Wait for the message to appear again after dynamic loading
hello_world_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h4[text()='Hello World!']"))
)

# Print the message again after it appears
print(hello_world_message.text)

# Quit the browser after finishing the tasks
driver.quit()
