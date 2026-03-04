class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __lt__(self, other):
        return self.edad < other.edad

    def __str__(self):
        return f"{self.nombre} ({self.edad})"


class Ordenador:
    def __init__(self, datos):
        self.datos = datos

    def merge(self, izquierda, derecha):
        resultado = []
        i = 0
        j = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1

        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])
        return resultado

    def merge_sort(self, lista):
        if len(lista) <= 1:
            return lista

        medio = len(lista) // 2
        izquierda = self.merge_sort(lista[:medio])
        derecha = self.merge_sort(lista[medio:])

        return self.merge(izquierda, derecha)

    def ordenar(self):
        self.datos = self.merge_sort(self.datos)
        return self.datos


class Aplicacion:
    def ejecutar(self):
        print("Seleccione el tipo de dato a ordenar:")
        print("1. Enteros")
        print("2. Caracteres")
        print("3. Persona (nombre y edad)")
        opcion = input("Opción: ")

        if opcion == "1":
            datos = list(map(int, input("Ingrese los números separados por espacio: ").split()))
        elif opcion == "2":
            datos = list(input("Ingrese los caracteres sin espacios: "))
        elif opcion == "3":
            cantidad = int(input("¿Cuántas personas desea ingresar?: "))
            datos = []
            for _ in range(cantidad):
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                datos.append(Persona(nombre, edad))
        else:
            print("Opción no válida")
            return

        ordenador = Ordenador(datos)
        resultado = ordenador.ordenar()

        print("Lista ordenada:")
        for elemento in resultado:
            print(elemento)


app = Aplicacion()
app.ejecutar() 