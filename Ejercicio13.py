from abc import ABC, abstractmethod

class Entidad(ABC):
    @abstractmethod
    def mostrar(self):
        pass

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
    def leer_persona(self):
        nombre = input("Ingrese nombre: ")
        ap = input("Ingrese apellido paterno: ")
        am = input("Ingrese apellido materno: ")
        genero = input("Ingrese genero: ")
        edad = int(input("Ingrese edad: "))
        return Persona(nombre, ap, am, genero, edad)

class RepositorioPersonas:
    def __init__(self):
        self._personas = []

    def agregar(self, persona):
        self._personas.append(persona)

    def obtener_por_indice(self, indice):
        if 0 <= indice < len(self._personas):
            return self._personas[indice]
        return None

    def cantidad(self):
        return len(self._personas)

class Aplicacion:
    def __init__(self):
        self.lector = LectorDatos()
        self.repositorio = RepositorioPersonas()

    def ejecutar(self):
        cantidad = int(input("Cuantas personas desea ingresar: "))
        for _ in range(cantidad):
            persona = self.lector.leer_persona()
            self.repositorio.agregar(persona)

        print("Total de personas registradas:", self.repositorio.cantidad())

        indice = int(input("Ingrese el indice de la persona que desea consultar(Empieza del 0): "))
        persona = self.repositorio.obtener_por_indice(indice)

        if persona:
            persona.mostrar()
        else:
            print("Indice no valido")

if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()