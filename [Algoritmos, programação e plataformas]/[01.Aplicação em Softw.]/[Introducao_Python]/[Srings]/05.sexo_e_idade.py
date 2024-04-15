# Elabore umprograma que leia nome, sexo e idade de um usuário. Se sexo for feminino e idade menor que 25,
# imprime o nome da pessoa e a palavra “ACEITA”, caso contrário imprimir “NÃO ACEITA”.

print(f"\n\tAceito ou não!")
while True:
    nome = str(input("Digite o nome: "))
    sexo = str(input("Digite o sexo\n[M/F]:"))
    idade = int(input("Digite a idade:"))

    if sexo == "F" and idade < 25:
        print(f"{nome} Aceita!")
        break
    else:
        print(f"{nome} Não Aceito!")
        break
