#include <iostream>
using namespace std;

int main()
{
    int num;
    bool isValid = false;
    while (isValid == false)
    {
        printf("Digite o numero: ");
        cin >> num;
        if(num <= 0)
        {
            printf("Digite um inteiro positivo!!\n");
        }else{
            isValid = true;
        }
    }
    
    for(int i=num-1; i > 1; i--)
    {
        if(num%i == 0)
        {
            cout << num << " Nao eh primo";
            return 0;
        }
    }
    cout << num << " eh primo";
    return 0;
}