# Um funcionário irá receber um aumento de acordo com o seu 
# plano de trabalho, de acordo com a tabela abaixo: 
#         PLANO           AUMENTO
#         1               10%
#         2               15%
#         3               20%
# Faça um programa que leia o plano de trabalho e o salário atual de 
# um funcionário e calcula e imprime o seu novo salário. 

print(f"\n\tPlanos de aumento")

plano = int(input("\nDigite o seu plano de aumento: "))
salario = float(input("Digite o salário base: "))

if plano == 1:
    print(f"\nO novo salário reajustado é de {salario+(salario*0.10)}")
elif plano == 2:
    print(f"\nO novo salário reajustado é de {salario+(salario*0.15)}")
elif plano == 3:
    print(f"\nO novo salário reajustado é de {salario+(salario*0.20)}")
else:
    print(f"\tSeleção do plano incorreta!")

    