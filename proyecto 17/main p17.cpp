#include <iostream>
using namespace std;

class InsertionSort {
private:
    int arr[5] = {5,3,4,1,2};

public:
    void ordenar() {
        for(int i=1;i<5;i++){
            int key=arr[i];
            int j=i-1;
            while(j>=0 && arr[j]>key){
                arr[j+1]=arr[j];
                j--;
            }
            arr[j+1]=key;
        }
    }

    void mostrar() {
        for(int i=0;i<5;i++)
            cout<<arr[i]<<" ";
    }
};

int main() {
    InsertionSort i;
    i.ordenar();
    i.mostrar();
}