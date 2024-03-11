# Escreva um programa que calcule x elevado a n. Considere que n é um
# # valor inteiro não negativo. PROIBIDO USAR QUALQUER FUNÇÃO MATEMATICA EXISTENTE no PYTHON

print(f"\tPotenciação sem operadores!")

x = int(input("Digite o valor a ser elevado: "))
n = int(input("Digite a potencia: "))
resultado = 1
i = 1

while i <= n:
    resultado = resultado * x
    i += 1

print(f"O Valor de {x} elevado a {n} é {resultado}")

