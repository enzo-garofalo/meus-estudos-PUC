# Elabore um programa que leia um nº e o transforme
# em impar com a adição de 1 

print("Impar ou par!")

num = int(input(f"\nDigite um número: "))

if num % 2 == 0:
    print(f"\nSeu numero foi transformado em impar: {num+1}! ")
else:
    print(F"\nSeu número é impar: {num}")