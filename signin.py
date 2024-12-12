from selenium_imports.common_imports import *

class SignUp:
    def SignUpFunctionality(self,driver):
        driver.get("https://www.browserstack.com/users/sign_in")
        email_field = WebDriverWait(driver , 10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='user_email_login']"))
        )
        email_field.send_keys("sanaullahmehrani4@gmail.com")
        time.sleep(2)
        password_field = WebDriverWait(driver , 10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='user_password']"))
        )
        password_field.send_keys("this is Password")
        time.sleep(2)
        login_button = WebDriverWait(driver , 10).untill(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='user_submit']"))
        )
        login_button.click()
        time.sleep(2)
driver = webdriver.Chrome()     
try:
    SignupObj = SignUp()
    SignupObj.SignUpFunctionality(driver)  
finally:
        driver.quit()     