class AdventureNotSelectedError(Exception):
    def __init__(self, msg=""):
        self.args = msg
    def __str__(self):
        return ("Adventure Not Selected: You must select an adventure before doing this action. "
 + str(self.args))
