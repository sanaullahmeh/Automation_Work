from selenium_imports.common_imports import *

class MultiForm:
    def golbal_sqa_multiform(self,driver):
        driver.get("https://www.globalsqa.com/angularJs-protractor/Multiform/#/form/profile")
        name = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@name='name']"))
        )
        name.clear()
        name.send_keys("Roreck Knit")
        time.sleep(1)
        email_field = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@name='email']"))
        )
        email_field.clear()
        email_field.send_keys("roreck@gmail.com")
        time.sleep(2)
        next_section_button = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH<"//a[@class='btn btn-block btn-info']"))
        )
        next_section_button.click()
        print("1st Form Done")
    def second_form (self,driver):
        console_checkbox = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@name='00O']"))
        )
        console_checkbox.click()
        nextt_section_button = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//a[@class='btn btn-block btn-info']"))
        )
        nextt_section_button.click()
        time.sleep(2)
driver = webdriver.Chrome()
driver.maximize_window()
try:
    Runner = MultiForm()
    Runner.golbal_sqa_multiform(driver)
    Runner.second_form(driver)
finally:
    driver.quit()