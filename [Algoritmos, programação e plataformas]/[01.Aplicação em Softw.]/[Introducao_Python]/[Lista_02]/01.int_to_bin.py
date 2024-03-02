#Faça um programa que leie o número em decimal e o transforme em binário e vice-versa


choice = input(f"\nVocê deseja transformar um número decimal ou binário?\n")

def dec_to_bin():

    return 0

def bin_to_dec():

    return 1

if choice == "bin":
    print(bin_to_dec())
elif choice == "dec":
    print(dec_to_bin())
else:
    print("Opção incorreta!")
    exit()

