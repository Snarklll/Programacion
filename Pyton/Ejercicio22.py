class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None  # referencia al mismo tipo de dato

    def __lt__(self, other):
        return self.valor < other.valor

    def __le__(self, other):
        return self.valor <= other.valor

    def __str__(self):
        return str(self.valor)


class QuickSort:
    def ordenar(self, lista):
        if len(lista) <= 1:
            return lista
        else:
            pivote = lista[0]
            menores = [x for x in lista[1:] if x <= pivote]
            mayores = [x for x in lista[1:] if x > pivote]
            return self.ordenar(menores) + [pivote] + self.ordenar(mayores)


n1 = Nodo(40)
n2 = Nodo(10)
n3 = Nodo(30)
n4 = Nodo(20)

n1.siguiente = n2
n2.siguiente = n3
n3.siguiente = n4

# Convertimos a lista para aplicar QuickSort
lista_nodos = [n1, n2, n3, n4]

# Ordenar
qs = QuickSort()
ordenados = qs.ordenar(lista_nodos)

print("Nodos ordenados:")
for nodo in ordenados:
    print(nodo)