/*
    Fazer um programa que faz a leitura de um vetor X com N
    reais , com tamanho máximo igual a 20 e N deverá ser lido.
    Calcula o somatório de todos os elementos do vetor.
    Imprimir o vetor lido e o valor do somatório.
    
    - O somatório é dado por: S = S + X[i]; para i = 0, 1, 2, ..., N-1
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

void set_val(float vec[], int len){
    for(int pos = 0; pos < len; pos++){
        cout << "Digite o valor para X[" << pos << "]: ";
        cin >> vec[pos];
        cout << "-------------------------------------" << endl;
    }
}

int main(){
    int n = get_n();
    float x[n];
    float soma = 0;

    cout << "\n-------------------------------------" << endl;
    set_val(x, n);

    for(int i = 0; i < n; i++){
        cout << "\t\t| " << x[i] << " |\n";
        soma += x[i];
    }
    cout << "\tSomatorio: " << soma;
    return 0; 
}