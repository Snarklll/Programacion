from typing import Union

Numero = Union[int, float]


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("El factorial no está definido para negativos")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci no está definido para negativos")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


class Operacion:
    def validar(self, *args: Numero) -> None:
        if len(args) != 1:
            raise ValueError("Esta operación requiere exactamente 1 parámetro")

    def calcular(self, *args: Numero) -> Numero:
        raise NotImplementedError


class Factorial(Operacion):
    def calcular(self, *args: Numero) -> Numero:
        self.validar(*args)
        n = args[0]
        if int(n) != n:
            raise ValueError("El factorial requiere un número entero")
        return factorial(int(n))


class Fibonacci(Operacion):
    def calcular(self, *args: Numero) -> Numero:
        self.validar(*args)
        n = args[0]
        if int(n) != n:
            raise ValueError("Fibonacci requiere un número entero")
        return fibonacci(int(n))


class Calculadora:
    def ejecutar_operacion(self, operacion: Operacion, *args: Numero) -> Numero:
        return operacion.calcular(*args)


class Aplicacion:
    def __init__(self, calculadora: Calculadora):
        self._calculadora = calculadora

    def ejecutar(self) -> None:
        print("1. Factorial")
        print("2. Fibonacci")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            operacion = Factorial()
        elif opcion == "2":
            operacion = Fibonacci()
        else:
            print("Operación no válida")
            return

        try:
            numero = float(input("Ingresa un número entero: "))
            resultado = self._calculadora.ejecutar_operacion(operacion, numero)
            print("Resultado:", resultado)
        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    calculadora = Calculadora()
    app = Aplicacion(calculadora)
    app.ejecutar()