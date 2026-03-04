#include <iostream>
using namespace std;

class QuickSort {
private:
    int arr[5] = {3,5,1,4,2};

    int partition(int low,int high){
        int pivot=arr[high], i=low-1;
        for(int j=low;j<high;j++){
            if(arr[j]<pivot){
                i++;
                swap(arr[i],arr[j]);
            }
        }
        swap(arr[i+1],arr[high]);
        return i+1;
    }

    void quickSort(int low,int high){
        if(low<high){
            int pi=partition(low,high);
            quickSort(low,pi-1);
            quickSort(pi+1,high);
        }
    }

public:
    void ordenar(){
        quickSort(0,4);
    }

    void mostrar(){
        for(int i=0;i<5;i++)
            cout<<arr[i]<<" ";
    }
};

int main(){
    QuickSort q;
    q.ordenar();
    q.mostrar();
}