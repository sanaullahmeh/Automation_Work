from selenium_imports.common_imports import *

class PracticeExcercise:
    def practice_excercise(self,driver):
        driver.get("https://www.automationexercise.com/contact_us")
        name_field = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Name']"))
        )
        name_field.clear()
        name_field.send_keys("Demo Name")
        time.sleep(1)
        email_field = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Email']"))
        )
        email_field.clear()
        email_field.send_keys("demo@gmail.com")
        time.sleep(1)
        subject = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Subject']"))
        )
        subject.send_keys("This Subject is Written Through Selenium Automation")
        time.sleep(1)
        message = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//textarea[@id='message']"))
        )
        message.send_keys("This Message is Written Through Selenium Automation ")
        time.sleep(1)
        file_upload = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@name='upload_file']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()" , file_upload)
        file_path = "Path of the File"
        file_upload.send_keys(file_path)
        time.sleep(2)
        submit_button = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@name='submit']"))
        )
        driver.execute_script("arguments[0].scrollIntoView" , submit_button)
        time.sleep(2)
        submit_button.click()
        time.sleep(2)
        alert = WebDriverWait(driver,10).until(
            EC.alert_is_present()
        )
        alert.accept()
        time.sleep(2)
        print("Contact us form is filled automatically")


driver = webdriver.Chrome()
driver.maximize_window()
try:
    PracObj = PracticeExcercise()
    PracObj.practice_excercise(driver)
finally:
    driver.quit()

