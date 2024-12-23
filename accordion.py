from selenium_imports.common_imports import *

class Accordion:
    def SeeMore(self,driver):
        driver.get("https://practice-automation.com/accordions/")
        seeMore_button = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.TAG_NAME,"Summary"))
        )
        seeMore_button.click()
        expected_text = "This is an accordion item."
        actual_text_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='This is an accordion item.']"))
        )

         # Extract the text
        actual_text = actual_text_element.text
        if actual_text == expected_text:
            print(f"Content Matched")
        else:
            print("Content does not matched")

driver = webdriver.Chrome()
driver.maximize_window()
try:
    AccordionObj = Accordion()
    AccordionObj.SeeMore(driver)
finally:
    driver.quit()