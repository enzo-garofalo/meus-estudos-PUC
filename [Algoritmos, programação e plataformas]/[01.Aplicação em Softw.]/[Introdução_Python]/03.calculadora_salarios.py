# Leia o salário mensal atual de um funcionário e o percentual de reajuste 
# determine o valor do novo salário

print(f"\tCalculadora de reajustes!")
 
atual = float(input("\nDigite o salário atual: "))
percentual = float(input("\nDigite o percentual de reajuste: "))

print(f"\tNovo salário: {atual+(atual*percentual/100)}")