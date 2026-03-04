from typing import Union

Numero = Union[int, float]


def sumar(a: Numero, b: Numero) -> Numero:
    return a + b


class Numeros:
    def __init__(self, a: Numero, b: Numero):
        self._a = a
        self._b = b

    def obtener_a(self) -> Numero:
        return self._a

    def obtener_b(self) -> Numero:
        return self._b


class Sumadora:
    def calcular(self, numeros: Numeros) -> Numero:
        return sumar(numeros.obtener_a(), numeros.obtener_b())


class Aplicacion:
    def __init__(self, numeros: Numeros, sumadora: Sumadora):
        self._numeros = numeros
        self._sumadora = sumadora

    def ejecutar(self) -> None:
        print("Suma de 2 números")
        resultado = self._sumadora.calcular(self._numeros)
        print("Resultado:", resultado)


if __name__ == "__main__":
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    numeros = Numeros(a, b)
    sumadora = Sumadora()
    app = Aplicacion(numeros, sumadora)
    app.ejecutar()