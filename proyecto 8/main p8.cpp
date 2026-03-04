#include <iostream>
using namespace std;

class Arreglo {
private:
    int datos[5];

public:
    void mostrarTamano() {
        cout << "Tamano en bytes: " << sizeof(datos) << endl;
    }
};

int main() {
    Arreglo a;
    a.mostrarTamano();
}