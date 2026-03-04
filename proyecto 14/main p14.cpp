#include <iostream>
using namespace std;

class Factorial {
public:
    int calcular(int n) {
        if(n<=1) return 1;
        return n * calcular(n-1);
    }
};

int main() {
    Factorial f;
    cout << f.calcular(5);
}