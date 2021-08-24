import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from dataLibrary.HomepgData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# running pytest in cmd prompt
# C:\Users\stuga\PycharmProjects\pythonProject1\pySelenium>py.test test_Demo.py -v -s for detailed log & display prints
# --html=report.html
# -k is used to ask pytest to search for keywords - used in group testing
# -m for mark

class TestBa(BaseClass):
    def test_ba(self, getData):
        driver = self.driver
        log = self.getLogger()
        homepage = HomePage(self.driver)
        ctrClick = Keys.CONTROL + Keys.ENTER
        # should be on another pageObjectModel page
        homepage.getZero().send_keys(ctrClick)
        log.info("new window opened")

        driver.execute_script("window.scrollTo(0, 900);")
        homepage.gethols().click()  # might not get auto suggestions for '.click()'
        homepage.catchFlight().click()
        driver.execute_script("window.scrollTo(0, 800);")
        log.info("page scrolled")
        self.waiter(By.CSS_SELECTOR, "span[class*='month-name'] span")
        while driver.find_element_by_css_selector("span[class*='month-name'] span").text != "September":
            time.sleep(1)
            homepage.next().click()
            time.sleep(1)
        dates = homepage.calender()
        for date in dates:
            self.waiter(By.XPATH, "//tbody/tr/td/div/span")
            if date.text == getData["travelDate"]:
                date.click()
                break
        log.info("flight date selected")
        homepage.getAirport().send_keys("lon")
        airports = homepage.chooseAirport()
        for airport in airports:
            destination = airport.text
            if getData["homeAirport"] in destination:
                airport.click()
                break
        arrive = driver.find_element_by_id("to")
        arrive.send_keys(getData["destination"])
        arrive.send_keys(Keys.ENTER)
        homepage.getPax().click()
        homepage.getOne().click()
        homepage.getTwo().click()
        homepage.getThree().click()
        self.selector(homepage.getSelect(), getData["childAge"])
        homepage.getFour().click()
        homepage.getFive().click()
        homepage.getSix().click()
        homepage.getSeven().click()
        homepage.getEight().click()
        homepage.getNine().click()
        log.info("holidays booked!")
        time.sleep(3)
        driver.back()

        driver.switch_to.window(driver.window_handles[-1])
        log.info(driver.title)

    @pytest.fixture(params=HomePageData.test_HomePageData)
    def getData(self, request):
        return request.param

    # @pytest.fixture(params=HomePageData.getTestData("Client"))
    # def getData(self, request):
    # return request.param
