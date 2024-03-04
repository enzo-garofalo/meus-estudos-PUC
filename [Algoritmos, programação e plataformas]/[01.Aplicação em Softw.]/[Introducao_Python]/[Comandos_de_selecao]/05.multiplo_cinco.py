# Crie um programa que diga se o valor é múltiplo de 5

print(f"\tMultiplo de 5!")

num = int(input(f"\nDigite o valor: "))

if num % 5 == 0:
    print(f"\tO seu número é multiplo de 5!")
else:
    print(f"\tSeu número não é multiplo de 5!")