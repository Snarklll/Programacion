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
        numeros_ordenados = sorted(numeros)
        n = len(numeros_ordenados)
        if n % 2 == 0:
            return (numeros_ordenados[n//2 - 1] + numeros_ordenados[n//2]) / 2
        else:
            return numeros_ordenados[n//2]

class Maximo(OperacionEstadistica):
    def calcular(self, numeros):
        return max(numeros)

class Minimo(OperacionEstadistica):
    def calcular(self, numeros):
        return min(numeros)

class CalculadoraEstadistica:
    def __init__(self, operaciones):
        self.operaciones = operaciones

    def ejecutar_operaciones(self, numeros):
        resultados = {}
        for operacion in self.operaciones:
            nombre = operacion.__class__.__name__
            resultados[nombre] = operacion.calcular(numeros)
        return resultados

class Aplicacion:
    def __init__(self):
        self.calculadora = CalculadoraEstadistica([
            Suma(),
            Promedio(),
            Media(),
            Maximo(),
            Minimo()
        ])

    def ejecutar(self):
        numeros = []
        for i in range(5):
            numero = float(input(f"Ingrese el numero {i+1}: "))
            numeros.append(numero)

        resultados = self.calculadora.ejecutar_operaciones(numeros)

        for nombre, resultado in resultados.items():
            print(nombre + ":", resultado)

if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()