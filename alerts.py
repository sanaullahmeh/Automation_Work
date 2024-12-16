from selenium_imports.common_imports import *

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the URL and maximize the window
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
js_alert = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@onclick='jsAlert()']"))
)
js_alert.click()
time.sleep(2)
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert.dismiss()
time.sleep(3)

js_confirm = WebDriverWait(driver ,10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@onclick='jsConfirm()']"))
)
js_confirm.click()
time.sleep(2)
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert.accept()
time.sleep(2)
js_prompt = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"//button[@onclick='jsPrompt()']"))
)
js_prompt.click()
time.sleep(1)
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert.send_keys("Handling Prompt Alert With Selenium Automation")
time.sleep(3)
alert.accept()
time.sleep(3)
print("Handled All the Js Alerts Successfully")
driver.quit()
