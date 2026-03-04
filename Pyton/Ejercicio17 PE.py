class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __lt__(self, other):
        return self.edad < other.edad

    def __str__(self):
        return f"{self.nombre} ({self.edad})"


def merge(lista_izquierda, lista_derecha):
    resultado = []
    i = 0
    j = 0

    while i < len(lista_izquierda) and j < len(lista_derecha):
        if lista_izquierda[i] < lista_derecha[j]:
            resultado.append(lista_izquierda[i])
            i += 1
        else:
            resultado.append(lista_derecha[j])
            j += 1

    resultado.extend(lista_izquierda[i:])
    resultado.extend(lista_derecha[j:])
    return resultado


def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])

    return merge(izquierda, derecha)


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
ordenados = merge_sort(datos)

print("Lista ordenada:")
for elemento in ordenados:
    print(elemento)