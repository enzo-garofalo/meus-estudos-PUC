#include <iostream>
using namespace std;

int main()
{
    int base, h;
    
    printf("Digite a base: ");
    cin >> base;

    printf("Digite a altura: ");
    cin >> h;

    if(base == h){
        printf("O quadrilatero eh um quadrado!");
    }else{
        printf("O quadrilatero eh um retangulo!");

    }
}