from abc import ABC, abstractmethod

class Entidad(ABC):
    @abstractmethod
    def mostrar(self):
        pass

class Auto(Entidad):
    def __init__(self, precio, anio):
        self._precio = precio
        self._anio = anio

    def mostrar(self):
        print("Auto")
        print("Precio:", self._precio)
        print("Año:", self._anio)

class Persona(Entidad):
    def __init__(self, nombre, ap, am, genero, edad):
        self._nombre = nombre
        self._ap = ap
        self._am = am
        self._genero = genero
        self._edad = edad

    def nombre_completo(self):
        return self._nombre + " " + self._ap + " " + self._am

    def mostrar(self):
        print("Persona")
        print("Nombre completo:", self.nombre_completo())
        print("Genero:", self._genero)
        print("Edad:", self._edad)

class LectorDatos:
    def leer_auto(self):
        precio = float(input("Ingrese precio del auto: "))
        anio = int(input("Ingrese año del auto: "))
        return Auto(precio, anio)

    def leer_persona(self):
        nombre = input("Ingrese nombre: ")
        ap = input("Ingrese apellido paterno: ")
        am = input("Ingrese apellido materno: ")
        genero = input("Ingrese genero: ")
        edad = int(input("Ingrese edad: "))
        return Persona(nombre, ap, am, genero, edad)

class Repositorio:
    def __init__(self):
        self._elementos = []

    def agregar(self, entidad):
        self._elementos.append(entidad)

    def mostrar_todos(self):
        for elemento in self._elementos:
            elemento.mostrar()
            print()

class Aplicacion:
    def __init__(self):
        self.lector = LectorDatos()
        self.personas = Repositorio()
        self.autos = Repositorio()

    def ejecutar(self):
        cantidad_personas = int(input("Cuantas personas desea ingresar: "))
        for _ in range(cantidad_personas):
            persona = self.lector.leer_persona()
            self.personas.agregar(persona)

        cantidad_autos = int(input("Cuantos autos desea ingresar: "))
        for _ in range(cantidad_autos):
            auto = self.lector.leer_auto()
            self.autos.agregar(auto)

        print("Lista de Personas")
        self.personas.mostrar_todos()

        print("Lista de Autos")
        self.autos.mostrar_todos()

if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()