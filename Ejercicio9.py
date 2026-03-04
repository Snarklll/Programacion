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

class ProcesadorNumeros:
    def convertir(self, entrada):
        partes = entrada.split(",")
        numeros = [float(numero.strip()) for numero in partes]
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
        self.procesador = ProcesadorNumeros()
        self.calculadora = CalculadoraEstadistica([
            Suma(),
            Promedio(),
            Media(),
            Maximo(),
            Minimo()
        ])

    def ejecutar(self):
        entrada = input("Ingrese 5 numeros separados por coma: ")
        numeros = self.procesador.convertir(entrada)

        if len(numeros) != 5:
            print("Debe ingresar exactamente 5 numeros")
            return

        resultados = self.calculadora.ejecutar(numeros)

        for nombre, valor in resultados.items():
            print(nombre + ":", valor)

if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()