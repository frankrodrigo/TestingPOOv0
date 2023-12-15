from browser.chrome import create


class FactoryBrowser:
    @staticmethod
    def make(browser_type):
        if browser_type.lower() == "chrome":
            return create()
# It is needed to have the other drivers for the other browsers, for example, Geckodriver for Firefox

        else:
            return create()  # Default to Chrome
