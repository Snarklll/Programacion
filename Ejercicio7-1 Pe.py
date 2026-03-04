import sys

def identificar_tipo(dato):
    try:
        valor = int(dato)
        return valor, "int", "basico"
    except ValueError:
        try:
            valor = float(dato)
            return valor, "float", "basico"
        except ValueError:
            if dato.lower() == "true" or dato.lower() == "false":
                valor = dato.lower() == "true"
                return valor, "bool", "basico"
            else:
                return dato, "str", "basico"

def calcular_tamano(valor):
    return sys.getsizeof(valor)

def mostrar_resultado(valor, tipo, categoria):
    tamano = calcular_tamano(valor)
    print("Tipo detectado:", tipo)
    print("Categoria:", categoria)
    print("Tamaño en bytes:", tamano)

def main():
    dato = input("Ingrese un dato: ")
    valor, tipo, categoria = identificar_tipo(dato)
    mostrar_resultado(valor, tipo, categoria)

if __name__ == "__main__":
    main()