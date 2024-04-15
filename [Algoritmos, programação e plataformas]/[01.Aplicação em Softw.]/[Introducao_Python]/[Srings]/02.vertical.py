# Faça um programa que solicite o nome do usuário e
# imprima-o na vertical.

nome = str(input("Digite seu nome: "))

print("Nome na Vertical: ")
for letra in range(len(nome)):
    print(f"\t{nome[letra]}")