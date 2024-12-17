from selenium_imports.common_imports import *

class AutomationExcercies:
    def SignUpProcess(self,driver):
        driver.get("https://www.automationexercise.com/signup")
        name = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Name']"))
        )
        name.clear()
        name.send_keys("Rixxer")
        time.sleep(1)
        email_field = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"input[data-qa='signup-email']"))
        )
        email_field.clear()
        email_field.send_keys("rixxer42@gmail.com")
        time.sleep(1)
        SignUpButton = WebDriverWait(driver , 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Signup']"))
        )
        SignUpButton.click()
        time.sleep(1)
    def RegistrationDetails(self , driver):
        Personstitle = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.ID,"uniform-id_gender1"))
        )
        Personstitle.click()
        time.sleep(2)
        password = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='password']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()" , password)
        password.send_keys("Rixer2288")
        time.sleep(2)
    def DateOfBirth(self,driver):
        Days = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//select[@id='days']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()" , Days)
        selectDays = Select(Days)
        selectDays.select_by_visible_text("10")
        time.sleep(1)
        Months = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//select[@id='months']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()" , Days)
        selectMonths = Select(Months)
        selectMonths.select_by_visible_text("October")
        time.sleep(1)
        Year = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//select[@id='years']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()" , Months)
        selectYear = Select(Year)
        selectYear.select_by_visible_text("2010")
        time.sleep(1)
    def NewsLetterSection(self ,driver):
        NewsLetter = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='newsletter']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()",NewsLetter)
        NewsLetter.click()
        time.sleep(1)
        Offers = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='optin']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()",Offers)
        Offers.click()
        time.sleep(2)






driver = webdriver.Chrome()
driver.maximize_window()
try:
    AutomationExcerciesObj = AutomationExcercies()
    AutomationExcerciesObj.SignUpProcess(driver)
    AutomationExcerciesObj.RegistrationDetails(driver)
    AutomationExcerciesObj.DateOfBirth(driver)
    AutomationExcerciesObj.NewsLetterSection(driver)
finally:
    driver.quit()