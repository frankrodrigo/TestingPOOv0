from tests.control.button import Button
from tests.control.textbox import TextBox
from tests.control.checkbox import CheckBox
from selenium.webdriver.common.by import By

class SignUpSection:
    def __init__(self):
        self.full_name_textbox = TextBox((By.ID, "ctl00_MainContent_SignupControl1_TextBoxFullName"))
        self.email_textbox = TextBox((By.ID, "ctl00_MainContent_SignupControl1_TextBoxEmail"))
        self.pwd_textbox = TextBox((By.ID, "ctl00_MainContent_SignupControl1_TextBoxPassword"))
        self.agree_terms_checkbox = CheckBox((By.ID, "ctl00_MainContent_SignupControl1_CheckBoxTerms"))
        self.signup_button = Button((By.ID, "ctl00_MainContent_SignupControl1_ButtonSignup"))

    def create_new_account(self, full_name, email, pwd):
        self.full_name_textbox.set_text(full_name)
        self.email_textbox.set_text(email)
        self.pwd_textbox.set_text(pwd)
        self.agree_terms_checkbox.check()
        self.signup_button.click()
