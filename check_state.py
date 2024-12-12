from selenium_imports.common_imports import *

class CheckState:
    def enable_disable(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://training.openspan.com/login")
        email_field = WebDriverWait(driver , 10).until(
            EC.presence_of_element_located((By.XPATH,"//input[@id='user_name']"))
        )
        email_field.send_keys("test@gmail.com")
        password_field = WebDriverWait(driver , 10).until(
            EC.presence_of_element_located((By.XPATH,"//input[@id='user_pass']"))
        )
        password_field.send_keys("ZZZZZZZZZZZ")
        sign_in = WebDriverWait(driver , 10).until(
            EC.presence_of_element_located((By.XPATH,"//input[@id='login_button']"))
        )
        sign_in.click()
        time.sleep(1)
        title = driver.title
        print(f"Title of the Page - {title}")

        products = WebDriverWait(driver , 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Products']"))
        )

        products.click()

        time.sleep(1)
        bevrages = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@title='Beverages']"))
        )
        bevrages.click()
        bevrage_page_title = driver.title
        print(f"Bevrage's Page Title = {bevrage_page_title}")

        time.sleep(1)
        specific_product = WebDriverWait(driver , 10).until(
            EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='Cote de Blaye']"))
        )
        specific_product.click()
        specific_product_title = driver.title
        print(f"Title of Specific Product is {specific_product_title}")
        time.sleep(1)
        product_quantity = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.NAME,"product_quantity"))
        )
        select = Select(product_quantity)
        select.select_by_visible_text("5")
        time.sleep(1)
        
        order_buttton = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.ID,"login_button"))
        )
        order_buttton.click()
        time.sleep(1)

        continue_shopping = WebDriverWait(driver ,10).until(
            EC.element_to_be_clickable((By.XPATH,"//tbody//tr//input[1]"))
        )
        continue_shopping.click()
        time.sleep(1)
        driver.quit()

objCs = CheckState()
objCs.enable_disable()
  


    
