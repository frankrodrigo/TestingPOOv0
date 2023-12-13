from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tests.session.session import Session


class CheckBox:
    def __init__(self, locator: By):
        self.locator = locator

    def find(self) -> WebElement:
        return Session.getInstance().get_browser().find_element(*self.locator)

    def check(self):
        control = self.find()
        if not control.is_selected():
            control.click()

    def un_check(self):
        control = self.find()
        if control.is_selected():
            control.click()
