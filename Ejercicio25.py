class Persona:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def to_string(self):
        return f"{self.nombre},{self.edad},{self.carrera}"


class ManejadorTXT:

    def escribir(self, nombre_archivo, datos_basicos, arreglo, matriz, personas):

        with open(nombre_archivo, "w") as archivo:

            archivo.write("=== DATOS BASICOS ===\n")
            for clave, valor in datos_basicos.items():
                archivo.write(f"{clave}: {valor}\n")

            archivo.write("\n=== ARREGLO ===\n")
            archivo.write(",".join(map(str, arreglo)) + "\n")

            archivo.write("\n=== MATRIZ ===\n")
            for fila in matriz:
                archivo.write(",".join(fila) + "\n")

            archivo.write("\n=== PERSONAS ===\n")
            for persona in personas:
                archivo.write(persona.to_string() + "\n")


    def leer(self, nombre_archivo):

        print("\n=== CONTENIDO DEL ARCHIVO TXT ===\n")

        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            print(contenido)


class Sistema:

    def ejecutar(self):

        # ----- Datos Básicos -----
        print("=== CAPTURA DATOS BASICOS ===")
        universidad = input("Universidad: ")
        materia = input("Materia: ")

        datos_basicos = {
            "Universidad": universidad,
            "Materia": materia
        }

        # ----- Arreglo -----
        print("\n=== CAPTURA ARREGLO ===")
        arreglo = []
        n = int(input("¿Cuántos números deseas ingresar?: "))
        for i in range(n):
            numero = input(f"Número {i+1}: ")
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

        # ----- Personas -----
        print("\n=== CAPTURA PERSONAS ===")
        personas = []
        cantidad = int(input("¿Cuántas personas deseas ingresar?: "))

        for i in range(cantidad):
            print(f"\nPersona {i+1}")
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            carrera = input("Carrera: ")

            persona = Persona(nombre, edad, carrera)
            personas.append(persona)

        # ----- Guardar y Leer -----
        manejador = ManejadorTXT()
        manejador.escribir("datos.txt", datos_basicos, arreglo, matriz, personas)
        manejador.leer("datos.txt")


if __name__ == "__main__":
    sistema = Sistema()
    sistema.ejecutar()