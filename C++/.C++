#1 Hola mundo 

#include <iostream>
using namespace std;

int main() {
    cout << "Hola Mundo" << endl;
    return 0;
}

#2 Suma con función 

#include <iostream>
using namespace std;

int suma(int a, int b) {
    return a + b;
}

int main() {
    int x, y;
    cout << "Ingresa dos numeros: ";
    cin >> x >> y;
    cout << "Resultado: " << suma(x, y) << endl;
    return 0;
}

#3 Calculadora 

#include <iostream>
using namespace std;

int main() {
    int a, b;
    char op;

    cout << "Ingresa dos numeros: ";
    cin >> a >> b;
    cout << "Operacion (+ - * /): ";
    cin >> op;

    switch(op) {
        case '+': cout << a + b; break;
        case '-': cout << a - b; break;
        case '*': cout << a * b; break;
        case '/': 
            if(b != 0) cout << (float)a / b;
            else cout << "Error division entre 0";
            break;
        default: cout << "Operacion invalida";
    }

    return 0;
}

#4 Arreglo como clase 

#include <iostream>
using namespace std;

class Arreglo {
private:
    int datos[5];

public:
    void ingresar() {
        cout << "Ingresa 5 numeros: ";
        for (int i = 0; i < 5; i++)
            cin >> datos[i];
    }

    int suma() {
        int s = 0;
        for (int i = 0; i < 5; i++)
            s += datos[i];
        return s;
    }
};

int main() {
    Arreglo obj;
    obj.ingresar();
    cout << "Suma: " << obj.suma() << endl;
    return 0;
}

#5 Clase persona con constructor 

#include <iostream>
#include <string>
using namespace std;

class Persona {
private:
    string nombre;
    int edad;

public:
    Persona(string n, int e) {
        nombre = n;
        edad = e;
    }

    void mostrar() {
        cout << "Nombre: " << nombre << endl;
        cout << "Edad: " << edad << endl;
    }
};

int main() {
    Persona p("Juan", 20);
    p.mostrar();
    return 0;
}

#6 multiplicación con método 

#include <iostream>
using namespace std;

class Multiplicacion {
private:
    int a, b;

public:
    Multiplicacion(int x, int y) {
        a = x;
        b = y;
    }

    int calcular() {
        int resultado = 0;
        for(int i = 0; i < b; i++)
            resultado += a;
        return resultado;
    }
};

int main() {
    Multiplicacion m(5,3);
    cout << "Resultado: " << m.calcular();
    return 0;
}

#7 clase persona con encapsulamiento 

#include <iostream>
#include <string>
using namespace std;

class Persona {
private:
    string nombre;
    int edad;

public:
    void setDatos(string n, int e) {
        nombre = n;
        edad = e;
    }

    void mostrar() {
        cout << nombre << " - " << edad << endl;
    }
};

int main() {
    Persona p;
    p.setDatos("Ana", 21);
    p.mostrar();
}

#8 tamaño de arreglo en clase 

#include <iostream>
using namespace std;

class Arreglo {
private:
    int datos[5];

public:
    void mostrarTamano() {
        cout << "Tamano en bytes: " << sizeof(datos) << endl;
    }
};

int main() {
    Arreglo a;
    a.mostrarTamano();
}



#9 suma, mayor y menor 

#include <iostream>
using namespace std;

class Estadisticas {
private:
    int datos[5];

public:
    void ingresar() {
        for(int i=0;i<5;i++)
            cin >> datos[i];
    }

    void calcular() {
        int suma=0, max=datos[0], min=datos[0];

        for(int i=0;i<5;i++){
            suma+=datos[i];
            if(datos[i]>max) max=datos[i];
            if(datos[i]<min) min=datos[i];
        }

        cout << "Suma: " << suma << endl;
        cout << "Max: " << max << endl;
        cout << "Min: " << min << endl;
    }
};

int main() {
    Estadisticas e;
    e.ingresar();
    e.calcular();
}

#10 #include <iostream>

using namespace std;

class ArregloDinamico {
private:
    int *datos;
    int n;

public:
    ArregloDinamico(int tam) {
        n = tam;
        datos = new int[n];
    }

    void ingresar() {
        for(int i=0;i<n;i++)
            cin >> datos[i];
    }

    ~ArregloDinamico() {
        delete[] datos;
    }
};

int main() {
    ArregloDinamico a(5);
    a.ingresar();
}

#11 multiplicación de matrices 

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

#12 vector de objetos 

#include <iostream>
#include <vector>
using namespace std;

class Persona {
public:
    string nombre;
    int edad;
};

class Grupo {
private:
    vector<Persona> personas;

public:
    void agregar(string n, int e) {
        personas.push_back({n,e});
    }

    void mostrar() {
        for(auto p : personas)
            cout << p.nombre << " " << p.edad << endl;
    }
};

int main() {
    Grupo g;
    g.agregar("Ana",20);
    g.agregar("Luis",22);
    g.mostrar();
}







#13 vector de punteros 

#include <iostream>
#include <vector>
using namespace std;

class Persona {
public:
    string nombre;
    int edad;
};

class Grupo {
private:
    vector<Persona*> personas;

public:
    void agregar(string n, int e) {
        personas.push_back(new Persona{n,e});
    }

    void mostrar() {
        for(auto p : personas)
            cout << p->nombre << " " << p->edad << endl;
    }

    ~Grupo() {
        for(auto p : personas)
            delete p;
    }
};

int main() {
    Grupo g;
    g.agregar("Ana",20);
    g.agregar("Luis",22);
    g.mostrar();
}

#14 factorial 

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
#15 Fibonacci 
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

#16 bubble sort

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



#17 insertion sort 

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

#18 Selection sort 

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

#19 merge sort 

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

Quick sort #20

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

PRÁCTICA 21 – Clase CuentaBancaria

#include <iostream>
using namespace std;

class CuentaBancaria {
private:
    double saldo;

public:
    CuentaBancaria(double s) {
        saldo = s;
    }

    void depositar(double cantidad) {
        saldo += cantidad;
    }

    void retirar(double cantidad) {
        if (cantidad <= saldo)
            saldo -= cantidad;
        else
            cout << "Fondos insuficientes\n";
    }

    void mostrar() {
        cout << "Saldo actual: $" << saldo << endl;
    }
};

int main() {
    CuentaBancaria cuenta(1000);
    cuenta.depositar(500);
    cuenta.retirar(200);
    cuenta.mostrar();
    return 0;
}


PRÁCTICA 22 – Herencia (Empleado)

#include <iostream>
using namespace std;

class Persona {
protected:
    string nombre;

public:
    Persona(string n) {
        nombre = n;
    }
};

class Empleado : public Persona {
private:
    double salario;

public:
    Empleado(string n, double s) : Persona(n) {
        salario = s;
    }

    void mostrar() {
        cout << "Nombre: " << nombre << endl;
        cout << "Salario: $" << salario << endl;
    }
};

int main() {
    Empleado emp("Carlos", 15000);
    emp.mostrar();
    return 0;
}

PRÁCTICA 23 – Polimorfismo

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

PRÁCTICA 24 – Clase Archivo (Lectura/Escritura)
#include <iostream>
#include <fstream>
using namespace std;

class Archivo {
public:
    void escribir() {
        ofstream file("datos.txt");
        file << "Hola archivo\n";
        file.close();
    }

    void leer() {
        ifstream file("datos.txt");
        string linea;
        while (getline(file, linea)) {
            cout << linea << endl;
        }
        file.close();
    }
};

int main() {
    Archivo a;
    a.escribir();
    a.leer();
    return 0;
}







PRÁCTICA 25 – Clase Figura (Clase Abstracta)

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

PRÁCTICA 26 – Sobrecarga de Operadores

#include <iostream>
using namespace std;

class Numero {
private:
    int valor;

public:
    Numero(int v) {
        valor = v;
    }

    Numero operator+(Numero n) {
        return Numero(valor + n.valor);
    }

    void mostrar() {
        cout << "Resultado: " << valor << endl;
    }
};

int main() {
    Numero n1(5), n2(7);
    Numero n3 = n1 + n2;
    n3.mostrar();
    return 0;
}


