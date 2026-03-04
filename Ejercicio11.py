from abc import ABC, abstractmethod

class OperacionMatriz(ABC):
    @abstractmethod
    def ejecutar(self, *args):
        pass

class MultiplicacionPorConstante(OperacionMatriz):
    def ejecutar(self, matriz, constante):
        resultado = []
        for fila in matriz:
            nueva_fila = []
            for elemento in fila:
                nueva_fila.append(elemento * constante)
            resultado.append(nueva_fila)
        return resultado

class MultiplicacionMatrices(OperacionMatriz):
    def ejecutar(self, matriz_a, matriz_b):
        filas_a = len(matriz_a)
        columnas_a = len(matriz_a[0])
        filas_b = len(matriz_b)
        columnas_b = len(matriz_b[0])

        if columnas_a != filas_b:
            raise ValueError("No se pueden multiplicar las matrices")

        resultado = []
        for i in range(filas_a):
            fila_resultado = []
            for j in range(columnas_b):
                suma = 0
                for k in range(columnas_a):
                    suma += matriz_a[i][k] * matriz_b[k][j]
                fila_resultado.append(suma)
            resultado.append(fila_resultado)
        return resultado

class LectorMatriz:
    def leer_matriz(self, nombre):
        filas = int(input(f"Ingrese numero de filas de {nombre}: "))
        columnas = int(input(f"Ingrese numero de columnas de {nombre}: "))
        matriz = []
        for i in range(filas):
            fila = input(f"Ingrese fila {i+1} separada por espacios: ")
            valores = [float(x) for x in fila.split()]
            matriz.append(valores)
        return matriz

class Aplicacion:
    def __init__(self):
        self.lector = LectorMatriz()
        self.multiplicacion_constante = MultiplicacionPorConstante()
        self.multiplicacion_matrices = MultiplicacionMatrices()

    def mostrar_matriz(self, matriz):
        for fila in matriz:
            print(fila)

    def ejecutar(self):
        matriz_a = self.lector.leer_matriz("A")
        matriz_b = self.lector.leer_matriz("B")

        constante = float(input("Ingrese una constante para multiplicar A: "))

        resultado_constante = self.multiplicacion_constante.ejecutar(matriz_a, constante)
        print("Resultado A * constante:")
        self.mostrar_matriz(resultado_constante)

        try:
            resultado_matrices = self.multiplicacion_matrices.ejecutar(matriz_a, matriz_b)
            print("Resultado A * B:")
            self.mostrar_matriz(resultado_matrices)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()