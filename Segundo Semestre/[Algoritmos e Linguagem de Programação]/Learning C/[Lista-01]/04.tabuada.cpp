#include <iostream>
using namespace std;

int main()
{
    int num;
    printf("Digite um numero: ");
    cin >> num;

    for(int i=0; i <= 10; i++)
    {
        cout << num << " X " << i << " = " << (i*num) << endl;
    }
}