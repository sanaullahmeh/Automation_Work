from selenium_imports.common_imports import *

class LoginTestPrac:
    def login_test(self,driver):
        driver.get("https://trytestingthis.netlify.app/")
        username = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.ID,"uname"))
        )
        driver.execute_script("arguments[0].scrollIntoView()" , username)
        username.send_keys("test")
        time.sleep(2)
        pass_field =WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.ID,"pwd"))
        )
        driver.execute_script("arguments[0].scrollIntoView()" , pass_field)
        pass_field.send_keys("test")
        time.sleep(1)
        click_login_button = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@value='Login']"))
        )
        click_login_button.click()
        assert "Login Success" in driver.title
        print(driver.title)
driver = webdriver.Chrome()
driver.maximize_window()
try:
    RunTest = LoginTestPrac()
    RunTest.login_test(driver)
finally:
    driver.close()