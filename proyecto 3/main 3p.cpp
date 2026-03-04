#include <iostream>
using namespace std;

int main() {
    int a, b;
    char op;

    cout << "Ingresa dos numeros: ";
    cin >> a >> b;
    cout << "Operacion (+ - * /): ";
    cin >> op;

    switch(op) {
        case '+': cout << a + b; break;
        case '-': cout << a - b; break;
        case '*': cout << a * b; break;
        case '/': 
            if(b != 0) cout << (float)a / b;
            else cout << "Error division entre 0";
            break;
        default: cout << "Operacion invalida";
    }

    return 0;
}