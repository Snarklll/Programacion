#include <iostream>
#include <fstream>
using namespace std;

class Archivo {
public:
    void escribir() {
        ofstream file("datos.txt");
        file << "Hola archivo\n";
        file.close();
    }

    void leer() {
        ifstream file("datos.txt");
        string linea;
        while (getline(file, linea)) {
            cout << linea << endl;
        }
        file.close();
    }
};

int main() {
    Archivo a;
    a.escribir();
    a.leer();
    return 0;
}