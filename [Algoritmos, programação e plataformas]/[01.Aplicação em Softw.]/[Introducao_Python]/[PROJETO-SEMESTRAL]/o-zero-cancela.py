#  Construir um programa que calcule a soma de uma sequencia de números digitado pelo usuário, 
#  Quando o usuário digitar 0 vai cancelar o último digito, o usuário pode cancelar 3 vezes consecutivas
# O programa deve exibir soma total, números considerados e números desconsiderados
#  O programa vai parar quando num < 0 

print(f"\n\tBem vindo ao zero cancela.")

num  = 0
soma = 0
num_anterior = 0
conta_zero = 0

while num >= 0:
    num = float(input("Número: "))
    
    if num > 0:
        num_anterior = num
        soma += num_anterior

    
    elif num == 0:
        conta_zero += 1
        soma = soma - num_anterior
        


print(f"Soma total = {soma}")
