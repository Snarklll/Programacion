#include <iostream>
using namespace std;

class MergeSort {
private:
    int arr[5] = {5,1,4,2,3};

    void merge(int l,int m,int r){
        int temp[5], i=l, j=m+1, k=0;
        while(i<=m && j<=r)
            temp[k++] = (arr[i]<arr[j]) ? arr[i++] : arr[j++];
        while(i<=m) temp[k++]=arr[i++];
        while(j<=r) temp[k++]=arr[j++];
        for(int i=0;i<k;i++)
            arr[l+i]=temp[i];
    }

    void mergeSort(int l,int r){
        if(l<r){
            int m=(l+r)/2;
            mergeSort(l,m);
            mergeSort(m+1,r);
            merge(l,m,r);
        }
    }

public:
    void ordenar(){
        mergeSort(0,4);
    }

    void mostrar(){
        for(int i=0;i<5;i++)
            cout<<arr[i]<<" ";
    }
};

int main(){
    MergeSort m;
    m.ordenar();
    m.mostrar();
}