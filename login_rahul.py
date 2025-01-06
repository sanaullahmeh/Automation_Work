from selenium_imports.common_imports import *

class LoginFunctionality:
    def SignIn(self , driver):
        driver.get("https://rahulshettyacademy.com/loginpagePractise/")
        user_name = WebDriverWait(driver , 10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='username']"))
        )
        user_name.clear()
        user_name.send_keys("rahulshettyacademy")
        time.sleep(1)
        password_field = WebDriverWait(driver , 10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='password']"))
        )
        password_field.clear()
        password_field.send_keys("learning")
        time.sleep(1)
        dropdown_element = WebDriverWait(driver , 10).until(
            EC.element_to_be_clickable((By.XPATH,"//select[@class='form-control']"))
        )
        dropdown_element_select = Select(dropdown_element)
        dropdown_element_select.select_by_visible_text("Teacher")
        time.sleep(2)
        terms_checkbox = WebDriverWait(driver , 10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='terms']"))
        )
        terms_checkbox.click()
        time.sleep(1)
        submit_button = WebDriverWait(driver , 10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='signInBtn']"))
        )
        submit_button.click()
        time.sleep(5)

driver = webdriver.Chrome()
driver.maximize_window()
try:
    loginObj = LoginFunctionality()
    loginObj.SignIn(driver)
finally:
    driver.quit()


