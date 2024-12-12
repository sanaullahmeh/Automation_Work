from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
time.sleep(2)

title = driver.title
print(f"title of the Page is = {title}")

plus_button = driver.find_element(By.XPATH,value="//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[2]")
plus_button.click()
time.sleep(3)


add_to_cart = driver.find_element(By.XPATH,value="//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]")
add_to_cart.click()

time.sleep(2)

cart_button = driver.find_element(By.XPATH,value="//img[@alt='Cart']")
cart_button.click()
time.sleep(2)

proceed_to_checkout= driver.find_element(By.XPATH,value="//button[normalize-space()='PROCEED TO CHECKOUT']")
proceed_to_checkout.click()
time.sleep(2)

place_order = driver.find_element(By.XPATH,value="//button[normalize-space()='Place Order']")
place_order.click()
time.sleep(2)

dropdown_element = driver.find_element(By.XPATH,value="//div[@class='wrapperTwo']//div//select")
select = Select(dropdown_element)
select.select_by_visible_text("Pakistan")
time.sleep(2)

checkbox = driver.find_element(By.XPATH,value="//input[@type='checkbox']")
checkbox.click()
time.sleep(2)

proceed_button = driver.find_element(By.XPATH,value="//button[normalize-space()='Proceed']")
proceed_button.click()
time.sleep(5)

driver.quit()