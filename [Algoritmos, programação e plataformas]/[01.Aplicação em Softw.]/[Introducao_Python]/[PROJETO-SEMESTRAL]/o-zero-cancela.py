#  Construir um programa que calcule a soma de uma sequencia de números digitado pelo usuário, 
#  Quando o usuário digitar 0 vai cancelar o último digito, o usuário pode cancelar 3 vezes consecutivas
# O programa deve exibir soma total, números considerados e números desconsiderados
#  O programa vai parar quando num < 0 

print(f"\n\tBem vindo ao zero cancela.")

num = soma = num_anterior1 = num_anterior2 = num_anterior3 = 0
nums_considerados = nums_desconsiderados = 0
qtd_num = qtd_zero = 0

while num >= 0:
    num = float(input("Número: "))
    
    if num > 0:
        nums_considerados += 1
        soma += num
        conta_zero = 0
        
        num_anterior3 = num_anterior2
        num_anterior2 = num_anterior1
        num_anterior1 = num
        continue
    
    elif num == 0:
        if conta_zero == 3:
            print("Apenas 3 zeros consecutivos.")
            continue
        elif conta_zero == 0:
            soma -= num_anterior1
            conta_zero += 1

        elif conta_zero == 1:
            soma -= num_anterior2
            conta_zero += 1

        elif conta_zero == 2:
            soma -= num_anterior3
            num_anterior1 = num_anterior2 = num_anterior3 = 0
            conta_zero += 1
        
        nums_desconsiderados += 1
        nums_considerados -= 1
        continue


if nums_desconsiderados >= nums_considerados:
    soma = 0
    print("Soma = ", soma)
else:
    print("Soma = ", soma)       
    
    