# Elabore um programa para determinar se é um quadrado ou retângulo.

print(f"\tDeterminação de quadrilátero!")

h = float(input(f"\nDigite a altura: "))
larg = float(input(f"Digite a largura: "))

if h == larg:
    print(f"\n\tO seu quadrilátero é um qudrado!")
else:
    print(f"\n\tO seu quadrilátero é um retângulo!")