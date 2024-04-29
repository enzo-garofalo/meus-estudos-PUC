# Faça um programa que leia se o valor é positivo, negativo ou nulo


num = float(input("\nDigite um número: "))

if num > 0:
    print(f"\tO seu número é positivo!")
elif num < 0:
    print(f"\tO seu número é negativo!")
else: 
    print(f"\tO seu número é nulo!")