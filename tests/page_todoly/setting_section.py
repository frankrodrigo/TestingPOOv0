from tests.control.button import Button
from tests.control.textbox import TextBox
from selenium.webdriver.common.by import By


class SettingsSection:
    def __init__(self):
        self.old_password_textbox = TextBox((By.ID, "TextPwOld"))
        self.new_password_textbox = TextBox((By.ID, "TextPwNew"))
        self.ok_button = Button((By.XPATH, "//span[text()='Ok']"))
