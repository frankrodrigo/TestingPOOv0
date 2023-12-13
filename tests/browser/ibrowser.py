from abc import ABC, abstractmethod
from selenium.webdriver.remote.webdriver import WebDriver


class IBrowser(ABC):
    @abstractmethod
    def create(self) -> WebDriver:
        pass
