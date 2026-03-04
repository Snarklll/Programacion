from typing import Union
import math

Numero = Union[int, float]


def leer_numero(mensaje: str) -> float:
    valor = float(input(mensaje))
    if valor <= 0:
        raise ValueError("Los lados deben ser positivos")
    return valor


def validar_triangulo(a: Numero, b: Numero, c: Numero) -> None:
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("No forman un triángulo")


def calcular_angulos(a: Numero, b: Numero, c: Numero):
    A = math.degrees(math.acos((b*b + c*c - a*a) / (2*b*c)))
    B = math.degrees(math.acos((a*a + c*c - b*b) / (2*a*c)))
    C = math.degrees(math.acos((a*a + b*b - c*c) / (2*a*b)))
    return A, B, C


class Triangulo:
    def __init__(self, a: Numero, b: Numero, c: Numero):
        validar_triangulo(a, b, c)
        self.a = a
        self.b = b
        self.c = c
        self.angulos = calcular_angulos(a, b, c)

    def tipo(self) -> str:
        raise NotImplementedError

    def mostrar_angulos(self):
        A, B, C = self.angulos
        print("Ángulo A:", round(A, 2))
        print("Ángulo B:", round(B, 2))
        print("Ángulo C:", round(C, 2))


class TrianguloAgudo(Triangulo):
    def tipo(self) -> str:
        return "Triángulo Agudo"


class TrianguloRecto(Triangulo):
    def tipo(self) -> str:
        return "Triángulo Recto"


class TrianguloObtuso(Triangulo):
    def tipo(self) -> str:
        return "Triángulo Obtuso"


class ClasificadorTriangulo:
    def clasificar(self, a: Numero, b: Numero, c: Numero) -> Triangulo:
        angulos = calcular_angulos(a, b, c)

        for ang in angulos:
            if abs(ang - 90) < 0.01:
                return TrianguloRecto(a, b, c)

        for ang in angulos:
            if ang > 90:
                return TrianguloObtuso(a, b, c)

        return TrianguloAgudo(a, b, c)


class Aplicacion:
    def __init__(self, clasificador: ClasificadorTriangulo):
        self._clasificador = clasificador

    def ejecutar(self) -> None:
        print("Clasificador de Triángulos con Herencia")

        try:
            a = leer_numero("Ingresa el lado a: ")
            b = leer_numero("Ingresa el lado b: ")
            c = leer_numero("Ingresa el lado c: ")

            triangulo = self._clasificador.clasificar(a, b, c)

            print("Tipo:", triangulo.tipo())
            triangulo.mostrar_angulos()

        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    clasificador = ClasificadorTriangulo()
    app = Aplicacion(clasificador)
    app.ejecutar()