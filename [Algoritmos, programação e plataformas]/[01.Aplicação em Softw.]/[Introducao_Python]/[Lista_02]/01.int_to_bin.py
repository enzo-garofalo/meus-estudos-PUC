#Faça um programa que leie o número em decimal e o transforme em binário e vice-versa

print(f"\tConversor inteiro para binário ou vice-versa!")
choice = input(f"\nVocê deseja transformar um número inteiro ou binário?\n\nUse bin ou int: ")

def int_to_bin():
    bin = []
    num = int(input(f"\nDigite o valor inteiro: "))
    
    while num >= 1:
        bin.append(num % 2)
        num = num // 2
    bin.reverse()
    bin = ''.join(str(x) for x in bin)
    return bin

def bin_to_int():

    bin = input(f"\nDigite o valor binário: ")
    bin = list(bin)
    bin.reverse()
    num = 0

    for i in range(len(bin)):
        num = num + int(bin[i])*2**i

    return num

if choice == "bin":
    print(f"\n\tO valor em número binário é: {bin_to_int()}")
elif choice == "int":
    print(f"\n\tO valor em número inteiro é: {int_to_bin()}")
else:
    print("Opção incorreta!")
    exit()

