# Elabore um programa que faça a simulação de um caixa de uma loja.
# O usuário deverá digitar o Valor da Compra, o Valor Pago pelo cliente.
# O programa irá retornar o valor do troco, as cédulas que fazem parte do troco e a quantidade de cada cédula.;
# Para este programa considere as cédulas de R$20, R$10, R$5 e R$1 real
# Considere a possibilidade de não haver troco

print("\n\tSistema de Caixa!")

compra = int(input("\nInsira o valor da compra: R$ "))
pgmto = int(input("Pagamento: R$ "))

troco = pgmto-compra

if troco == 0:
    print("Não há necessidade de troco!")

print(f"\nTroco: {troco:.2f}")

cinquenta = int(troco/50)
troco = troco - (cinquenta*50)

vinte = int(troco/20)
troco = troco - (vinte*20)

dez = int(troco/10)
troco = troco - (dez*10)

cinco = int(troco/5)
troco = troco - (cinco*5)

um = int(troco)

print("Em:\n")
print(f"50,00: {cinquenta} cédulas.")
print(f"20,00: {vinte} cédulas.")
print(f"10,00: {dez} cédulas.")
print(f"5,00: {cinco} cédulas.")
print(f"1,00: {um} cédulas.")