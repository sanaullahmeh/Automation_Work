from selenium_imports.common_imports import *

class ScrollBar:
    def handling_scroll(self,driver):
        driver.get("https://trytestingthis.netlify.app/")
        slider = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.ID ,"a"))
        )
        driver.execute_script("arguments[0].scrollIntoView()" , slider)
        actions = ActionChains(driver)
        actions.click_and_hold(slider).move_by_offset(0,5).release().perform()
        time.sleep(2)
driver = webdriver.Chrome()
driver.maximize_window()
try:
    Runner = ScrollBar()
    Runner.handling_scroll(driver)
finally:
    driver.close()
