import csv
print("=== DATOS BÁSICOS ===")

with open("datos_basicos.csv", "w", newline="") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["Nombre", "Edad"])
    writer.writerow(["Juan", 25])
    writer.writerow(["Ana", 20])

with open("datos_basicos.csv", "r") as archivo:
    reader = csv.reader(archivo)
    for fila in reader:
        print(fila)

print("\n=== ARREGLO SIMPLE ===")

numeros = [10, 40, 20, 5]

with open("arreglo.csv", "w", newline="") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(numeros)

with open("arreglo.csv", "r") as archivo:
    reader = csv.reader(archivo)
    for fila in reader:
        arreglo_leido = [int(x) for x in fila]
        print("Arreglo leído:", arreglo_leido)

print("\n=== ARREGLO CREADO ===")

estudiantes = [
    ["Luis", 22, "Ing"],
    ["Maria", 21, "Derecho"],
    ["Pedro", 23, "Medicina"]
]

with open("matriz.csv", "w", newline="") as archivo:
    writer = csv.writer(archivo)
    writer.writerows(estudiantes)

with open("matriz.csv", "r") as archivo:
    reader = csv.reader(archivo)
    for fila in reader:
        print("Fila:", fila)

print("\n=== ADT ===")

class Persona:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def to_list(self):
        return [self.nombre, self.edad, self.carrera]

    def mostrar(self):
        return f"{self.nombre} - {self.edad} - {self.carrera}"


personas = [
    Persona("Carlos", 24, "Arquitectura"),
    Persona("Elena", 22, "Psicología")
]

# Escribir ADT
with open("adt.csv", "w", newline="") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["Nombre", "Edad", "Carrera"])
    for p in personas:
        writer.writerow(p.to_list())

# Leer ADT
personas_leidas = []

with open("adt.csv", "r") as archivo:
    reader = csv.reader(archivo)
    next(reader)
    for fila in reader:
        persona = Persona(fila[0], int(fila[1]), fila[2])
        personas_leidas.append(persona)

print("Personas leídas:")
for p in personas_leidas:
    print(p.mostrar())