from selenium_imports.common_imports import *

class AssertionPractice:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    
    def checkassertion(self):
        try:
            self.driver.get("https://www.python.org/")
            pages_title = self.driver.title
            assert "Python" in pages_title , "Python Does not Found in the Title"
            print(f"Actual Title - {pages_title}")
        except AssertionError as e:
            print(f"Assertion Failed - {e}")
    def testcase_two(self):
        try:
            self.driver.get("https://www.google.com/")
            google_page_title = self.driver.title
            assert "Google" in google_page_title , "Google Page Title Does not Matched"
            print(f"Actual Title = {google_page_title}")
        except AssertionError as e:
            print(f"Assertion Failed - {e}")
    def close_driver(self):
        self.driver.quit


AssertionObj = AssertionPractice()
AssertionObj.checkassertion()
AssertionObj.testcase_two()
AssertionObj.close_driver()



        

