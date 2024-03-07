#Faça um programa que leie o número em decimal e o transforme em binário e vice-versa


choice = input(f"\nVocê deseja transformar um número inteiro ou binário?\n")

def int_to_bin():
    bin = []
    num = int(input(f"\nDigite o valor inteiro: "))
    
    while num >= 1:
        bin.append(num % 2)
        num = num // 2
    
    return bin

def bin_to_dec():

    return 1

if choice == "bin":
    print(bin_to_dec())
elif choice == "int":
    print(int_to_bin())
else:
    print("Opção incorreta!")
    exit()

