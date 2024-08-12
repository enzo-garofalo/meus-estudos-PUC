

#include <iostream>

int main()
{
	int senha = 12324;
	int tentativas = 3;
	int chute;

	while (tentativas > 0) 
	{
		printf("\nDigite a senha: ");
		std::cin >> chute;

		if (senha != chute) 
		{
			tentativas--;
			std::cout << "Acesso Negado";
		}
		else {
			return printf("Acesso Liberado");
		}
	}
}

