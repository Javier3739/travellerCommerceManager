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
    def busca_aventura_por_nombre(self, nombre):
        for aventura in self.aventuras:
            if nombre == aventura.nombre:
                return aventura
        raise ValueError
