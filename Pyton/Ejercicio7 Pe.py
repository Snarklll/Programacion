def crear_auto(precio, anio):
    return {
        "precio": precio,
        "anio": anio
    }

def crear_persona(nombre, ap, am, genero, edad):
    return {
        "nombre": nombre,
        "apellido_paterno": ap,
        "apellido_materno": am,
        "genero": genero,
        "edad": edad
    }

def mostrar_auto(auto):
    print("Auto")
    print("Precio:", auto["precio"])
    print("Año:", auto["anio"])

def mostrar_persona(persona):
    print("Persona")
    print("Nombre completo:", persona["nombre"], persona["apellido_paterno"], persona["apellido_materno"])
    print("Genero:", persona["genero"])
    print("Edad:", persona["edad"])

def main():
    precio = float(input("Ingrese precio del auto: "))
    anio = int(input("Ingrese año del auto: "))
    auto = crear_auto(precio, anio)

    nombre = input("Ingrese nombre: ")
    ap = input("Ingrese apellido paterno: ")
    am = input("Ingrese apellido materno: ")
    genero = input("Ingrese genero: ")
    edad = int(input("Ingrese edad: "))
    persona = crear_persona(nombre, ap, am, genero, edad)

    mostrar_auto(auto)
    mostrar_persona(persona)

if __name__ == "__main__":
    main()