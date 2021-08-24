from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
    zero = (By.CSS_SELECTOR, "a[title*='home page']")
    holidays = (By.ID, "flightAndHotelTab")
    flyOut = (By.XPATH, "//div[@id='flightandhotel-outbound-date-selector']")
    skip = (By.CSS_SELECTOR, "span[class*='next-month'] span")
    dates = (By.XPATH, "//tbody/tr/td/div/span")
    airportSearch = (By.XPATH, "//input[@id='from']")
    airports = (By.XPATH, "//li[contains(@class, 'flightOptions')]")
    paxMix = (By.ID, "sb-FlightAndHotel-pax-mix")
    one = (By.XPATH, "//div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]")
    two = (By.XPATH, "//div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/button[2]")
    three = (By.XPATH, "//div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/button[2]")
    select = (By.XPATH, "//div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/select[1]")
    four = (By.XPATH, "//div[4]/form[1]/div[1]/div[1]/div[2]/button[1]")
    five = (By.XPATH, "//span[contains(text(),'Travel class')]")
    six = (By.XPATH, "//label[contains(text(),'Business')]")
    seven = (By.XPATH, "//form[2]/div[1]/div[1]/div[2]/button[1]")
    eight = (By.CSS_SELECTOR, "div[class*='search-button-container'] button")
    nine = (By.XPATH, "//a[contains(text(),'Iberia.com')]")

    def getZero(self):
        return self.driver.find_element(*HomePage.zero)
    def gethols(self):
        return self.driver.find_element(*HomePage.holidays)

    def catchFlight(self):
        return self.driver.find_element(*HomePage.flyOut)

    def next(self):
        return self.driver.find_element(*HomePage.skip)

    def calender(self):
        return self.driver.find_elements(*HomePage.dates)

    def getAirport(self):
        return self.driver.find_element(*HomePage.airportSearch)

    def chooseAirport(self):
        return self.driver.find_elements(*HomePage.airports)

    def getPax(self):
        return self.driver.find_element(*HomePage.paxMix)

    def getOne(self):
        return self.driver.find_element(*HomePage.one)

    def getTwo(self):
        return self.driver.find_element(*HomePage.two)

    def getThree(self):
        return self.driver.find_element(*HomePage.three)

    def getSelect(self):
        return self.driver.find_element(*HomePage.select)

    def getFour(self):
        return self.driver.find_element(*HomePage.four)

    def getFive(self):
        return self.driver.find_element(*HomePage.five)

    def getSix(self):
        return self.driver.find_element(*HomePage.six)

    def getSeven(self):
        return self.driver.find_element(*HomePage.seven)

    def getEight(self):
        return self.driver.find_element(*HomePage.eight)

    def getNine(self):
        return self.driver.find_element(*HomePage.nine)
