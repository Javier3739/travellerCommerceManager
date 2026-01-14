from gestorBase import gestorBase

RUTA_BD = './traveller.db'

class Principal(object):
    def __init__(self):
        self.aventura = None
        self.conexion = gestorBase(RUTA_BD)
    def cargar_aventura
