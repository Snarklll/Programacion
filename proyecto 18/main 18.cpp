#include <iostream>
using namespace std;

class SelectionSort {
private:
    int arr[5] = {5,4,3,2,1};

public:
    void ordenar() {
        for(int i=0;i<4;i++){
            int min=i;
            for(int j=i+1;j<5;j++)
                if(arr[j]<arr[min])
                    min=j;
            swap(arr[i],arr[min]);
        }
    }

    void mostrar() {
        for(int i=0;i<5;i++)
            cout<<arr[i]<<" ";
    }
};

int main() {
    SelectionSort s;
    s.ordenar();
    s.mostrar();
}