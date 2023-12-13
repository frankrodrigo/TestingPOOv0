from tests.control.control import Control

class TextBox(Control):
    def __init__(self, locator):
        super().__init__(locator)

    def set_text(self, value):
        self.find()
        self.control.send_keys(value)

    def clear_set_text(self, value):
        self.find()
        self.control.clear()
        self.control.send_keys(value)
