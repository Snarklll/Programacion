#include <iostream>
using namespace std;

class BubbleSort {
private:
    int arr[5] = {5,2,4,1,3};

public:
    void ordenar() {
        for(int i=0;i<4;i++)
            for(int j=0;j<4-i;j++)
                if(arr[j]>arr[j+1])
                    swap(arr[j],arr[j+1]);
    }

    void mostrar() {
        for(int i=0;i<5;i++)
            cout<<arr[i]<<" ";
    }
};

int main() {
    BubbleSort b;
    b.ordenar();
    b.mostrar();
}