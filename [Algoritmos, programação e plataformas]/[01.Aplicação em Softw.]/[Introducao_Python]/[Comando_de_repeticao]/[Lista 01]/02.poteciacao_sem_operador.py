# Escreva um programa que calcule x elevado a n. Considere que n é um
# # valor inteiro não negativo. PROIBIDO USAR QUALQUER FUNÇÃO MATEMATICA EXISTENTE no PYTHON

print(f"\tPotenciação sem operadores!")

base = int(input("Digite a base: "))
exp = int(input("Digite o expoente: "))
pot = 1

print(f"O Valor de {base} elevado a {exp} é ", end=' ')
while exp > 0:
    pot = pot * base
    exp -= 1 

print(f"{pot}")


# <VERSÃO DA DRa Lucia!> 
# exp = int(input("Digite o expoente: "))
# while exp < 0:
#     print(f"Valor negativo não permitido!")
#     print(f"Digite outro valor")
#     exp = int(input("Digite o expoente: "))

# base = float(input("Base = "))
# pot = 1
# print(f"{base}^{exp} = ", end=' ')
# while exp > 0:
#     pot = pot*base
#     exp -= 1
# print(f"{pot}")
