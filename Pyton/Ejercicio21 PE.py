class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __lt__(self, other):
        return self.edad < other.edad

    def __str__(self):
        return f"{self.nombre} ({self.edad})"


def quick_sort_indirecto(lista, indices):
    if len(indices) <= 1:
        return indices

    pivote = indices[len(indices) // 2]
    menores = []
    iguales = []
    mayores = []

    for idx in indices:
        if lista[idx] < lista[pivote]:
            menores.append(idx)
        elif lista[pivote] < lista[idx]:
            mayores.append(idx)
        else:
            iguales.append(idx)

    return quick_sort_indirecto(lista, menores) + iguales + quick_sort_indirecto(lista, mayores)


def ordenar_indirecto(lista):
    indices = list(range(len(lista)))
    return quick_sort_indirecto(lista, indices)


def ingresar_datos():
    print("Seleccione el tipo de dato a ordenar:")
    print("1. Enteros")
    print("2. Caracteres")
    print("3. Persona (nombre y edad)")
    opcion = input("Opción: ")

    if opcion == "1":
        return list(map(int, input("Ingrese los números separados por espacio: ").split()))

    if opcion == "2":
        return list(input("Ingrese los caracteres sin espacios: "))

    if opcion == "3":
        cantidad = int(input("¿Cuántas personas desea ingresar?: "))
        personas = []
        for _ in range(cantidad):
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            personas.append(Persona(nombre, edad))
        return personas

    print("Opción no válida")
    return []


datos = ingresar_datos()
indices_ordenados = ordenar_indirecto(datos)

print("Orden original:")
for x in datos:
    print(x)

print("Ordenado indirectamente:")
for i in indices_ordenados:
    print(datos[i])