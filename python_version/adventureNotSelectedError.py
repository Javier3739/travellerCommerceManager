class AdventureNotSelectedError(Exception):
    def __init__(self, msg=""):
        self.args = msg
    def __str__(self):
        return ("Aventura no seleccionada. Debes seleccionar una para realizar esta acción. "
 + str(self.args))
