import turtle
from abc import ABC, abstractmethod


class Fractal(ABC):
    @abstractmethod
    def dibujar(self):
        pass


class ConfiguracionDibujo:
    def __init__(self, ancho=900, alto=700, titulo="Fractales"):
        self.ancho = ancho
        self.alto = alto
        self.titulo = titulo

    def preparar(self):
        pantalla = turtle.Screen()
        pantalla.setup(self.ancho, self.alto)
        pantalla.title(self.titulo)
        pantalla.bgcolor("white")

        lapiz = turtle.Turtle()
        lapiz.hideturtle()
        lapiz.speed(0)
        lapiz.pensize(2)
        lapiz.penup()

        return pantalla, lapiz


class ValidadorEntrada:
    def leer_entero(self, mensaje, minimo=0, maximo=10):
        valor = int(input(mensaje))
        if valor < minimo or valor > maximo:
            raise ValueError("Valor fuera de rango")
        return valor

    def leer_flotante(self, mensaje, minimo=1.0, maximo=800.0):
        valor = float(input(mensaje))
        if valor < minimo or valor > maximo:
            raise ValueError("Valor fuera de rango")
        return valor


class TrianguloSierpinski(Fractal):
    def __init__(self, lapiz, nivel, tamano, x, y):
        self._lapiz = lapiz
        self._nivel = nivel
        self._tamano = tamano
        self._x = x
        self._y = y

    def dibujar(self):
        self._dibujar_triangulo(self._x, self._y, self._tamano, self._nivel)

    def _mover(self, x, y):
        self._lapiz.penup()
        self._lapiz.goto(x, y)
        self._lapiz.pendown()

    def _triangulo(self, x, y, tamano):
        self._mover(x, y)
        self._lapiz.setheading(0)
        for _ in range(3):
            self._lapiz.forward(tamano)
            self._lapiz.left(120)

    def _dibujar_triangulo(self, x, y, tamano, nivel):
        if nivel == 0:
            self._triangulo(x, y, tamano)
            return

        mitad = tamano / 2
        self._dibujar_triangulo(x, y, mitad, nivel - 1)
        self._dibujar_triangulo(x + mitad, y, mitad, nivel - 1)

        altura = (3 ** 0.5) * mitad / 2
        self._dibujar_triangulo(x + mitad / 2, y + altura, mitad, nivel - 1)


class PolvoDeCantor(Fractal):
    def __init__(self, lapiz, nivel, tamano, x, y, separacion):
        self._lapiz = lapiz
        self._nivel = nivel
        self._tamano = tamano
        self._x = x
        self._y = y
        self._separacion = separacion

    def dibujar(self):
        self._cantor(self._x, self._y, self._tamano, self._nivel)

    def _mover(self, x, y):
        self._lapiz.penup()
        self._lapiz.goto(x, y)
        self._lapiz.pendown()

    def _segmento(self, x, y, longitud):
        self._mover(x, y)
        self._lapiz.setheading(0)
        self._lapiz.forward(longitud)

    def _cantor(self, x, y, longitud, nivel):
        self._segmento(x, y, longitud)
        if nivel == 0:
            return

        nueva_longitud = longitud / 3
        nuevo_y = y - self._separacion
        self._cantor(x, nuevo_y, nueva_longitud, nivel - 1)
        self._cantor(x + 2 * nueva_longitud, nuevo_y, nueva_longitud, nivel - 1)


class FabricaFractales:
    def crear(self, opcion, lapiz, nivel, tamano):
        if opcion == "1":
            x = -tamano / 2
            y = -250
            return TrianguloSierpinski(lapiz, nivel, tamano, x, y)
        if opcion == "2":
            x = -tamano / 2
            y = 250
            separacion = max(10, 220 / (nivel + 1))
            return PolvoDeCantor(lapiz, nivel, tamano, x, y, separacion)
        raise ValueError("Opción no válida")


class Aplicacion:
    def __init__(self):
        self._config = ConfiguracionDibujo()
        self._validador = ValidadorEntrada()
        self._fabrica = FabricaFractales()

    def ejecutar(self):
        print("1. Triángulo de Sierpinski")
        print("2. Polvo de Cantor")
        opcion = input("Selecciona una opción: ")

        try:
            nivel = self._validador.leer_entero("Ingresa el nivel (0 a 8): ", 0, 8)
            tamano = self._validador.leer_flotante("Ingresa el tamaño (50 a 700): ", 50.0, 700.0)
        except ValueError as e:
            print("Error:", e)
            return

        pantalla, lapiz = self._config.preparar()

        try:
            fractal = self._fabrica.crear(opcion, lapiz, nivel, tamano)
            fractal.dibujar()
        except ValueError as e:
            print("Error:", e)
            return

        pantalla.exitonclick()


if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()
