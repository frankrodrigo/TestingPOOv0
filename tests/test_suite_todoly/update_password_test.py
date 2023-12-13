import unittest
from datetime import datetime
from tests.page_todoly.main_page import MainPage
from tests.page_todoly.login_section import LoginSection
from tests.page_todoly.menu_section import MenuSection
from tests.page_todoly.setting_section import SettingsSection
from tests.page_todoly.sign_up_section import SignUpSection


class UpdatePasswordTest(unittest.TestCase):
    def test_verify_update_password(self):
        email = "bootcamp@" + str(datetime.now().timestamp()) + ".com"
        pwd = str(datetime.now().timestamp())
        new_pwd = "Auto" + pwd

        MainPage().sign_up_free_button.click()
        SignUpSection().create_new_account(email, email, pwd)
        MenuSection().setting_button.click()
        SettingsSection().old_password_txt_box.set_text(pwd)
        SettingsSection().new_password_txt_box.set_text(new_pwd)
        SettingsSection().ok_button.click()

        MenuSection().logout_button.click()
        MainPage().login_label.click()
        LoginSection().login(email, new_pwd)
        self.assertTrue(MenuSection().logout_button.is_control_displayed(), "ERROR! Failed to log in")


if __name__ == "__main__":
    unittest.main()
