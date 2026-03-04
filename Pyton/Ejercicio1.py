def mostrar_mensaje():
    print("Hola Mundo desde función")


class Mensaje:
    def __init__(self, texto):
        self._texto = texto

    def obtener_texto(self):
        return self._texto


class Impresora:
    def imprimir(self, mensaje: Mensaje):
        print(mensaje.obtener_texto())


class Aplicacion:
    def __init__(self, mensaje: Mensaje, impresora: Impresora):
        self._mensaje = mensaje
        self._impresora = impresora

    def ejecutar(self):
        print("Hola Mundo desde main")
        mostrar_mensaje()
        self._impresora.imprimir(self._mensaje)


if __name__ == "__main__":
    mensaje = Mensaje("Hola Mundo desde clase POO")
    impresora = Impresora()
    app = Aplicacion(mensaje, impresora)
    app.ejecutar()