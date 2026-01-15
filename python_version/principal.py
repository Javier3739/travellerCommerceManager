from gestorBase import GestorBase
from aventura import Aventura
from flota import Flota
from adventureNotSelectedError import AdventureNotSelectedError

RUTA_BD = './traveller.db'

class Modelo(object):
    def __init__(self):
        self.aventura = None
        self.base_datos = GestorBase(RUTA_BD)
    def nueva_aventura(self, nombre, fecha_estelar, narrador=None):
        aventura = Aventura.nueva_aventura(nombre, fecha_estelar, narrador)
        av_id = self.base_datos.nueva_aventura(aventura)
        aventura.establecer_id(av_id)
        aventura.establecer_bienes(self.cargar_bienes())
        aventura.establecer_reglas(self.cargar_reglas())
        
        """"
        Esto iría en Aventura.nueva_aventura():
        aventura.flotas = []
        aventura.lugares = []
        aventura.establecer_registro_integrantes = RegistroIntegrantes()
        aventura.establecer_registro_viajes = RegistroViajes()
        aventura.establecer_registro_paquetes = RegistroPaquetes()
        aventura.establecer_registro_transacciones = RegistroTransacciones()
        """
    def devolver_aventuras(self)
        aventuras = self.base_datos.mostrar_aventuras()
        for aventura in aventuras:
            l.append(aventura["nombre"])
        return l
    def cargar_aventura(self, nombre):
        datos = self.base_datos.cargar_aventura(nombre)
        self.aventura = Aventura.cargar_aventura(datos)
        aventura.establecer_bienes(self.cargar_bienes())
        aventura.establecer_reglas(self.cargar_reglas())
        aventura.establecer_flotas(self.cargar_flotas())
        l = []
        for flota in aventura.flotas:
            l += flota.mostrar_naves()
        aventura.establecer_lugares(l)
        aventura.establecer_registro_integrantes(self.cargar_registro_integrantes()
    def eliminar_aventura(self, nombre):
        if (aventura.nombre == nombre)
            self.aventura = None
        av_id = self.mostrar_id_aventura(nombre)
        l = self.base_datos.mostrar_bienes_propios_aventura(av_id)
        for bien in l:
            self.base_datos.borrar_bien(bien["id"])
        l = self.base_datos.mostrar_reglas_propias_aventura(av_id)
        for regla in l:
            l_int = self.base_datos.mostrar_int_por_regla(regla["id"])
            for intervalo in l_int:
                self.base_datos.borrar_intervalo(intervalo["id"])
            self.base_datos.borrar_regla(regla["id"])
        self.base_datos.borrar_registro_integrantes(av_id)
        self.base_datos.borrar_registro_paquetes(av_id)
        self.base_datos.borrar_registro_viajes(av_id)
        self.base_datos.borrar_registro_transacciones(av_id)
        l = self.base_datos.mostrar_lugares_por_aventura(av_id)
        for lugares in l:
            l_paq = self.base_datos.mostrar_paquetes_por_lugar(lugar["id"])
            for paquete in l_paq:
                self.base_datos.borrar_paquete(paquete["id"])
            self.base_datos.borrar_lugar(lugar["id"])
        l = self.base_datos.mostrar_flotas_por_aventura(av_id)
        for flota in l:
            self.base_datos.borrar_flota(flota["id"])
    def crear_flota(self, nombre, rangos_navieros, capacidades_grupo):
        if self.aventura == None:
            raise AdventureNotSelected()
        flota = Flota.nueva_flota(nombre, rangos_navieros, capacidades_grupo)
        self.aventura.aniade_flota(flota)
        id_fl = self.base_datos.nueva_flota(flota, self.aventura)
        flota.establecer_id(id_fl)
    def devolver_flotas(self):
        if self.aventura == None:
            raise AdventureNotSelected()
        if self.aventura != None:
            l = []
            for flota in self.aventura.flotas:
                l.append(flota.nombre)
            return l
    def cargar_flotas(self):
        if self.aventura == None:
            raise AdventureNotSelected()
        l = self.base_datos.mostrar_flotas(self.aventura.id)
        flotas = []
        for datos_fl in l:
            flota = Flota.cargar_flota(datos_fl))
            flota.establecer_naves()
        
