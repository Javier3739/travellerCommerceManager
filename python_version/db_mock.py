class DBMock(object):
    def __init__(self):
        self.aventuras = []
    def guardar_aventura(self, aventura):
        ok = 0
        for i in range(len(self.aventuras)):
            if aventura.nombre == self.aventuras[i].nombre:
                self.aventuras[i] = aventura
                ok = 1
        if ok == 0:
            self.aventuras.append(aventura)
    def buscar_aventura_por_nombre(self, nombre):
        for aventura in self.aventuras:
            if nombre == aventura.nombre:
                return aventura
        raise ValueError
    def buscar_aventura_por_id(self, id_av):
        for aventura in self.aventuras:
            if id_av == aventura.id:
                return aventura
        raise ValueError
    def mostrar_aventuras(self):
        pass
    def mostrar_datos_aventura(self, id_av):
        pass
    def cargar_aventura(self, id_av):
        pass
