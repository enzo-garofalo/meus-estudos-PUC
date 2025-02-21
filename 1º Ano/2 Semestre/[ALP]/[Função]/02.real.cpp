#include <iostream>
using namespace std;

float set_num(){
    float num;
    cout << "Digite o valor: ";
    cin >> num;

    return num;
}

float set_fracionario(float num){
    while(num >= 1){
        num = num - 1;
    }
    return num;
}

int main(){
    float num = set_num();
    float fracionario = set_fracionario(num);

    cout << "\nNum fracionario: " << fracionario;

    return 0;
}