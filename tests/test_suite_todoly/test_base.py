import unittest
from tests.page_todoly.main_page import MainPage
from tests.page_todoly.login_section import LoginSection
from tests.page_todoly.menu_section import MenuSection
from tests.page_todoly.project_section import ProjectSection
from tests.page_todoly.setting_section import SettingsSection
from tests.page_todoly.sign_up_section import SignUpSection
from tests.session.session import Session
from tests.util.get_properties import GetProperties


class TestBase(unittest.TestCase):
    def setUp(self):
        self.main_page = MainPage()
        self.login_section = LoginSection()
        self.menu_section = MenuSection()
        self.project_section = ProjectSection()
        self.settings_section = SettingsSection()
        self.sign_up_section = SignUpSection()
        self.user = GetProperties().get_user()
        self.password = GetProperties().get_pwd()

        Session().get_browser().get(GetProperties().get_host())

    def tearDown(self):
        Session().close_session()


if __name__ == "__main__":
    unittest.main()
