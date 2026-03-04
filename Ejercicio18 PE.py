class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __lt__(self, other):
        return self.edad < other.edad

    def __str__(self):
        return f"{self.nombre} ({self.edad})"


def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[len(lista) // 2]
    menores = []
    iguales = []
    mayores = []

    for elemento in lista:
        if elemento < pivote:
            menores.append(elemento)
        elif pivote < elemento:
            mayores.append(elemento)
        else:
            iguales.append(elemento)

    return quick_sort(menores) + iguales + quick_sort(mayores)


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
ordenados = quick_sort(datos)

print("Lista ordenada:")
for elemento in ordenados:
    print(elemento)