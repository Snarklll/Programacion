#include <iostream>
using namespace std;

class Figura {
public:
    virtual double area() = 0;
};

class Rectangulo : public Figura {
private:
    double base, altura;

public:
    Rectangulo(double b, double a) {
        base = b;
        altura = a;
    }

    double area() override {
        return base * altura;
    }
};

int main() {
    Rectangulo r(5, 3);
    cout << "Area: " << r.area() << endl;
    return 0;
}