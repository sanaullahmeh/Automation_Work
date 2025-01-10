from selenium_imports.common_imports import *

class RadioButtons:
    def handling_radio_buttons(self,driver):
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        radio_buttons = WebDriverWait(driver,10).until(
            EC.presence_of_all_elements_located((By.XPATH,"//input[@name='radioButton']"))
        )
        print(len(radio_buttons))
        for radio_button in radio_buttons:
            if radio_button.get_attribute("value") == "radio2":
                radio_button.click()
                assert radio_button.is_selected()
                break
        time.sleep(2)

driver = webdriver.Chrome()
driver.maximize_window()
try:
    Run = RadioButtons()
    Run.handling_radio_buttons(driver)
finally:
    driver.quit()
                