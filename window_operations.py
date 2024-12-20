from selenium_imports.common_imports import *

class Windowsoperations:
    def WindowFunctions(self,driver):
        driver.get("https://practice-automation.com/window-operations/")
        new_tab_button = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.ID,"//b[normalize-space()='New Tab']"))
        )
        new_tab_button.click()
        time.sleep(2)
driver = webdriver.Chrome()
driver.maximize_window()
try:
    WindowObj = Windowsoperations()
    WindowObj.WindowFunctions(driver)
finally:
    driver.quit()