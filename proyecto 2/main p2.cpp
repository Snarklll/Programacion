#include <iostream>
using namespace std;

int suma(int a, int b) {
    return a + b;
}

int main() {
    int x, y;
    cout << "Ingresa dos numeros: ";
    cin >> x >> y;
    cout << "Resultado: " << suma(x, y) << endl;
    return 0;
}