
frase = str(input("Digite uma frase: "))
frase = frase.upper()

print("Frase sem vogal: ", end=" ")

for letras in range(len(frase)):
    if frase[letras] == "A" or frase[letras] == "E" or frase[letras] == "I" or frase[letras] == "O" or frase[letras] == "U":
       print("*", end="")
    else:
        print(frase[letras], end="")
