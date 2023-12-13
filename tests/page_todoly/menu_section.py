from tests.control.button import Button
from selenium.webdriver.common.by import By

class MenuSection:
    def __init__(self):
        self.logout_button = Button((By.ID, "ctl00_HeaderTopControl1_LinkButtonLogout"))
        self.setting_button = Button((By.XPATH, "//a[text()='Settings']"))
