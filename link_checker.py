from selenium_imports.common_imports import *

class LinkChecker:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.base_url = "https://tristatedesigns.com/"  
    def get_links(self):  
        self.driver.get(self.base_url)
        elements = self.driver.find_elements(By.TAG_NAME, "a")
        links = [element.get_attribute("href") for element in elements if element.get_attribute("href")]
        return links
    def check_links(self, links):
        error_links = []
        for link in links:
            try:
                response = requests.get(link, timeout=10)
                if 400 <= response.status_code < 600:
                    error_links.append((link, response.status_code))
            except requests.exceptions.RequestException as e:
                error_links.append((link, str(e)))
        return error_links
    def run(self):
        links = self.get_links()
        print(f"Total links found on the website: {len(links)}")
        error_links = self.check_links(links)
        print(f"Total No of Error Links - {len(error_links)}")
        if error_links:
            print("\nLinks with errors:")
            for url, status in error_links:
                print(f"{url} - Error Code: {status}")
        else:
            print("No broken links found!")
        self.driver.quit()
checker = LinkChecker()
checker.run()
