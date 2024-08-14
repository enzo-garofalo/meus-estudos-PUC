#include <iostream>
using namespace std;

int main()
{
    int num;
    int inverso;
    int resto;
    printf("Digite o número: ");
    cin >> num;

    while( num > 0)
    {
        resto = num%10;
        num = num-resto;
        inverso = inverso + resto*10;
    }
    cout << inverso;

}