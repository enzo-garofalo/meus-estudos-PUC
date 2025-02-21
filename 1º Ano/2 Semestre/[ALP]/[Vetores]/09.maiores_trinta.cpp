/*
    Elaborar um programa que leia um vetor de no máximo 15
    elementos inteiros. O programa deverá imprimir o vetor e
    informar quantos números são maiores que 30.
*/
#include <iostream>
using namespace std;

void set_vec(int vec[], int len){
    cout << "\n-------------------------------------" << endl;
    for(int i = 0; i < len; i++){
        cout << "Preencha VEC[" << i << "]: ";
        cin >> vec[i];
        cout << "-------------------------------------" << endl;
    }
}

int get_n(){
    int n;
    while(true){
        cout << "Digite o valor de N: ";
        cin >> n;
        if(n > 15 || n <= 0){
            cout << "\nDigite um valor valido!\n";
            continue;
        }
        break;
    }
    return n;
}

int main(){
    int n = get_n();
    int vec[n];
    int maior = 0;
    set_vec(vec, n);

    cout << "\tVetor " << endl;
    for(int i = 0; i < n; i++){
        cout << "\t\t| " << vec[i] << " |\n";
        if(vec[i] > 30) maior++;
    } 

    cout << "Numeros maiores que 30: " << maior;
    return 0;
}