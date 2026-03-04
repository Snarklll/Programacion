#include <iostream>
using namespace std;

class Matriz {
private:
    int A[2][2], B[2][2], C[2][2];

public:
    void inicializar() {
        A[0][0]=1; A[0][1]=2;
        A[1][0]=3; A[1][1]=4;

        B[0][0]=2; B[0][1]=0;
        B[1][0]=1; B[1][1]=2;
    }

    void multiplicar() {
        for(int i=0;i<2;i++)
            for(int j=0;j<2;j++){
                C[i][j]=0;
                for(int k=0;k<2;k++)
                    C[i][j]+=A[i][k]*B[k][j];
            }
    }

    void mostrar() {
        for(int i=0;i<2;i++){
            for(int j=0;j<2;j++)
                cout<<C[i][j]<<" ";
            cout<<endl;
        }
    }
};

int main() {
    Matriz m;
    m.inicializar();
    m.multiplicar();
    m.mostrar();
}