/*Fazer um programa em C para ler um vetor de inteiros positivos
de 15 posições. Imprimir a quantidade de números pares e a
quantidade de múltiplos de 5*/
#include <iostream>
using namespace std;

void set_val(int vec[], int len){
    for(int pos = 0; pos < len; pos++){
        cout << "Digite a posicao " << pos+1 << " Para o Vetor X: ";
        cin >> vec[pos];
        cout << "-------------------------------------" << endl;
    }
}

int main(){
    int vec[15];
    set_val(vec, 15);

    int pares = 0, multi_cinco = 0;

    for(int i=0; i < 15; i++){
        if(vec[i]%2 == 0) pares++;
        if(vec[i]%5 == 0) multi_cinco++;
    }

    cout << "Pares: " << pares << endl;
    cout << "Multiplos de cinco: " << multi_cinco << endl;

}