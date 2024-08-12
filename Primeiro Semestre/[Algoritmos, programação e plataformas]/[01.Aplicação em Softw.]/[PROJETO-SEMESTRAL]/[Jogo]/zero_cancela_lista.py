#  Construir um programa que calcule a soma de uma sequencia de números digitado pelo usuário, 
#  Quando o usuário digitar 0 vai cancelar o último digito, o usuário pode cancelar 3 vezes consecutivas
# O programa deve exibir soma total, números considerados e números desconsiderados
#  O programa vai parar quando num_atual < 0 

numeros = []
num = nums_considerados = nums_desconsiderados = 0

while num >= 0:
      # Solicita ao usuário um número e armazena na variável num_atual
      num = float(input("Número: "))

      # Verifica se o número digitado é maior que zero
      if num > 0:
            numeros.append(num)
            nums_considerados += 1
            zero_consecutivo = 1
      elif num == 0:
            if zero_consecutivo >= 4:
              print("Apenas 3 zeros consecutivos.")
            else:
              zero_consecutivo += 1
              nums_desconsiderados += 1
              nums_considerados -= 1    
              numeros.pop()

print(f"Soma = {sum(numeros)}")
print(f"Numeros considerados: {nums_considerados}")
print(f"Numeros desconsiderados: {nums_desconsiderados}")