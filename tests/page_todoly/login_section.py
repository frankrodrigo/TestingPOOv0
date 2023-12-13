from tests.control.button import Button
from tests.control.textbox import TextBox
from selenium.webdriver.common.by import By


class LoginSection:
    def __init__(self):
        self.email_textbox = TextBox((By.ID, "ctl00_MainContent_LoginControl1_TextBoxEmail"))
        self.password_textbox = TextBox((By.ID, "ctl00_MainContent_LoginControl1_TextBoxPassword"))
        self.login_button = Button((By.ID, "ctl00_MainContent_LoginControl1_ButtonLogin"))

    def login(self, user, pwd):
        self.email_textbox.set_text(user)
        self.password_textbox.set_text(pwd)
        self.login_button.click()
