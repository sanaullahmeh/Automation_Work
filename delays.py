from selenium_imports.common_imports import *

class Delays:
    def handling_alerts(self, driver):
        driver.get("https://practice-automation.com/javascript-delays/")
        
        # Wait for the button and click it
        click_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='start']"))
        )
        click_btn.click()
        
        # Wait for the delayed input field to contain the expected value
        WebDriverWait(driver, 15).until(
            lambda d: d.find_element(By.XPATH, "//input[@id='delay']").get_attribute("value") == "Liftoff!"
        )
        
        # Locate the text field element
        text_field = driver.find_element(By.XPATH, "//input[@id='delay']")
        
        # Scroll to the text field
        driver.execute_script("arguments[0].scrollIntoView();", text_field)
        
        # Assert and print the value of the input field
        assert "Liftoff!" in text_field.get_attribute("value"), "Expected text 'Liftoff!' not found in the field"
        print("Text in field:", text_field.get_attribute("value"))

# Instantiate the driver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    Runner = Delays()
    Runner.handling_alerts(driver)
finally:
    driver.quit()