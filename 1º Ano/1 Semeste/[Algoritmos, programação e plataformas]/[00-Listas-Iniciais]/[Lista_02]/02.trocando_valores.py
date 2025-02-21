# Suponha que o valor de uma certa variável inteira A=5 e de uma 
# Variável B=13, como poderíamos trocar o valor dessas variáveis, 
# ou seja, A=13 e B=5?

print(f"\tTrocando valores!")
A = float(input("\nDigite o valor de A: "))
B = float(input("\Digite o valor de B: "))

aux = A
A = B
B = aux

print(f"\n\tValor de A: {A}")
print(f"\tValor de B: {B}")
