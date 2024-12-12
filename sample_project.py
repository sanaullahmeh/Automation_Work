from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

class SelecyByID():
    def locate_by_id(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.facebook.com/login.php/")
        email_field = driver.find_element(By.XPATH,value="//input[@id='email']")
        email_field.send_keys("Practice Test Automation")
        password_field = driver.find_element(By.XPATH,value="//input[@id='pass']")
        password_field.send_keys("Wrong Password")
        login_button = driver.find_element(By.XPATH,value="//button[@id='loginbutton']")
        login_button.click()
        time.sleep(5)

findById = SelecyByID()
findById.locate_by_id()

