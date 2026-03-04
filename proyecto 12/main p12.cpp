#include <iostream>
#include <vector>
using namespace std;

class Persona {
public:
    string nombre;
    int edad;
};

class Grupo {
private:
    vector<Persona> personas;

public:
    void agregar(string n, int e) {
        personas.push_back({n,e});
    }

    void mostrar() {
        for(auto p : personas)
            cout << p.nombre << " " << p.edad << endl;
    }
};

int main() {
    Grupo g;
    g.agregar("Ana",20);
    g.agregar("Luis",22);
    g.mostrar();
}