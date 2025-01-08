from selenium_imports.common_imports import *

class Resizable:
    def handling_resizable(self,driver):
        driver.get("https://www.way2automation.com/way2auto_jquery/resizable.php#load_box")
        WebDriverWait(driver,10).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@src='resizable/default.html']"))
        )
        time.sleep(2)
        resizeable_element = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']"))
        )
        size = resizeable_element.size
        print(f"Current size: {size['width']} x {size['height']}")

        action = ActionChains(driver)
        action.click_and_hold(resizeable_element).move_by_offset(80,95).release().perform()
        print("Resizable Element Automated")
        time.sleep(5)
driver = webdriver.Chrome()
driver.maximize_window()
try:
    Run = Resizable()
    Run.handling_resizable(driver)
finally:
    driver.quit()

