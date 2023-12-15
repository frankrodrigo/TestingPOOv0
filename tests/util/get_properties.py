class GetProperties:
    def __init__(self):
        self.browser = "chrome"  # Set default values or load from properties file
        self.host = "http://todo.ly/"
        self.user = "frank@frank.com"
        self.pwd = "123456"

    def get_browser(self):
        return self.browser

