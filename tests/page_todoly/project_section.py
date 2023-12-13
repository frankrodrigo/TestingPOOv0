from tests.control.button import Button
from tests.control.label import Label
from tests.control.textbox import TextBox
from selenium.webdriver.common.by import By
from .menu_project_section import MenuProjectSection

class ProjectSection:
    def __init__(self):
        self.menu_project_section = MenuProjectSection()
        self.add_new_project_button = Button((By.XPATH, "//td[text()='Add New Project']"))
        self.name_project_textbox = TextBox((By.ID, "NewProjNameInput"))
        self.add_button = Button((By.ID, "NewProjNameButton"))
        self.edit_project_textbox = TextBox((By.XPATH, "//td/div/input[@id='ItemEditTextbox']"))
        self.save_button = Button((By.XPATH, "//td/div/img[@id='ItemEditSubmit']"))

    def click_on_project(self, name_project):
        project_created = Label((By.XPATH, "//td[text()='" + name_project + "']"))
        project_created.click()

    def is_project_displayed_in_list(self, name_project):
        project_created = Label((By.XPATH, "//td[text()='" + name_project + "']"))
        return project_created.is_control_displayed()

    def get_project(self, name_project):
        project_created = Label((By.XPATH, "//td[text()='" + name_project + "']"))
        return project_created
