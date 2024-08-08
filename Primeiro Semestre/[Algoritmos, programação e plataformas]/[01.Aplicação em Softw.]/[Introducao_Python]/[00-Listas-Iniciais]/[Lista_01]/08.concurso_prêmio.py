# Uma certa importância será dividida entre três ganhadores de
# um concurso. Sendo que da quantia total:
# • O primeiro ganhador recebera 46%;
# • O segundo recebera 32%;
# • O terceiro recebera o restante;
# Elabore um programa que dado o valor do concurso em reais ele,
# calcule e imprima a quantia ganha por cada um dos ganhadores

print(f"\n\tResultado do concurso!")

premio = float(input("Insira o valor do prêmio em reais: "))

print(f"\nO primeiro ganhador receberá: {premio*42/100:.2f}")
print(f"\nO segundo ganhador receberá: {premio*32/100:.2f}")
print(f"\nO terceiro ganhador receberá: {premio*26/100:.2f}")