from typing import Union
import math

Numero = Union[int, float]


def leer_entero_positivo(mensaje: str) -> int:
    valor = input(mensaje).strip()
    if valor == "":
        raise ValueError("Entrada vacía")
    n = int(valor)
    if n <= 0:
        raise ValueError("El número debe ser positivo")
    return n


def leer_numero_positivo(mensaje: str) -> float:
    valor = input(mensaje).strip()
    if valor == "":
        raise ValueError("Entrada vacía")
    x = float(valor)
    if x <= 0:
        raise ValueError("El número debe ser positivo")
    return x


class Figura:
    def __init__(self, lados: int):
        self.lados = lados

    def nombre(self) -> str:
        raise NotImplementedError

    def perimetro(self) -> float:
        raise NotImplementedError

    def area(self) -> float:
        raise NotImplementedError


class Poligono(Figura):
    def __init__(self, lados: int):
        super().__init__(lados)

    def nombre(self) -> str:
        if self.lados == 3:
            return "Triángulo"
        if self.lados == 4:
            return "Cuadrado"
        return f"Polígono de {self.lados} lados"


class Triangulo(Poligono):
    def __init__(self, lado: Numero):
        super().__init__(3)
        self.lado = float(lado)

    def perimetro(self) -> float:
        return 3 * self.lado

    def area(self) -> float:
        return (math.sqrt(3) / 4) * (self.lado ** 2)


class Cuadrado(Poligono):
    def __init__(self, lado: Numero):
        super().__init__(4)
        self.lado = float(lado)

    def perimetro(self) -> float:
        return 4 * self.lado

    def area(self) -> float:
        return self.lado ** 2


class PoligonoRegular(Poligono):
    def __init__(self, lados: int, lado: Numero, apotema: Numero):
        super().__init__(lados)
        self.lado = float(lado)
        self.apotema = float(apotema)

    def perimetro(self) -> float:
        return self.lados * self.lado

    def area(self) -> float:
        return (self.perimetro() * self.apotema) / 2


class Clasificador:
    def crear_figura(self, lados: int) -> Figura:
        if lados < 3:
            raise ValueError("Con menos de 3 lados no es un polígono")

        if lados == 3:
            lado = leer_numero_positivo("Ingresa la longitud del lado: ")
            return Triangulo(lado)

        if lados == 4:
            lado = leer_numero_positivo("Ingresa la longitud del lado: ")
            return Cuadrado(lado)

        lado = leer_numero_positivo("Ingresa la longitud del lado: ")
        resp = input("¿Conoces el apotema? (s/n): ").strip().lower()

        if resp == "s":
            apotema = leer_numero_positivo("Ingresa el apotema: ")
            return PoligonoRegular(lados, lado, apotema)

        return PoligonoRegular(lados, lado, 0)


class Aplicacion:
    def __init__(self, clasificador: Clasificador):
        self.clasificador = clasificador

    def ejecutar(self) -> None:
        print("Clasificador de Figuras con Herencia")
        try:
            lados = leer_entero_positivo("Ingresa el número de lados: ")
            figura = self.clasificador.crear_figura(lados)

            print("Figura:", figura.nombre())

            if isinstance(figura, Triangulo) or isinstance(figura, Cuadrado):
                print("Perímetro:", figura.perimetro())
                print("Área:", figura.area())
            else:
                if isinstance(figura, PoligonoRegular) and figura.apotema > 0:
                    print("Perímetro:", figura.perimetro())
                    print("Área:", figura.area())
                else:
                    print("Perímetro:", figura.lados * figura.lado if hasattr(figura, "lado") else "No disponible")
                    print("Área: No disponible sin apotema")

        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    app = Aplicacion(Clasificador())
    app.ejecutar()