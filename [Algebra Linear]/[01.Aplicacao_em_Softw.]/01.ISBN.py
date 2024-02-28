# Embora tenha passado por atualização recente, a maioria dos livros tem um código de 10 dígitos denominado 
# ISBN (International Standard Book Number). 
    # 0 último dígito é o dígito de verificação do ISBN e é calculado utilizando-se produto escalar.  
    # Os nove primeiros dígitos deste número estão divididos em três grupos: 
    # i - o primeiro  grupo representa o país ou grupo de países no qual originou o livro, 
    # ii - o segundo identifica a editora que o publicou 
    # iii - o terceiro identifica o título do próprio livro.
    # iv -O décimo e último dígito, denominado dígito de verificação, é calculado a partir dos nove primeiros e é utilizado para garantir que não há erro de digitação nos nove primeiros, 
# Para explicar como isto é feito, considere os nove primeiros dígitos do ISBN como um vetor b de ℝ9 e seja a o 
# vetor  (1, 2, 3, 4, 5, 6, 7, 8, 9) . Então o dígito de verificação c é calculado pelo seguinte processo:  
# 1. Calcule o produto escalar a · b.  
# 2. Divida a · b por 11, produzindo um resto c que é um inteiro entre 0 e 10, inclusive. O dígito de verificação é 
# tomado como sendo c, com a ressalva de trocar 10 por X para evitar mais um dígito. 

print("\tInternational Standard Book Number!")

cod = input("\nDigite o código do livro: ")
cod = list(cod)
vetor_resultante = []

if len(cod) != 10:
       print(f"\n\tO código está incorreto ou incompleto!")
       exit()
else:
    for i in range(len(cod)):

        if i == 9:
                vetor_resultante.append(0)
                cod_livro = int(cod[i])
        else:
                digito = int(cod[i])*(i+1)
                vetor_resultante.append(digito)

digito_esperado = sum(vetor_resultante) % 11

print(f"\nDigito de verificação: {cod_livro}")
print(f"Digito esperado: {digito_esperado}")

if digito_esperado == cod_livro:
       print(f"\n\tO livro é legítimo!")
else:
       print(f"\n\tO livro não está com o código incorreto!")
