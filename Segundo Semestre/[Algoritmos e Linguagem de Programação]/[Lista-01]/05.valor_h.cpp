#include <iostream>
using namespace std;

int main()
{
    int n;
    double h = 0;
    cout << "Digite o valor de N: ";
    cin >> n;

    for(float i=1; i<=n; i++)
    {
        h = h + (1.0/i);
    }
    cout << "Valor de H: " << h;
}