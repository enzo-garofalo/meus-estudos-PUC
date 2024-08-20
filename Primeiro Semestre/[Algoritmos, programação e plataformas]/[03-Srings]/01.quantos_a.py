
while True:
    cont = 0
    frase = str(input("Digite uma frase: "))
    if len(frase) > 20:
        print("Digite uma frase com apenas 20 caracteres!")
        continue
    else:
        for a in range(len(frase)):
            if frase[a] == "a" or frase[a] == "A":
                cont += 1
    print(f"Número de as = {cont}")
    break
            