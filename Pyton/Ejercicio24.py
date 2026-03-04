import xml.etree.ElementTree as ET

class Persona:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera


class ManejadorXML:

    def escribir(self, nombre_archivo, datos_basicos, arreglo, matriz, personas):

        raiz = ET.Element("Sistema")

        # ----- Datos Básicos -----
        datos_xml = ET.SubElement(raiz, "DatosBasicos")
        for clave, valor in datos_basicos.items():
            elemento = ET.SubElement(datos_xml, clave)
            elemento.text = valor

        # ----- Arreglo Simple -----
        arreglo_xml = ET.SubElement(raiz, "Arreglo")
        for numero in arreglo:
            elemento = ET.SubElement(arreglo_xml, "Elemento")
            elemento.text = str(numero)

        # ----- Matriz -----
        matriz_xml = ET.SubElement(raiz, "Matriz")
        for fila in matriz:
            fila_xml = ET.SubElement(matriz_xml, "Fila")
            for valor in fila:
                elemento = ET.SubElement(fila_xml, "Valor")
                elemento.text = str(valor)

        # ----- Personas (ADT) -----
        personas_xml = ET.SubElement(raiz, "Personas")
        for persona in personas:
            persona_xml = ET.SubElement(personas_xml, "Persona")

            ET.SubElement(persona_xml, "Nombre").text = persona.nombre
            ET.SubElement(persona_xml, "Edad").text = str(persona.edad)
            ET.SubElement(persona_xml, "Carrera").text = persona.carrera

        arbol = ET.ElementTree(raiz)
        arbol.write(nombre_archivo)


    def leer(self, nombre_archivo):

        arbol = ET.parse(nombre_archivo)
        raiz = arbol.getroot()

        print("\n=== CONTENIDO DEL XML ===")

        print("\nDatos Básicos:")
        for elemento in raiz.find("DatosBasicos"):
            print(elemento.tag, ":", elemento.text)

        print("\nArreglo:")
        for elemento in raiz.find("Arreglo"):
            print(elemento.text)

        print("\nMatriz:")
        for fila in raiz.find("Matriz"):
            valores = [valor.text for valor in fila]
            print(valores)

        print("\nPersonas:")
        for persona in raiz.find("Personas"):
            nombre = persona.find("Nombre").text
            edad = persona.find("Edad").text
            carrera = persona.find("Carrera").text
            print(nombre, edad, carrera)


class Sistema:

    def ejecutar(self):

        # ----- Datos Básicos -----
        print("=== CAPTURA DATOS BÁSICOS ===")
        universidad = input("Universidad: ")
        materia = input("Materia: ")

        datos_basicos = {
            "Universidad": universidad,
            "Materia": materia
        }

        # ----- Arreglo Simple -----
        print("\n=== CAPTURA ARREGLO SIMPLE ===")
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
            personas.append(persona)

        # ----- Guardar y Leer -----
        manejador = ManejadorXML()
        manejador.escribir("datos.xml", datos_basicos, arreglo, matriz, personas)
        manejador.leer("datos.xml")



if __name__ == "__main__":
    sistema = Sistema()
    sistema.ejecutar()