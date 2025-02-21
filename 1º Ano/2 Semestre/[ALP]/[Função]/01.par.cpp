#include <iostream>
using namespace std;

bool par(int num){
    return (num%2==0);
}

int main(){
    int num;
    cout << "Digite o valor: ";
    cin >> num;

    if(par(num)) cout << "EH PAR";
    else cout << "Eh impar";

    return 0;
}