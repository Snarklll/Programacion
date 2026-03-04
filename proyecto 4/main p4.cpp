#include <iostream>
using namespace std;

class Arreglo {
private:
    int datos[5];

public:
    void ingresar() {
        cout << "Ingresa 5 numeros: ";
        for (int i = 0; i < 5; i++)
            cin >> datos[i];
    }

    int suma() {
        int s = 0;
        for (int i = 0; i < 5; i++)
            s += datos[i];
        return s;
    }
};

int main() {
    Arreglo obj;
    obj.ingresar();
    cout << "Suma: " << obj.suma() << endl;
    return 0;
}