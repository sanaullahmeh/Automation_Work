from selenium_imports.common_imports import *
class ActionsPractice:
    def WebActions(self ,driver):
        driver.get("https://webdriveruniversity.com/Actions/index.html")
        actions = ActionChains(driver)
        dragged_element = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//b[normalize-space()='DRAG ME TO MY TARGET!']"))
        )
        dropped_element = WebDriverWait(driver ,10).until(
            EC.element_to_be_clickable((By.XPATH,"//b[normalize-space()='DROP HERE!']"))
        )
        actions.drag_and_drop(dragged_element,dropped_element).perform()
        print("Drag and Dropped action performed successfully!")
        time.sleep(1)
    def DoubleClick(self ,driver):
        actions = ActionChains(driver)
        DoublleClick =WebDriverWait(driver , 10).until(
            EC.element_to_be_clickable((By.XPATH,"//div[@id='double-click']"))
        )
        actions.double_click(DoublleClick).perform()
        print("Double Click action performed successfully!")
        time.sleep(1)
    def MouseHover(self,driver):
        actions = ActionChains(driver)
        FirstHover = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Hover Over Me First!']"))
        )
        actions.move_to_element(FirstHover).perform()
        time.sleep(1)
        print("First Hover Successful")
        SecondHover = WebDriverWait(driver ,10).until(
            EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Hover Over Me Second!']"))
        )
        actions.move_to_element(SecondHover).perform()
        time.sleep(1)
        print("Second Hover Successful")
        ThirdHover = WebDriverWait(driver , 10).until(
            EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Hover Over Me Third!']"))
        )
        actions.move_to_element(ThirdHover).perform()
        time.sleep(1)
        print("Third Hover Successful")
driver = webdriver.Chrome()
driver.maximize_window()
try:
    actionsObj = ActionsPractice()
    actionsObj.WebActions(driver)
    actionsObj.DoubleClick(driver)
    actionsObj.MouseHover(driver)
finally:
    driver.quit()