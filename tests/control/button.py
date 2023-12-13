from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tests.session.session import Session


class Button:
    def __init__(self, locator: By):
        self.locator = locator

    def find(self) -> WebElement:
        return Session.getInstance().get_browser().find_element(*self.locator)

    def click(self):
        self.find().click()

    def is_control_displayed(self):
        try:
            return self.find().is_displayed()
        except Exception as e:
            return False

    def wait_control_is_not_in_the_page(self):
        explicit_wait = WebDriverWait(Session.getInstance().get_browser(), 5)
        explicit_wait.until(EC.invisibility_of_element_located(self.locator))
