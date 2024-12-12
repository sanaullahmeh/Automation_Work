from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()

time.sleep(5)

search_field = driver.find_element(By.NAME,value="q")
search_field.send_keys("Pak vs zim live score")
search_field.send_keys(Keys.RETURN)
time.sleep(5)
driver.quit()