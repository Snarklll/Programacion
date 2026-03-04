#include <iostream>
using namespace std;

class Persona {
protected:
    string nombre;

public:
    Persona(string n) {
        nombre = n;
    }
};

class Empleado : public Persona {
private:
    double salario;

public:
    Empleado(string n, double s) : Persona(n) {
        salario = s;
    }

    void mostrar() {
        cout << "Nombre: " << nombre << endl;
        cout << "Salario: $" << salario << endl;
    }
};

int main() {
    Empleado emp("Carlos", 15000);
    emp.mostrar();
    return 0;
}