#include <iostream>
using namespace std;

int main(){
    // a é uma varíavel do tipo inteiro 
    int a;
    a = 3;

    // b é um ponteiro
    // Ele aponta para um espaço da memória com o tipo inteiro
    // Na linha 12 ele aloca um valor a esse espaço da memoria
    int *b;
    *b  = 7;

    // c é um ponteiro; 
    // ele não aponta para um espaço da memória, pois ele foi inicializado com NULL;
    // c = b, significa que ambos os ponteiros apontam para o mesmo espaço na memória;
    // *c = 9, modifica o valor qual c e b apontam;
    int *c = NULL;
    c = b;
    *c = 9;
    // c = &a, c - ponteiro - aponta para a referência de a (o endereço em que a está alocado);
    // *c = 1, modifica o valor para qual c aponta, portanto modifica a;
    c = &a;
    *c = 1;
    
    return 0;
}