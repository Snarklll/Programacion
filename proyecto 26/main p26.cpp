#include <iostream>
using namespace std;

class Numero {
private:
    int valor;

public:
    Numero(int v) {
        valor = v;
    }

    Numero operator+(Numero n) {
        return Numero(valor + n.valor);
    }

    void mostrar() {
        cout << "Resultado: " << valor << endl;
    }
};

int main() {
    Numero n1(5), n2(7);
    Numero n3 = n1 + n2;
    n3.mostrar();
    return 0;
}