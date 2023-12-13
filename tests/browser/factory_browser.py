from tests.browser.chrome import Chrome


class FactoryBrowser:
    @staticmethod
    def make(browser_type):
        if browser_type.lower() == "chrome":
            return Chrome().create()
        # Add other cases for different browsers
        else:
            return Chrome().create()  # Default to Chrome
