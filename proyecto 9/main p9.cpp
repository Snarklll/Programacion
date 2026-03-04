#include <iostream>
using namespace std;

class Estadisticas {
private:
    int datos[5];

public:
    void ingresar() {
        for(int i=0;i<5;i++)
            cin >> datos[i];
    }

    void calcular() {
        int suma=0, max=datos[0], min=datos[0];

        for(int i=0;i<5;i++){
            suma+=datos[i];
            if(datos[i]>max) max=datos[i];
            if(datos[i]<min) min=datos[i];
        }

        cout << "Suma: " << suma << endl;
        cout << "Max: " << max << endl;
        cout << "Min: " << min << endl;
    }
};

int main() {
    Estadisticas e;
    e.ingresar();
    e.calcular();
}