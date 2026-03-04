class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __lt__(self, other):
        return self.edad < other.edad

    def __str__(self):
        return f"{self.nombre} ({self.edad})"


def merge_indices(lista, izq, der):
    resultado = []
    i = 0
    j = 0

    while i < len(izq) and j < len(der):
        if lista[izq[i]] < lista[der[j]]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado


def merge_sort_indirecto(lista, indices):
    if len(indices) <= 1:
        return indices

    medio = len(indices) // 2
    izq = merge_sort_indirecto(lista, indices[:medio])
    der = merge_sort_indirecto(lista, indices[medio:])

    return merge_indices(lista, izq, der)


def ordenar_indirecto_merge(lista):
    indices = list(range(len(lista)))
    return merge_sort_indirecto(lista, indices)


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
indices_ordenados = ordenar_indirecto_merge(datos)

print("Orden original:")
for x in datos:
    print(x)

print("Ordenado indirectamente:")
for i in indices_ordenados:
    print(datos[i])