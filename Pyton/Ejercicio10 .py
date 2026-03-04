from abc import ABC, abstractmethod

class OperacionEstadistica(ABC):
    @abstractmethod
    def calcular(self, numeros):
        pass

class Suma(OperacionEstadistica):
    def calcular(self, numeros):
        return sum(numeros)

class Promedio(OperacionEstadistica):
    def calcular(self, numeros):
        return sum(numeros) / len(numeros)

class Media(OperacionEstadistica):
    def calcular(self, numeros):
        ordenados = sorted(numeros)
        n = len(ordenados)
        if n % 2 == 0:
            return (ordenados[n//2 - 1] + ordenados[n//2]) / 2
        return ordenados[n//2]

class Maximo(OperacionEstadistica):
    def calcular(self, numeros):
        return max(numeros)

class Minimo(OperacionEstadistica):
    def calcular(self, numeros):
        return min(numeros)

class RecolectorNumeros:
    def recolectar(self):
        numeros = []
        for i in range(5):
            numero = float(input("Ingrese un numero: "))
            numeros.append(numero)
        return numeros

class CalculadoraEstadistica:
    def __init__(self, operaciones):
        self.operaciones = operaciones

    def ejecutar(self, numeros):
        resultados = {}
        for operacion in self.operaciones:
            nombre = operacion.__class__.__name__
            resultados[nombre] = operacion.calcular(numeros)
        return resultados

class Aplicacion:
    def __init__(self):
        self.recolector = RecolectorNumeros()
        self.calculadora = CalculadoraEstadistica([
            Suma(),
            Promedio(),
            Media(),
            Maximo(),
            Minimo()
        ])

    def ejecutar(self):
        numeros = self.recolector.recolectar()
        resultados = self.calculadora.ejecutar(numeros)

        for nombre, valor in resultados.items():
            print(nombre + ":", valor)

if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()