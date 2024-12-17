from selenium_imports.common_imports import *

class SauceDemo:
    def SauceDemoAutomation(self ,driver):
        driver.get("https://www.saucedemo.com/")
        user_name = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='user-name']"))
        )
        user_name.clear()
        user_name.send_keys("standard_user")
        time.sleep(2)
        password = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='password']"))
        )
        password.clear()
        password.send_keys("secret_sauce")
        time.sleep(1)
        login_button = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='login-button']"))
        )
        login_button.click()
        time.sleep(1)
        print("Login Successful")
        expected_title = "Swag Labs"
        actual_title = driver.title
        if expected_title ==actual_title:
            print("Title Matched Successfully")
        else:
            print("title does not matched")
        

        #assert actual_title == expected_title, f"Title mismatch! Expected: '{expected_title}', but got: '{actual_title}'"
        #print("Title Matched Successfully")
    def AddProducts(self , driver):
        product1 = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']"))
        )
        product1.click()
        product2 = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()" , product2)
        product2.click()
        time.sleep(2)
        print("Products Added Successfully to Cart")
        add_to_cart = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//a[@class='shopping_cart_link']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()" , add_to_cart)
        add_to_cart.click()
        time.sleep(2)
        checkout = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//button[@id='checkout']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()" , checkout)
        checkout.click()
        time.sleep(2)
        print("Checkout Process Done")
    def ContactInformation(self,driver):
        first_name = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='first-name']"))
        )
        first_name.clear()
        first_name.send_keys("Jack")
        time.sleep(1)
        last_name = WebDriverWait(driver ,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='last-name']"))
        )
        last_name.clear()
        last_name.send_keys("Wills")
        time.sleep(1)
        Zip_code = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='postal-code']"))
        )
        Zip_code.clear()
        Zip_code.send_keys("01901")
        time.sleep(1)
        continue_button = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='continue']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()" ,continue_button)
        continue_button.click()
        time.sleep(2)
        print("Contact Details Added Successfully")
        finish_button = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//button[@id='finish']"))
        )
        driver.execute_script("arguments[0].scrollIntoView" , finish_button)
        finish_button.click()
        time.sleep(2)
        back_to_products = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//button[@id='back-to-products']"))
        )
        back_to_products.click()
        time.sleep(2)
        print("Back to Home button Clicked")
driver = webdriver.Chrome()
driver.maximize_window()
try:
    SauceDemoObj = SauceDemo()
    SauceDemoObj.SauceDemoAutomation(driver)
    SauceDemoObj.AddProducts(driver)
    SauceDemoObj.ContactInformation(driver)
finally:
    driver.quit()
