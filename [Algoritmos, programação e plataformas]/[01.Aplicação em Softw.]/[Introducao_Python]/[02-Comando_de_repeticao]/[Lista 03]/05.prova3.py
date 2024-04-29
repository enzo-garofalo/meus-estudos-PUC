n = int(input("Número de mercadorias: "))
baixo = medio = alto = cod_mercadoria = compra = venda = lucro = soma = 0

for i in range(1,n+1):
  cod_mercadoria = int(input("\nCódigo: "))
  compra = float(input("Valor de compra: "))
  venda = float(input("Valor de Venda: "))

  soma += (venda-compra)
  lucro = ((venda-compra)*100)/compra

  if lucro <= 10:
    baixo += 1
  elif lucro <= 20:
    medio += 1
  else:
    alto += 1

print(f"\nQuantidade de mercadorias com")
print(f"  |Lucro Baixo: {baixo}")
print(f"  |Lucro medio: {medio}")
print(f"  |Lucro alto: {alto}") 
print(f"Soma total dos lucros: R${soma}") 