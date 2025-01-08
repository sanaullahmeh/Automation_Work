from selenium_imports.common_imports import *

class Draggable:
    def handling_draggable(self,driver):
        driver.get("https://www.way2automation.com/way2auto_jquery/draggable.php#load_box")
        WebDriverWait(driver,10).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@src='draggable/default.html']"))
        )

        draggable_element = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//div[@id='draggable']"))
        )
        action = ActionChains(driver)
        action.click_and_hold(draggable_element).move_by_offset(100,100).release().perform()
        time.sleep(3)
        print("Drag and Dropeed Completed")
driver = webdriver.Chrome()
driver.maximize_window()
try:
    Executer = Draggable()
    Executer.handling_draggable(driver)
finally:
    driver.quit()