from typing import Union

Numero = Union[int, float]


def sumar(*args: Numero) -> Numero:
    if len(args) == 0:
        return 0
    if len(args) == 2:
        return args[0] + args[1]
    if len(args) == 3:
        return args[0] + args[1] + args[2]
    raise ValueError("Cantidad de parámetros no válida")


def restar(*args: Numero) -> Numero:
    if len(args) == 0:
        return 0
    if len(args) == 2:
        return args[0] - args[1]
    if len(args) == 3:
        return args[0] - args[1] - args[2]
    raise ValueError("Cantidad de parámetros no válida")


def multiplicar(*args: Numero) -> Numero:
    if len(args) == 0:
        return 0
    if len(args) == 2:
        return args[0] * args[1]
    if len(args) == 3:
        return args[0] * args[1] * args[2]
    raise ValueError("Cantidad de parámetros no válida")


def dividir(*args: Numero) -> Numero:
    if len(args) == 0:
        return 0
    if len(args) == 2:
        if args[1] == 0:
            raise ValueError("No se puede dividir entre cero")
        return args[0] / args[1]
    if len(args) == 3:
        if args[1] == 0 or args[2] == 0:
            raise ValueError("No se puede dividir entre cero")
        return args[0] / args[1] / args[2]
    raise ValueError("Cantidad de parámetros no válida")


def potencia(*args: Numero) -> Numero:
    if len(args) == 0:
        return 0
    if len(args) == 2:
        return args[0] ** args[1]
    if len(args) == 3:
        return (args[0] ** args[1]) ** args[2]
    raise ValueError("Cantidad de parámetros no válida")


class Calculadora:
    def calcular(self, operacion: str, *args: Numero) -> Numero:
        if operacion == "1":
            return sumar(*args)
        elif operacion == "2":
            return restar(*args)
        elif operacion == "3":
            return multiplicar(*args)
        elif operacion == "4":
            return dividir(*args)
        elif operacion == "5":
            return potencia(*args)
        else:
            raise ValueError("Operación no válida")


class Aplicacion:
    def __init__(self, calculadora: Calculadora):
        self._calculadora = calculadora

    def ejecutar(self) -> None:
        print("Calculadora con sobrecarga")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")

        operacion = input("Selecciona una opción: ")
        cantidad = int(input("¿Cuántos parámetros deseas usar? (0, 2 o 3): "))

        try:
            if cantidad == 0:
                resultado = self._calculadora.calcular(operacion)
            elif cantidad == 2:
                a = float(input("Ingresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))
                resultado = self._calculadora.calcular(operacion, a, b)
            elif cantidad == 3:
                a = float(input("Ingresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))
                c = float(input("Ingresa el tercer número: "))
                resultado = self._calculadora.calcular(operacion, a, b, c)
            else:
                raise ValueError("Cantidad no permitida")

            print("Resultado:", resultado)

        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    calculadora = Calculadora()
    app = Aplicacion(calculadora)
    app.ejecutar()