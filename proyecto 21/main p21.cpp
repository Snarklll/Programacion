#include <iostream>
using namespace std;

class CuentaBancaria {
private:
    double saldo;

public:
    CuentaBancaria(double s) {
        saldo = s;
    }

    void depositar(double cantidad) {
        saldo += cantidad;
    }

    void retirar(double cantidad) {
        if (cantidad <= saldo)
            saldo -= cantidad;
        else
            cout << "Fondos insuficientes\n";
    }

    void mostrar() {
        cout << "Saldo actual: $" << saldo << endl;
    }
};

int main() {
    CuentaBancaria cuenta(1000);
    cuenta.depositar(500);
    cuenta.retirar(200);
    cuenta.mostrar();
    return 0;
}