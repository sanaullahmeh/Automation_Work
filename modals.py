from selenium_imports.common_imports import *

class Modals:
    def HandlingModals(self,driver):
        driver.get("https://practice-automation.com/modals/")
        modal_element = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.ID,"simpleModal"))
        )
        modal_element.click()
        close_modal = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"div[id='popmake-1318'] button[aria-label='Close']"))
        )
        close_modal.click()
        print("Modal is Closed Successfully")
    def form_modal(self,driver):
        form_modal = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.ID,"formModal"))
        )
        form_modal.click()
        print("Form Modal Clicked Successfully")
        name_field = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.ID,"g1051-name"))
        )
        name_field.send_keys("Wrecked Savye")
        email_field= WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.ID,"g1051-email"))
        )
        email_field.send_keys("wreckedsavvy@gmail.com")
        message_field = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.ID,"contact-form-comment-g1051-message"))
        )
        message_field.send_keys(" Lorem Ipsum Lorem Lorem Lorem Lorem Lorem Lorem")
        submit_button = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Submit']"))
        )
        driver.execute_script("arguments[0].scrollIntoView()" ,submit_button)
        submit_button.click()
        print("Modal Form is Submitted and Modals Excercise Done")

driver = webdriver.Chrome()
driver.maximize_window()
try:
    ModalObj = Modals()
    ModalObj.HandlingModals(driver)
    ModalObj.form_modal(driver)
finally:
    driver.quit()