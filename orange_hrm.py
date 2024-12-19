from selenium_imports.common_imports import *

class OrangeHRM:
    def Login(self,driver):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        username_field = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Username']"))
        )
        username_field.clear()
        username_field.send_keys("Admin")
        password_field = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Password']"))
        )
        password_field.clear()
        password_field.send_keys("admin123")
        submit_button = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']"))
        )
        submit_button.click()
        time.sleep(2)
        Actual_title = driver.title
        Expected_title = "OrangeHRM"
        if Actual_title == Expected_title:
            print("Title is Same as Expected")
        else:
            print("Title Did not matched")
        
driver = webdriver.Chrome()
driver.maximize_window()
try:
    OrangeHrmObj = OrangeHRM()
    OrangeHrmObj.Login(driver)
finally:
    driver.quit()