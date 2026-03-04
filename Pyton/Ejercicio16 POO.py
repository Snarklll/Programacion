class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __gt__(self, other):
        return self.edad > other.edad

    def __str__(self):
        return f"{self.nombre} ({self.edad})"


class Ordenador:
    def __init__(self, datos):
        self.datos = datos

    def burbuja(self):
        n = len(self.datos)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.datos[j] > self.datos[j + 1]:
                    self.datos[j], self.datos[j + 1] = self.datos[j + 1], self.datos[j]
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
        resultado = ordenador.burbuja()

        print("Lista ordenada:")
        for elemento in resultado:
            print(elemento)


app = Aplicacion()
app.ejecutar()