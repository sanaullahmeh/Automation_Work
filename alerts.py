from selenium_imports.common_imports import *

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the URL and maximize the window
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# Wait for the "jsAlert" button to be present and clickable
js_alert = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@onclick='jsAlert()']"))
)

# Click the "jsAlert" button
js_alert.click()

# Wait for the alert to be present
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

# Dismiss the alert
alert.dismiss()

# Optional: wait before closing the browser (to observe the result)
time.sleep(3)

# Quit the browser
driver.quit()
