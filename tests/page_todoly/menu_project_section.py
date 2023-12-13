from tests.control.button import Button
from selenium.webdriver.common.by import By

class MenuProjectSection:
    def __init__(self):
        self.menu_icon_button = Button((By.XPATH, "//div[contains(@style,'block')]/img"))
        self.edit_button = Button((By.XPATH, "//ul[@id=\"projectContextMenu\"]//a[text()='Edit']"))
        self.delete_button = Button((By.ID, "ProjShareMenuDel"))
