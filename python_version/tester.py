from tests.basicos_aventura import BasicosAventura

class Tester(object):
	@classmethod
	def haz_pruebas(this):
		ok = 1
		test = BasicosAventura()
		if test.haz_prueba() != 0:
			print("El test básico de aventuras resultó en error. ")
			ok = 0
		if (ok):
			print("Todo OK!")

if __name__ == '__main__':
	Tester.haz_pruebas()
