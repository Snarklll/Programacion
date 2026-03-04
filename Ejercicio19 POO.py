class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __lt__(self, other):
        return self.edad < other.edad

    def __str__(self):
        return f"{self.nombre} ({self.edad})"


class OrdenadorIndirecto:
    def __init__(self, datos):
        self.datos = datos
        self.indices = list(range(len(datos)))

    def burbuja_indirecta(self):
        n = len(self.indices)

        for i in range(n):
            for j in range(0, n - i - 1):
                if self.datos[self.indices[j + 1]] < self.datos[self.indices[j]]:
                    self.indices[j], self.indices[j + 1] = self.indices[j + 1], self.indices[j]

        return self.indices

    def mostrar_ordenado(self):
        for i in self.indices:
            print(self.datos[i])


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

        ordenador = OrdenadorIndirecto(datos)
        ordenador.burbuja_indirecta()

        print("Orden original:")
        for elemento in datos:
            print(elemento)

        print("Ordenado indirectamente:")
        ordenador.mostrar_ordenado()


app = Aplicacion()
app.ejecutar()