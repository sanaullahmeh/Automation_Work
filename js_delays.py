from selenium_imports.common_imports import *

class JsDelays:
    def Delays(self, driver):
        # Navigate to the target URL
        driver.get("https://practice-automation.com/javascript-delays/")
        
        # Wait for the 'start' button to be clickable and click it
        start_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "start"))
        )
        start_button.click()
        
        # Wait for the 'delay' field to contain the text 'Liftoff!'
        liftoff_text = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "delay"), "Liftoff!")
        )
        
        # Validate if the text appeared
        if liftoff_text:
            print("Test Passed: 'Liftoff!' text appeared.")
        else:
            print("Test Failed: 'Liftoff!' text did not appear within the timeout.")

# Create an object of JsDelays and run the program
if __name__ == "__main__":
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # Ensure you have the appropriate WebDriver installed and configured
    
    try:
        # Create an object of the class
        js_delays = JsDelays()
        
        # Call the Delays method
        js_delays.Delays(driver)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the WebDriver
        driver.quit()