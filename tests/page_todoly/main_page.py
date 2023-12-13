from tests.control.button import Button
from tests.control.label import Label
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self):
        self.login_label = Label((By.XPATH, "//img[contains(@src,'pagelogin')]"))
        self.sign_up_free_button = Button((By.XPATH, "//img[@src=\"/Images/design/pagesignup.png\"]"))
