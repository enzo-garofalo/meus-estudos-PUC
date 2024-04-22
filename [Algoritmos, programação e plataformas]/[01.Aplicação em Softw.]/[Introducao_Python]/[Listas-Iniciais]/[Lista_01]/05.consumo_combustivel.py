# Elabore um programa que dada uma distância percorrida (em quilômetro, bem como o total de combustível gasto (em litros),
# informe o consumo do veículo)
print("Vamos calcular o consumo do seu veículo!")

km = float(input("\n\tInforme a distância percorrida (km): "))
litros = float(input("\n\tInforme o combustível gasto (Litros): "))

print(f"\nO consumo do veículo {km/litros:.2f} km/l")
