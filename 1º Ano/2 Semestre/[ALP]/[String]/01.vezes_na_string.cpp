/*
    Elabore um programa que leia um caracter e uma string
    de no máximo 20 caracteres. O programa deverá determinar
    o número de vezes que esse caractere aparece na string.
 */
#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
    char caracter;
    cout << "Digite o caracter: "; 
    cin >> caracter;

    char string[20];
    cout << "\nDigite a palavra e ou frase: ";
    cin >> string;
    // fgets(string, 20, in);

    int vezes = 0;

    for(int i =0; string[i] != '\0'; i++) if (tolower(string[i]) == tolower(caracter)) vezes++;

    cout << "\nA letra " << caracter << " Aparece " << vezes << " vezes na palavra " << string;

    return 0; 
}