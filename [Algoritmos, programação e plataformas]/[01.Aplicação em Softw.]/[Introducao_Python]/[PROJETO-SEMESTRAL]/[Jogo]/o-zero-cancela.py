#  Construir um programa que calcule a soma de uma sequencia de números digitado pelo usuário, 
#  Quando o usuário digitar 0 vai cancelar o último digito, o usuário pode cancelar 3 vezes consecutivas
# O programa deve exibir soma total, números considerados e números desconsiderados
#  O programa vai parar quando num_atual < 0 

print(f"\n\tBem vindo ao zero cancela.")

num_atual = soma = num_anterior1 = num_anterior2 = num_anterior3 = nums_considerados = nums_desconsiderados = 0

while num_atual >= 0:

    num_atual = float(input("Número: "))
    
    if num_atual > 0:
        
        soma += num_atual
        nums_considerados += 1
        
        num_anterior3 = num_anterior2
        num_anterior2 = num_anterior1
        num_anterior1 = num_atual

        zero_consecutivo = 0
    
    elif num_atual == 0:
        if zero_consecutivo == 3:
            print("Apenas 3 zeros consecutivos.")
        else:
            nums_desconsiderados += 1
            nums_considerados -= 1
            
            if zero_consecutivo == 0:
                soma -= num_anterior1
                zero_consecutivo += 1
            
            elif zero_consecutivo == 1:
                soma -= num_anterior2
                zero_consecutivo += 1            

            elif zero_consecutivo == 2:
                soma -= num_anterior3
                zero_consecutivo += 1
                num_anterior1 = num_anterior2 = num_anterior3 = 0


if nums_considerados <=  0:
    nums_considerados = 0
    soma = 0

print(f"Soma = {soma}")
print(f"Numeros considerados: {nums_considerados}")
print(f"Numeros desconsiderados: {nums_desconsiderados}")