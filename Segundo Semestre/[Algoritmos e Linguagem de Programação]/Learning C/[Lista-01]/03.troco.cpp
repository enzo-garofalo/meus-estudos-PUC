#include <iostream>

int main(){
    int compra;
    int valor_pago;
    
    printf("Digite o valor do produto: ");
    std::cin >> compra;

    printf("Digite o valor pago: ");
    std::cin >>  valor_pago;

    int troco = valor_pago - compra;
    std::cout << "Troco: " << troco << std::endl;
    
    int vinte, dez, cinco, dois, um;

    vinte = troco / 20;
    troco = troco - (vinte*20);

    dez = troco/10;
    troco = troco - (dez*10);
    
    cinco = troco/5;
    troco = troco - (cinco*5);
    
    dois = troco/2;
    troco = troco - (dois*2);

    std::cout << "20.00 : " << vinte << " Cedulas"<< std::endl;
    std::cout << "10.00 : " << dez << " Cedulas"<< std::endl;
    std::cout << "5.00 : " << cinco << " Cedulas"<< std::endl;
    std::cout << "2.00 : " << dois << " Cedulas"<< std::endl;
    std::cout << "1.00 : " << troco << " Cedulas"<< std::endl;
}