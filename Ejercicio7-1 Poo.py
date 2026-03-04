import sys
from abc import ABC, abstractmethod

class TipoDato(ABC):
    @abstractmethod
    def obtener_valor(self, dato):
        pass

    @abstractmethod
    def obtener_nombre_tipo(self):
        pass

class Entero(TipoDato):
    def obtener_valor(self, dato):
        return int(dato)

    def obtener_nombre_tipo(self):
        return "int"

class Flotante(TipoDato):
    def obtener_valor(self, dato):
        return float(dato)

    def obtener_nombre_tipo(self):
        return "float"

class Booleano(TipoDato):
    def obtener_valor(self, dato):
        return dato.lower() == "true"

    def obtener_nombre_tipo(self):
        return "bool"

class Cadena(TipoDato):
    def obtener_valor(self, dato):
        return dato

    def obtener_nombre_tipo(self):
        return "str"

class IdentificadorTipo:
    def __init__(self, tipos):
        self._tipos = tipos

    def identificar(self, dato):
        for tipo in self._tipos:
            try:
                valor = tipo.obtener_valor(dato)
                return valor, tipo.obtener_nombre_tipo(), "basico"
            except:
                continue
        return dato, "desconocido", "creado"

class CalculadoraTamano:
    def calcular(self, valor):
        return sys.getsizeof(valor)

class Aplicacion:
    def __init__(self):
        self.identificador = IdentificadorTipo([
            Entero(),
            Flotante(),
            Booleano(),
            Cadena()
        ])
        self.calculadora = CalculadoraTamano()

    def ejecutar(self):
        dato = input("Ingrese un dato: ")
        valor, tipo, categoria = self.identificador.identificar(dato)
        tamano = self.calculadora.calcular(valor)
        print("Tipo detectado:", tipo)
        print("Categoria:", categoria)
        print("Tamaño en bytes:", tamano)

if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()