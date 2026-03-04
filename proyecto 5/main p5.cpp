#include <iostream>
#include <string>
using namespace std;

class Persona {
private:
    string nombre;
    int edad;

public:
    Persona(string n, int e) {
        nombre = n;
        edad = e;
    }

    void mostrar() {
        cout << "Nombre: " << nombre << endl;
        cout << "Edad: " << edad << endl;
    }
};

int main() {
    Persona p("Juan", 20);
    p.mostrar();
    return 0;
}