#include <iostream>
using namespace std;

int main()
{
    int num;
    int inverso = 0; // Initialize inverso to 0
    int resto;

    cout << "Digite o numero: ";
    cin >> num;

    while(num > 0){
        resto = num % 10;
        inverso = 10 * inverso + resto;
        num = num / 10;
    }

    cout << "Numero invertido: " << inverso << endl;

    return 0;
}
