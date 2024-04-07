print("\n\tBem vindo ao zero cancela.")

num_atual = 0
soma = 0
nums_considerados = 0
nums_desconsiderados = 0
num_anterior1 = 0
num_anterior2 = 0
num_anterior3 = 0
zero_consecutivo = 0

while True:
    entrada = input("Número: ")
    if entrada.isdigit() or (entrada[0] == '-' and entrada[1:].isdigit()):
        num_atual = float(entrada)
        if num_atual < 0:
            break
        elif num_atual > 0:
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
                elif zero_consecutivo == 1:
                    soma -= num_anterior2
                elif zero_consecutivo == 2:
                    soma -= num_anterior3
                zero_consecutivo += 1
    else:
        print("Por favor, insira um número válido.")

print(f"Soma = {soma}")
print(f"Números considerados: {nums_considerados}")
print(f"Números desconsiderados: {nums_desconsiderados}")
