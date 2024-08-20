/*Fazer um programa que faz a leitura de um vetor x,
com n inteiros, com tamanho máximo igual a 20 e N deverá ser lido.
Gere um segundo vetor com os valores do vetor X em ordem inversa. 
Imprimir o vetor X e vetor com a ordem inversa.*/
#include <iostream>
using namespace std;

int get_n(){
    int n;
    while(true){
        cout << "Digite o valor de N: ";
        cin >> n;
        cout << endl;
        if(n > 20 || n <= 0){
            cout << "Digite um valor valido!\n";
            continue;
        }
        break;
    }
    return n;
}

void set_val(int vec[], int len){
    for(int pos = 0; pos < len; pos++){
        cout << "Digite a posicao " << pos << " Para o Vetor X: ";
        cin >> vec[pos];
        cout << "-------------------------------------" << endl;
    }
}

void get_inverse_vec(int vec[], int len){
    cout << "Vetor em ordem inversa: " << endl;
    for(int i = len-1; i >= 0; i--) cout << "X["<< i << "]: " << vec[i] << endl; 
}

int main(){
    int n = get_n();
    int x[n];
    set_val(x, n);
    get_inverse_vec(x, n); 
}