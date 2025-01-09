from selenium_imports.common_imports import *

class DynamicDropDown:
    def handling_autosuggestive_dropdown(self,driver):
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        dynamic_dropdown_field = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@placeholder = 'Type to Select Countries']"))
        )
        dynamic_dropdown_field.send_keys("Pa")
        suggestions = WebDriverWait(driver,10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR,".ui-menu-item div"))
        )
        for suggestion in suggestions:
            if suggestion.text == "Pakistan" :
             suggestion.click()
             break
        selected_value = dynamic_dropdown_field.get_attribute("value")
        assert selected_value == "Pakistan", f"Assertion failed! Expected 'Pakistan', but got '{selected_value}'."
            

driver = webdriver.Chrome()
driver.maximize_window()
try:
   Run = DynamicDropDown()
   Run.handling_autosuggestive_dropdown(driver)
finally:
   driver.quit()
