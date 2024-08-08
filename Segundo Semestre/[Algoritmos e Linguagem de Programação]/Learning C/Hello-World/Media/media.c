#include <stdio.h>
#include <iostream>

int main(){
    float nota1;
    float nota2;
    std::cout << "Digite a primeira nota: ";
    std::cin  >> nota1;

    std::cout << "Digite a segunda nota: ";
    std::cin   >> nota2;
    
    float media = (nota1+nota2)/2;
    std::cout << "Média: ";
    std::cout << media;
}