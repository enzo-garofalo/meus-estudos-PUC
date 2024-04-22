# Faça um programa para receber um número inteiro 
# representando segundos e imprimir a quantidade 
# correspondente em horas, minutos e segundos

print(f"\tConversor de segundo!")
sec = int(input("\nDigite o valor em segundos: "))

print(f"Horas: {sec // 3600}")
sec = sec % 3600
print(f"Minutos: {sec // 60}")
sec = sec % 60
print(f"Segundos: {sec}")