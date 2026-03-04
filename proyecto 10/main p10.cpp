#include <iostream>
using namespace std;

class ArregloDinamico {
private:
    int *datos;
    int n;

public:
    ArregloDinamico(int tam) {
        n = tam;
        datos = new int[n];
    }

    void ingresar() {
        for(int i=0;i<n;i++)
            cin >> datos[i];
    }

    ~ArregloDinamico() {
        delete[] datos;
    }
};

int main() {
    ArregloDinamico a(5);
    a.ingresar();
}