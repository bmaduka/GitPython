import time

import pytest
from selenium.webdriver.chrome import webdriver

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope='class')
def loadUp(request):
    global driver
    chrome_Options = webdriver.Options()
    chrome_Options.add_argument("headless")

    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.WebDriver(executable_path='C:\\chromedriver.exe', options=chrome_Options)

    elif browser_name == "firefox":
        print("firefox")

    driver.implicitly_wait(7)
    driver.maximize_window()
    driver.get("https://www.britishairways.com")
    request.cls.driver = driver

    yield
    time.sleep(3)
    driver.quit()
