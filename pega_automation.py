from selenium_imports.common_imports import *

class LoginFunc:
    def LoginPega(self, driver):
        driver.maximize_window()
        driver.get("https://training.openspan.com/login")
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='user_name']"))
        )
        email_field.send_keys("test@gmail.com")
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='user_pass']"))
        )
        password_field.send_keys("ZZZZZZZZZZZ")
        sign_in = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='login_button']"))
        )
        sign_in.click()
        time.sleep(1)

class PegaPracSite:
    def DropDownPractice(self, driver):
        product_type = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "productType"))
        )
        product_type_dropdown = Select(product_type)
        product_type_dropdown.select_by_visible_text("Seasonings")
        time.sleep(2)

        product_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "productsList"))
        )
        product_name_dropdown = Select(product_name)
        product_name_dropdown.select_by_visible_text("Genen Shouyu")
        time.sleep(2)

        view_details = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "viewButton"))
        )
        view_details.click()
        time.sleep(2)

# Main Execution
driver = webdriver.Chrome()
try:
    login = LoginFunc()
    login.LoginPega(driver)

    pega_practice = PegaPracSite()
    pega_practice.DropDownPractice(driver)
finally:
    driver.quit()
