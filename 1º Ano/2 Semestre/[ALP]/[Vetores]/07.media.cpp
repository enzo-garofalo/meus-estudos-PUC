/*ler um vetor A com 10 elementos inteiros correspondentes as
idades de um grupo de pessoas. Escreva um programa que
determine e escreva a idade média dos elementos lidos e
quantos elementos são menores que a média.*/
#include <iostream>
using namespace std;

int set_val(int vec[], int len){
    int soma = 0;
    for(int pos = 0; pos < len; pos++){
        cout << "Digite a a idade do elemento " << pos+1 << ": ";
        cin >> vec[pos];
        cout << "-------------------------------------" << endl;
        soma += vec[pos];
    }
    return (soma/10);
}

int main(){
    int vec[10];
    float media = set_val(vec, 10);
    float abaixo = 0;

    for(int i=0; i < 10; i++) if(vec[i] < media) abaixo++; 
    
    cout << "Mehdia: " << media << endl;
    cout << "Elementos abaixo da mehdia: " << abaixo << endl;

}