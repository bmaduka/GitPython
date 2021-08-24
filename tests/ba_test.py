import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class TestBa(BaseClass):
    def test_ba(self):
        #driver = webdriver.WebDriver(executable_path="C:\\chromedriver.exe")
        driver = self.driver
        #driver.implicitly_wait(7)
        #driver.maximize_window()
        #driver.get("https://www.britishairways.com")
        ctrClick = Keys.CONTROL+Keys.ENTER
        driver.find_element_by_css_selector("a[title*='home page']").send_keys(ctrClick)
        driver.execute_script("window.scrollTo(0, 900);")
        driver.find_element_by_id("flightAndHotelTab").click()
        driver.find_element_by_xpath("//div[@id='flightandhotel-outbound-date-selector']").click()
        driver.execute_script("window.scrollTo(0, 800);")
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span[class*='month-name'] span")))
        month = driver.find_element_by_css_selector("span[class*='month-name'] span").text
        while driver.find_element_by_css_selector("span[class*='month-name'] span").text != "September":
            time.sleep(1)
            forward = driver.find_element_by_css_selector("span[class*='next-month'] span")
            forward.click()
            month = driver.find_element_by_css_selector("span[class*='month-name'] span").text
            time.sleep(1)

        dates = driver.find_elements_by_xpath("//tbody/tr/td/div/span")
        for date in dates:
            wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//tbody/tr/td/div/span")))
            if date.text == "16":
                date.click()
                break

        driver.find_element_by_xpath("//input[@id='from']").send_keys("lon")
        airports = driver.find_elements_by_xpath("//li[contains(@class, 'flightOptions')]")
        for airport in airports:
            destination = airport.text
            if "Heathrow" in destination:
                airport.click()
                break
        arrive = driver.find_element_by_id("to")
        arrive.send_keys("Barbados")
        arrive.send_keys(Keys.ENTER)
        driver.find_element_by_id("sb-FlightAndHotel-pax-mix").click()
        driver.find_element_by_xpath("//div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
        driver.find_element_by_xpath("//div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/button[2]").click()
        driver.find_element_by_xpath("//div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/button[2]").click()
        dropDown = Select(driver.find_element_by_xpath(
            "//div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/select[1]"))
        dropDown.select_by_visible_text('7')
        driver.find_element_by_xpath("//div[4]/form[1]/div[1]/div[1]/div[2]/button[1]").click()
        driver.find_element_by_xpath("//span[contains(text(),'Travel class')]").click()
        driver.find_element_by_xpath("//label[contains(text(),'Business')]").click()
        driver.find_element_by_xpath("//form[2]/div[1]/div[1]/div[2]/button[1]").click()
        driver.find_element_by_css_selector("div[class*='search-button-container'] button").click()
        time.sleep(3)
        driver.back()
        driver.find_element_by_xpath("//a[contains(text(),'Iberia.com')]").click()
        #mainWindow = driver.window_handles[0]
        #window1 = driver.window_handles[1]
        #window2 = driver.window_handles[2]

        driver.switch_to.window(driver.window_handles[-1])
        print(driver.title)

        time.sleep(3)
        driver.quit()
