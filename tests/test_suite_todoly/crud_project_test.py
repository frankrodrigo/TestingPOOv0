import unittest
from datetime import datetime
from tests.page_todoly.main_page import MainPage
from tests.page_todoly.login_section import LoginSection
from tests.page_todoly.menu_section import MenuSection
from tests.page_todoly.project_section import ProjectSection
from tests.session.session import Session


class CRUDProjectTest(unittest.TestCase):
    def test_verify_crud_project(self):
        project_created = "Lambton" + str(datetime.now().timestamp())
        project_updated = "PythonUpdate" + str(datetime.now().timestamp())

        MainPage().login_label.click()
        LoginSection().email_txt_box.set_text("username")
        LoginSection().password_txt_box.set_text("password")
        LoginSection().login_button.click()
        self.assertTrue(MenuSection().logout_button.is_control_displayed(), "ERROR! The login failed")

        ProjectSection().add_new_project_button.click()
        ProjectSection().name_project_txt_box.set_text(project_created)
        ProjectSection().add_button.click()
        self.assertTrue(ProjectSection().is_project_displayed_in_list(project_created),
                        "ERROR! The project was not created")

        ProjectSection().click_on_project(project_created)
        ProjectSection().menu_project_section.menu_icon_button.click()
        ProjectSection().menu_project_section.edit_button.click()
        ProjectSection().edit_project_txt_box.clean_set_text(project_updated)
        ProjectSection().save_button.click()
        self.assertTrue(ProjectSection().is_project_displayed_in_list(project_updated),
                        "ERROR! The project was not updated")

        ProjectSection().click_on_project(project_updated)
        ProjectSection().menu_project_section.menu_icon_button.click()
        ProjectSection().menu_project_section.delete_button.click()
        Session().accept_alert()
        ProjectSection().get_project(project_updated).wait_control_is_not_in_the_page()
        self.assertFalse(ProjectSection().is_project_displayed_in_list(project_updated),
                         "ERROR! The project was not deleted")


if __name__ == "__main__":
    unittest.main()
