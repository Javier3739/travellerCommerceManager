from errores import *

class Instancia(object):
    def __init__(self, conexionbd):
        self.conexion = conexionbd
        self.aventura = None
    def mostrar_aventuras(self):
        return self.conexion.mostrar_aventuras()
    def mostrar_detalles_aventura(self, id_av):
        return self.conexion.mostrar_datos_aventura(id_av)
    def seleccionar_aventura(self, id_av):
        if (self.aventura.id != id_av):
            self.conexion.guardar_aventura()
            try:
                self.aventura = self.conexion.cargar_aventura(id_av)
            except ValueError:
                raise ErrorIDNoEncontrado("El valor de id de aventura "str(id_av) + " no existe. ")
        
