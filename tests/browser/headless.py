from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Headless:
    def create(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        return driver
