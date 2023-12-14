from browser.chrome import create


class FactoryBrowser:
    @staticmethod
    def make(browser_type):
        if browser_type.lower() == "chrome":
            return create()
        # Add other cases for different browsers
        else:
            return create()  # Default to Chrome
