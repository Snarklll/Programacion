from typing import Union

Numero = Union[int, float]

def sumar(a: Numero, b: Numero) -> Numero:
    return a + b

def restar(a: Numero, b: Numero) -> Numero:
    return a - b

def multiplicar(a: Numero, b: Numero) -> Numero:
    return a * b

def dividir(a: Numero, b: Numero) -> Numero:
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

def potencia(a: Numero, b: Numero) -> Numero:
    return a ** b

class Numeros:
    def __init__(self, a: Numero, b: Numero):
        self._a = a
        self._b = b

    def obtener_a(self) -> Numero:
        return self._a

    def obtener_b(self) -> Numero:
        return self._b

class Calculadora:
    def calcular(self, operacion: str, numeros: Numeros) -> Numero:
        a = numeros.obtener_a()
        b = numeros.obtener_b()

        if operacion == "1":
            return sumar(a, b)
        elif operacion == "2":
            return restar(a, b)
        elif operacion == "3":
            return multiplicar(a, b)
        elif operacion == "4":
            return dividir(a, b)
        elif operacion == "5":
            return potencia(a, b)
        else:
            raise ValueError("Operación no válida")


class Aplicacion:
    def __init__(self, calculadora: Calculadora):
        self._calculadora = calculadora

    def ejecutar(self) -> None:
        print("Calculadora POO")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")

        operacion = input("Selecciona una opción: ")
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))

        numeros = Numeros(a, b)

        try:
            resultado = self._calculadora.calcular(operacion, numeros)
            print("Resultado:", resultado)
        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    calculadora = Calculadora()
    app = Aplicacion(calculadora)
    app.ejecutar()