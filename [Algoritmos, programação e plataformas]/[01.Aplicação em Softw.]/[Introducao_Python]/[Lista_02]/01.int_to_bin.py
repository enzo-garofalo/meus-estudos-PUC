#Faça um programa que leie o número em decimal e o transforme em binário e vice-versa

print(f"\tConversor inteiro para binário ou vice-versa!")
choice = input(f"\nVocê deseja transformar um número inteiro ou binário?\n\nUse bin ou int: ")

def int_to_bin():
    binary = []
    num = int(input(f"\nDigite o valor inteiro: "))
    
    # while num >= 1:
    #     bin.append(num % 2)
    #     num = num // 2
    # binary.reverse()
    # binary = ''.join(str(x) for x in binary)
    return bin(num)

def bin_to_int():

    bin = input(f"\nDigite o valor binário: ")
    # bin = list(bin)
    # bin.reverse()
    # num = 0

    # for i in range(len(bin)):
    #     num = num + int(bin[i])*2**i

    return int(bin, 2)

if choice == "bin" or "binario":
    print(f"\n\tO valor em número inteiro é: {bin_to_int()}")
elif choice == "int" or "inteiro":
    print(f"\n\tO valor em número binário é: {int_to_bin()}")
else:
    print("Opção incorreta!")
    exit()

