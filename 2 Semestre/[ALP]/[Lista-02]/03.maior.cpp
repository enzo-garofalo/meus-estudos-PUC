#include <iostream>
using namespace std;

int main()
{
    int num1, num2;
    printf("Digite um numero: ");
    cin >> num1;
    printf("Digite um numero: ");
    cin >> num2;

    if(num1 > num2){
        cout << num1 << "eh maior";
    }else{
        cout << num2 << "eh maior";

    }
}