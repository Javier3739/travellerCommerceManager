from gestorBase import GestorBase
from aventura import Aventura

RUTA_BD = './traveller.db'

class Principal(object):
    def __init__(self):
        self.aventura = None
        self.base_datos = GestorBase(RUTA_BD)
    def nueva_aventura(self, nombre, fecha_estelar, narrador=None):
        aventura = Aventura(nombre, fecha_estelar, narrador)
        av_id = self.base_datos.nueva_aventura(aventura)
        bienes = self.base_datos.cargar_bienes(av_id)
        reglas = self.base_datos.cargar_reglas(av_id)
        aventura.cargar_bienes(bienes)
        aventura.cargar_reglas(reglas)
    def cargar_aventura(self, nombre):
        self.aventura = self.base_datos.cargar_aventura(nombre)
    def mostrar_aventuras(self):
        aventuras = self.base_datos.mostrar_aventuras()
        l = []
        for aventura in aventuras:
            l.append(aventura["nombre"])
        return l
    def eliminar_aventura(self, nombre):
        if (aventura.nombre == nombre)
            self.aventura = None
        av_id = self.mostrar_id_aventura(nombre)
        l = self.base_datos.mostrar_bienes_por_aventura(av_id)
        for bien in l:
            self.base_datos.borrar_bien(bien["id"])
        l = self.base_datos.mostrar_reglas_por_aventura(av_id)
        for regla in l:
            l_int = self.base_datos.mostrar_int_por_regla(regla["id"])
            for intervalo in l_int:
                self.base_datos.borrar_intervalo(intervalo["id"])
            self.base_datos.borrar_regla(regla["id"])
        l = self.base_datos.mostrar_naves_por_aventura(av_id)
        for nave in l:
            l_paq = self.base_datos.mostrar_paquetes_por_nave(nave["id"])
            for paquete in l_paq:
                self.base_datos.borrar_paquete(paquete["id"])
            self.base_datos.borrar_nave(nave["id"])
        l = self.base_datos.mostrar_flotas_por_aventura(av_id)
        for flota in l:
            self.base_datos.borrar_flota(flota["id"])
    def crear_flota(self, nombre):
        
        
