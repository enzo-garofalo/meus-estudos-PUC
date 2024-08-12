#include <iostream>

int fatorial(int num) {
    if (num == 1 || num == 0) {
        return 1;
    }
    return num * fatorial(num - 1);
}

int main()
{
    int num;
    while (num >= 0) {
        printf("\nDigite o numero: ");
        std::cin >> num;
        std::cout << "Fatorial de " << num << ": " << fatorial(num);
    }
}

