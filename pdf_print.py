from selenium_imports.common_imports import *



pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_prints_page(driver):
    driver.get("https://www.selenium.dev/")
    print_options = PrintOptions()
    pdf = driver.print_page(print_options)
    assert len(pdf) > 0 