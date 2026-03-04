#include <iostream>
using namespace std;

class Multiplicacion {
private:
    int a, b;

public:
    Multiplicacion(int x, int y) {
        a = x;
        b = y;
    }

    int calcular() {
        int resultado = 0;
        for(int i = 0; i < b; i++)
            resultado += a;
        return resultado;
    }
};

int main() {
    Multiplicacion m(5,3);
    cout << "Resultado: " << m.calcular();
    return 0;
}