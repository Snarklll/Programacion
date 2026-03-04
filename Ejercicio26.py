import json

class Persona:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "carrera": self.carrera
        }


class BaseDeDatosJSON:

    def guardar(self, nombre_archivo, datos):
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def leer(self, nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

class Sistema:

    def ejecutar(self):

        # ----- Datos Básicos -----
        print("=== CAPTURA DATOS BÁSICOS ===")
        universidad = input("Universidad: ")
        materia = input("Materia: ")

        datos_basicos = {
            "universidad": universidad,
            "materia": materia
        }

        # ----- Arreglo -----
        print("\n=== CAPTURA ARREGLO ===")
        arreglo = []
        n = int(input("¿Cuántos números deseas ingresar?: "))
        for i in range(n):
            numero = int(input(f"Número {i+1}: "))
            arreglo.append(numero)

        # ----- Matriz -----
        print("\n=== CAPTURA MATRIZ ===")
        matriz = []
        filas = int(input("Número de filas: "))
        columnas = int(input("Número de columnas: "))

        for i in range(filas):
            fila = []
            print(f"Fila {i+1}")
            for j in range(columnas):
                valor = input(f"Valor [{i+1}][{j+1}]: ")
                fila.append(valor)
            matriz.append(fila)

        # ----- Personas (ADT) -----
        print("\n=== CAPTURA PERSONAS ===")
        personas = []
        cantidad = int(input("¿Cuántas personas deseas ingresar?: "))

        for i in range(cantidad):
            print(f"\nPersona {i+1}")
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            carrera = input("Carrera: ")

            persona = Persona(nombre, edad, carrera)
            personas.append(persona.to_dict())

        # ----- Estructura tipo Base de Datos -----
        base_de_datos = {
            "datos_basicos": datos_basicos,
            "arreglo": arreglo,
            "matriz": matriz,
            "personas": personas
        }

        # ----- Guardar y Leer -----
        bd = BaseDeDatosJSON()
        bd.guardar("datos.json", base_de_datos)

        datos_leidos = bd.leer("datos.json")

        print("\n=== CONTENIDO DEL JSON ===")
        print(json.dumps(datos_leidos, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    sistema = Sistema()
    sistema.ejecutar()