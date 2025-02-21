/*
    Faça um programa que lê uma string de 5 caracterese inverte
    esta string. No final o programa deverá imprimir a string
    original e a invertida.
*/

#include <iostream>
using namespace std;

void set_string(char string[5]){
    cout << "Digite a palavra: ";
    cin >> string;
}

int main(){
    char string[5];
    set_string(string); 

    char inversa[5];
    int pos = 0;
    for(int i = 6; i >= 0; i--){
        inversa[pos] = string[i];
        pos++;
    }

    cout << "Original: " << string;
    cout << "Inversa: " << inversa;

    return 0;
}