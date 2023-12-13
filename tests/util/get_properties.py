class GetProperties:
    def __init__(self):
        self.browser = "chrome"  # Set default values or load from properties file
        self.host = "http://todo.ly/"
        self.user = "bootcamp@mojix45.com"
        self.pwd = "12345"

    def get_browser(self):
        return self.browser

