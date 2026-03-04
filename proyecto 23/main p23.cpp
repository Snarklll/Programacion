#include <iostream>
using namespace std;

class Animal {
public:
    virtual void sonido() {
        cout << "Sonido generico\n";
    }
};

class Perro : public Animal {
public:
    void sonido() override {
        cout << "Guau\n";
    }
};

int main() {
    Animal* a;
    Perro p;
    a = &p;
    a->sonido();
    return 0;
}