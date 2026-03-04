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


class Operacion:
    def validar(self, *args: Numero) -> None:
        if len(args) not in (0, 2, 3):
            raise ValueError("Cantidad de parámetros no válida")

    def calcular(self, *args: Numero) -> Numero:
        raise NotImplementedError


class Suma(Operacion):
    def validar(self, *args: Numero) -> None:
        super().validar(*args)

    def calcular(self, *args: Numero) -> Numero:
        self.validar(*args)
        return sumar(*args)


class Resta(Operacion):
    def validar(self, *args: Numero) -> None:
        super().validar(*args)

    def calcular(self, *args: Numero) -> Numero:
        self.validar(*args)
        return restar(*args)


class Multiplicacion(Operacion):
    def validar(self, *args: Numero) -> None:
        super().validar(*args)

    def calcular(self, *args: Numero) -> Numero:
        self.validar(*args)
        return multiplicar(*args)


class Division(Operacion):
    def validar(self, *args: Numero) -> None:
        super().validar(*args)
        if len(args) == 2:
            if args[1] == 0:
                raise ValueError("No se puede dividir entre cero")
        if len(args) == 3:
            if args[1] == 0 or args[2] == 0:
                raise ValueError("No se puede dividir entre cero")

    def calcular(self, *args: Numero) -> Numero:
        self.validar(*args)
        return dividir(*args)


class Potencia(Operacion):
    def validar(self, *args: Numero) -> None:
        super().validar(*args)

    def calcular(self, *args: Numero) -> Numero:
        self.validar(*args)
        return potencia(*args)


class Calculadora:
    def ejecutar_operacion(self, operacion: Operacion, *args: Numero) -> Numero:
        return operacion.calcular(*args)


class Aplicacion:
    def __init__(self, calculadora: Calculadora):
        self._calculadora = calculadora

    def ejecutar(self) -> None:
        print("Calculadora con Herencia y Sobreescritura")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")

        opcion = input("Selecciona una opción: ")
        cantidad = int(input("¿Cuántos parámetros deseas usar? (0, 2 o 3): "))

        if opcion == "1":
            operacion = Suma()
        elif opcion == "2":
            operacion = Resta()
        elif opcion == "3":
            operacion = Multiplicacion()
        elif opcion == "4":
            operacion = Division()
        elif opcion == "5":
            operacion = Potencia()
        else:
            print("Operación no válida")
            return

        try:
            if cantidad == 0:
                resultado = self._calculadora.ejecutar_operacion(operacion)
            elif cantidad == 2:
                a = float(input("Ingresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))
                resultado = self._calculadora.ejecutar_operacion(operacion, a, b)
            elif cantidad == 3:
                a = float(input("Ingresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))
                c = float(input("Ingresa el tercer número: "))
                resultado = self._calculadora.ejecutar_operacion(operacion, a, b, c)
            else:
                raise ValueError("Cantidad no permitida")

            print("Resultado:", resultado)

        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    calculadora = Calculadora()
    app = Aplicacion(calculadora)
    app.ejecutar()