class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __lt__(self, other):
        return self.edad < other.edad

    def __str__(self):
        return f"{self.nombre} ({self.edad})"


def burbuja_indirecta(lista):
    indices = list(range(len(lista)))
    n = len(indices)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[indices[j + 1]] < lista[indices[j]]:
                indices[j], indices[j + 1] = indices[j + 1], indices[j]

    return indices


def ingresar_datos():
    print("Seleccione el tipo de dato a ordenar:")
    print("1. Enteros")
    print("2. Caracteres")
    print("3. Persona (nombre y edad)")
    opcion = input("Opción: ")

    if opcion == "1":
        datos = list(map(int, input("Ingrese los números separados por espacio: ").split()))
        return datos

    elif opcion == "2":
        datos = list(input("Ingrese los caracteres sin espacios: "))
        return datos

    elif opcion == "3":
        cantidad = int(input("¿Cuántas personas desea ingresar?: "))
        personas = []
        for _ in range(cantidad):
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            personas.append(Persona(nombre, edad))
        return personas

    else:
        print("Opción no válida")
        return []


datos = ingresar_datos()
indices_ordenados = burbuja_indirecta(datos)

print("Orden original:")
for elemento in datos:
    print(elemento)

print("Ordenado indirectamente:")
for i in indices_ordenados:
    print(datos[i])