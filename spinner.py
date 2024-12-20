from selenium_imports.common_imports import *

class LoadingPage:
    def SpinnerPrac(self,driver):
        driver.get("https://practice-automation.com/")
        spinner_element = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='Spinners']"))
        )
        driver.execute_script("arguments[0]" , spinner_element)
        time.sleep(2)
        spinner_element.click()

driver = webdriver.Chrome()
driver.maximize_window()
try:
    LoadingObj = LoadingPage();
    LoadingObj.SpinnerPrac(driver)
finally:
    driver.quit()