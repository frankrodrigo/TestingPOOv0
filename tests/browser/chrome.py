from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class Chrome:
    def create(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        service = Service("resources/drivers/chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        return driver
