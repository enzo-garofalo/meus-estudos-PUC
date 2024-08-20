# Fazer um programa que calcule o valor de N! 
# (fatorial de N), sendo que o valor inteiro de N deve ser lido. 
# Lembrando  que:
# • N! = 1 x 2 x 3 x .... x (N - 1) x N;
# •0! = 1, por definição

print(f"\tFATORIAL!")

n = int(input("Digite o valor que deseja fatorar: "))
resultado = 1
i = 2

if n != 0:
    while i <= n:
        resultado *=  i
        i += 1
    print(f"\tO valor de {n}! é {resultado}")    
else:
    print(f"\tO valor de {n}! = 1")


