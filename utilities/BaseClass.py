import inspect
import logging

import pytest

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("loadUp")
class BaseClass:
    pass

    def selector(self, locator, text):
        dropDown = Select(locator)
        dropDown.select_by_visible_text(text)

    def waiter(self, locator, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((locator, text)))

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('C:\\Users\\stuga\\PycharmProjects\\BAProj\\reports\\logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)  # logger report level
        return logger

    #  logger.debug("A debug statement is executed")
    #     logger.info("Information statement")
    #     logger.warning("Something is in warning mode")
    #     logger.error("A Major error has happend")
    #     logger.critical("Critical issue")
    #     logger.fatal("Fatal occurence")
