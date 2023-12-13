from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Grid:
    def create(self):
        chrome_options = Options()
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['goog:chromeOptions'] = {'args': ['--start-maximized']}

        driver = webdriver.Remote(command_executor='http://selenium-hub:4444/wd/hub',
                                  options=chrome_options)
        return driver
