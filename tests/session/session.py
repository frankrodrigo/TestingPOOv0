from tests.browser.factory_browser import FactoryBrowser


class Session:
    _instance = None

    def __init__(self):
        self.browser = FactoryBrowser.create()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def close_session(self):
        self.browser.quit()
        self._instance = None

    def get_browser(self):
        return self.browser

    def accept_alert(self):
        self.browser.switch_to.alert.accept()
