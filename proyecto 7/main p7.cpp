#include <iostream>
#include <string>
using namespace std;

class Persona {
private:
    string nombre;
    int edad;

public:
    void setDatos(string n, int e) {
        nombre = n;
        edad = e;
    }

    void mostrar() {
        cout << nombre << " - " << edad << endl;
    }
};

int main() {
    Persona p;
    p.setDatos("Ana", 21);
    p.mostrar();
}