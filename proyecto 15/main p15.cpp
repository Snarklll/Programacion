#include <iostream>
using namespace std;

class Fibonacci {
public:
    int calcular(int n) {
        if(n<=1) return n;
        return calcular(n-1)+calcular(n-2);
    }
};

int main() {
    Fibonacci f;
    for(int i=0;i<10;i++)
        cout<<f.calcular(i)<<" ";
}