class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __lt__(self, other):
        return self.edad < other.edad

    def __str__(self):
        return f"{self.nombre} ({self.edad})"


class OrdenadorIndirectoMerge:
    def __init__(self, datos):
        self.datos = datos
        self.indices = list(range(len(datos)))

    def merge_indices(self, izq, der):
        resultado = []
        i = 0
        j = 0

        while i < len(izq) and j < len(der):
            if self.datos[izq[i]] < self.datos[der[j]]:
                resultado.append(izq[i])
                i += 1
            else:
                resultado.append(der[j])
                j += 1

        resultado.extend(izq[i:])
        resultado.extend(der[j:])
        return resultado

    def merge_sort_indices(self, indices):
        if len(indices) <= 1:
            return indices

        medio = len(indices) // 2
        izq = self.merge_sort_indices(indices[:medio])
        der = self.merge_sort_indices(indices[medio:])

        return self.merge_indices(izq, der)

    def ordenar(self):
        self.indices = self.merge_sort_indices(self.indices)
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

        ordenador = OrdenadorIndirectoMerge(datos)
        ordenador.ordenar()

        print("Orden original:")
        for x in datos:
            print(x)

        print("Ordenado indirectamente:")
        ordenador.mostrar_ordenado()


app = Aplicacion()
app.ejecutar()