from selenium_imports.common_imports import *
from faker import Faker

class AutomationExcercies:
    def SignUpProcess(self,driver):
        driver.get("https://www.automationexercise.com/signup")
        fake = Faker()
        name = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Name']"))
        )
        random_name = fake.name()
        name.clear()
        name.send_keys(random_name)
        time.sleep(1)
        
        random_email = fake.email()
        email_field = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"input[data-qa='signup-email']"))
        )
        email_field.clear()
        email_field.send_keys(random_email)
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
    def AddressInformation(self ,driver):
        first_name = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='first_name']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()",first_name)
        first_name.clear()
        first_name.send_keys("Rixxer")
        time.sleep(2)
        last_name = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='last_name']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()",first_name)
        last_name.clear()
        last_name.send_keys("Deggon")
        time.sleep(2)
        company_name = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='company']"))
        )
        company_name.clear()
        company_name.send_keys("Dekkon")
        time.sleep(2)
        Address_one = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='address1']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()" , Address_one)
        Address_one.clear()
        Address_one.send_keys("Random Address Number One")
        time.sleep(1)
        Address_two = WebDriverWait(driver ,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='address2']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()" , Address_two)
        Address_two.clear()
        Address_two.send_keys("My Random Address Number 2 Street Unknown House No 22")
        time.sleep(1)
        country = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//select[@id='country']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()" , country)
        country_dropdown = Select(country)
        country_dropdown.select_by_visible_text("Canada")
        time.sleep(1)
        state = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='state']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()" , state)
        state.clear()
        state.send_keys("British Columbia")
        time.sleep(1)
        city = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='city']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()" , city)
        city.clear()
        city.send_keys("Vancouver")
        time.sleep(1)
        zip_code = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='zipcode']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()" , zip_code)
        zip_code.clear()
        zip_code.send_keys("87689")
        time.sleep(2)
        Mobile_number = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='mobile_number']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()" , Mobile_number)
        Mobile_number.clear()
        Mobile_number.send_keys("023200892123")
        time.sleep(1)
        create_account = WebDriverWait(driver ,10).until(
            EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Create Account']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()" , Mobile_number)
        create_account.click()
        time.sleep(2)
        continue_button = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//a[@class='btn btn-primary']"))
        )
        continue_button.click()
        time.sleep(2)
        print("Automation Excercise Website Signup Page Automated Successfully")
driver = webdriver.Chrome()
driver.maximize_window()
try:
    AutomationExcerciesObj = AutomationExcercies()
    AutomationExcerciesObj.SignUpProcess(driver)
    AutomationExcerciesObj.RegistrationDetails(driver)
    AutomationExcerciesObj.DateOfBirth(driver)
    AutomationExcerciesObj.NewsLetterSection(driver)
    AutomationExcerciesObj.AddressInformation(driver)
finally:
    driver.quit()