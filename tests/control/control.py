from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.session.session import Session

class Control:
    def __init__(self, locator):
        self.locator = locator
        self.control = None

    def find(self):
        self.control = Session.getInstance().getBrowser().find_element(*self.locator)

    def click(self):
        self.find()
        self.control.click()

    def is_control_displayed(self):
        try:
            self.find()
            return self.control.is_displayed()
        except Exception as e:
            return False

    def get_text(self):
        self.find()
        return self.control.text

    def wait_control_is_not_in_the_page(self):
        explicit_wait = WebDriverWait(Session.getInstance().getBrowser(), 5)
        explicit_wait.until(EC.invisibility_of_element_located(self.locator))
