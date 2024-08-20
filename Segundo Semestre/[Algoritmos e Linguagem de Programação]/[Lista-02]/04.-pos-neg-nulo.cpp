#include <iostream>
using namespace std;

int main(){
    int num;
    cout << "Digite o numero: ";
    cin >> num;
 
    if(num > 0){
        printf("Numero eh positivo!");
    }else if(num < 0){
        printf("Numero eh negativo!");
    }else{
        printf("Numero eh nulo!");
    }
}