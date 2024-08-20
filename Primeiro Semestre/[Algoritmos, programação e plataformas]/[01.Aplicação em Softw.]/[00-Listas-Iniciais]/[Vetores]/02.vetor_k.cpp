/*
Fazer um programa que faz a leitura de um vetor X com N inteiros,
com tamanho máximo igual a 20 e N deverá ser lido. Multiplique
cada elemento do vetor por um inteiro K(K também deverá ser lido).
Imprimir o vetor lido, o valor da variável K e o vetor multiplicado por K.
*/
#include <iostream>
using namespace std;

int get_n(){
    int n;
    while(true){
        cout << "Digite o valor de N: ";
        cin >> n;
        if(n > 20 || n <= 0){
            cout << "\nDigite um valor valido!\n";
            continue;
        }
        break;
    }
    return n;
}

void set_val(int vec[], int pos){
    cout << "\nDigite a posicao " << pos << " Para o Vetor X: ";
    cin >> vec[pos];
}

void get_vec(int vec[], int n){
    for(int position = 0; position < n; position++) cout <<"Z"<< position << ": "<< vec[position] << endl;
}

int main(){
    int k;
    cout << "Digite o valor de K: ";
    cin >> k;
    cout << "\n=========================" << endl;

    int n = get_n();
    int x[n];
    int z[n];

    for(int i = 0; i < n; i++){
        set_val(x, i);
        z[i] = k * x[i];
    }    
    get_vec(z, n);
}
