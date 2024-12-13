from selenium_imports.common_imports import *

class RegistrationForm:
    def DemoQaReg(self , driver):
        driver.get("https://demoqa.com/automation-practice-form")
        name_field = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='firstName']"))
        )
        name_field.clear()
        name_field.send_keys("John")
        time.sleep(1)
        last_name = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='lastName']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()", last_name)
        last_name.clear()
        last_name.send_keys("Doe")
        time.sleep(1)
        email_field = WebDriverWait(driver , 10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='userEmail']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()", email_field)
        email_field.clear()
        email_field.send_keys("johndoee4@gmail.com")
        time.sleep(1)
        gender_radio = WebDriverWait(driver , 10).until(
            EC.element_to_be_clickable((By.XPATH,"//label[@for='gender-radio-1']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()", gender_radio)
        gender_radio.click()
        time.sleep(1)
        mobile_number = WebDriverWait(driver , 10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='userNumber']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()", mobile_number)
        mobile_number.clear()
        mobile_number.send_keys("0300223344")
        time.sleep(1)
        DateOfBirth = WebDriverWait(driver , 10).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='dateOfBirthInput']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()", DateOfBirth)
        DateOfBirth.click()
        time.sleep(2)
        year_dropdown = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//select[@class='react-datepicker__year-select']"))
        )
        year_dropdown_select = Select(year_dropdown)
        year_dropdown_select.select_by_visible_text("2002")
        time.sleep(2)
        month_dropdown = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//select[@class='react-datepicker__month-select']"))
        )
        month_dropdown_select = Select(month_dropdown)
        month_dropdown_select.select_by_visible_text("June")
        time.sleep(1)
        day = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//div[contains(@aria-label,'Choose Thursday, June 20th, 2002')]"))
        )
        day.click()
        time.sleep(2)
        hobbies1_field = WebDriverWait(driver , 10).until(
            EC.element_to_be_clickable((By.XPATH,"//label[@for='hobbies-checkbox-3']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()",hobbies1_field)
        hobbies1_field.click()
        time.sleep(1)
        hobbies2_field = WebDriverWait(driver , 10).until(
            EC.element_to_be_clickable((By.XPATH,"//label[@for='hobbies-checkbox-1']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()",hobbies2_field)
        hobbies2_field.click()
        time.sleep(1)
        file_input = driver.find_element(By.XPATH, "//input[@id='uploadPicture']")
        file_path = os.path.abspath(r"C:\Users\NTech\Downloads\profile-pic (5).png")
        file_input.send_keys(file_path)
        time.sleep(1)
        current_address = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//textarea[@id='currentAddress']"))
        )
        current_address.clear()
        current_address.send_keys("Lorem Ipsusm Test Address Written")
        time.sleep(1)
        select_state = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//div[@class=' css-yk16xz-control']//div[@class=' css-1hwfws3']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()",select_state)
        select_state_dropdown = Select(select_state)
        select_state_dropdown.select_by_visible_text("NCR")
        time.sleep(2)
        



        

driver = webdriver.Chrome()
driver.maximize_window()
try:
    DemoQa = RegistrationForm()
    DemoQa.DemoQaReg(driver)
finally:
    driver.quit()   