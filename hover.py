from selenium_imports.common_imports import *

class MouseHover:
    def handling_mouse_hover (self,driver):
        driver.get("https://practice-automation.com/hover/")
        action = ActionChains(driver)
        hover_element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"//h3[@id='mouse_over']"))
        )
        action.move_to_element(hover_element).perform()
        time.sleep(2)
        print("Mouse Hover Action Performed Successfully")

driver = webdriver.Chrome()
driver.maximize_window()
try:
    HoverChecker = MouseHover()
    HoverChecker.handling_mouse_hover(driver)
finally:
    driver.quit()
        