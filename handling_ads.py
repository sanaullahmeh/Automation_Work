from selenium_imports.common_imports import *

class HandlingAds:
    def Ads(self,driver):
        driver.get("https://practice-automation.com/ads/")
        Ads_element = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"div[id='popmake-1272'] button[aria-label='Close']"))
        )
        Ads_element.click()
        print("Ad is Closed Successfully")

driver = webdriver.Chrome()
driver.maximize_window()
try:
    AdsObj = HandlingAds()
    AdsObj.Ads(driver)
finally:
    driver.quit()
