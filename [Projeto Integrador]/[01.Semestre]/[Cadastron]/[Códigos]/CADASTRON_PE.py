import os
from prettytable import PrettyTable


# Definição da função para cadastrar um novo produto
def cadastrar_produto():
    # Limpa a tela do console (apenas Windows)
    os.system("cls")  
    table_produto = PrettyTable()

    # Mensagem de cabeçalho para o cadastro
    print(f"\n\tCadastro de produto!")  
    
    # Solicita e armazena os dados do produto inseridos pelo usuário
    global cod_prod
    cod_prod = int(input("\nCódigo do produto: "))
    table_produto.add_column(f"Código do Produto",[cod_prod])

    global nome_prod
    nome_prod = input("Nome do produto: ")
    table_produto.add_column(f"Nome",[nome_prod]) 

    global desc_prod
    desc_prod = input("Descrição: ")
    table_produto.add_column(f"Descrição",[desc_prod]) 

    global custo_prod
    custo_prod = float(input("Custo de compra: R$ "))
    # table_produto.add_column(f"Custo de Compra",[custo_prod]) sem uso por enquanto 09.04

    global custo_fixo_prod
    custo_fixo_prod = float(input("Custo fixo/administrativo [%]: "))
    # table_produto.add_column(f"Custo Fixo/Administrativo",[custo_fixo_prod]) sem uso por enquanto 09.04

    global comissao_vendas
    comissao_vendas = float(input("Comissão de vendas [%]: "))
    # table_produto.add_column(f"Comissão de vendas",[comissao_vendas]) sem uso por enquanto 09.04

    global imposto_prod
    imposto_prod = float(input("Imposto sobre a venda [%]: "))
    # table_produto.add_column(f"Imposto sobre a venda",[imposto_prod]) sem uso por enquanto 09.04

    global lucro_prod
    lucro_prod = float(input("Margem de lucro [%]: "))
    # table_produto.add_column(f"Margem de Lucro",[lucro_prod]) sem uso por enquanto 09.04

    # Retorna os dados do produto
    print(f"\n{table_produto}")

    # Chama a função cálculo do preço de venda e margem de lucro
    calculo_precos()
    
# Definição da função para calcular o preço de venda, custos e rentabilidade do produto
def calculo_precos():

    table_precos = PrettyTable(["Descrição", "Valor", "%"])

    # Cálculo do preço de venda
    preco_venda = (custo_prod) * (1 + ((custo_fixo_prod + comissao_vendas + imposto_prod + lucro_prod) / 100))
    
    # Cálculo dos custos
    custos = preco_venda * ((custo_fixo_prod + comissao_vendas + imposto_prod) / 100)

    # Calculo Receita bruta
    receita_bruta = preco_venda-custo_prod

    # Calculo Custo Fixo
    custo_fixo = preco_venda*(custo_fixo_prod/100)

    # Calculo Comissão de vendas
    comissao_vendas_valor = (preco_venda*comissao_vendas)/100

    # Calculo impostos
    imposto_valor = (preco_venda*imposto_prod)/100

    # Calculo Rentabilidade
    rentabilidade = (lucro_prod*preco_venda)/100

    trans_porcem = 100/preco_venda

    # Verifica a margem de margem_lucro e exibe uma mensagem correspondente
    if lucro_prod > 20:
        margem_lucro = "Alto"
    elif lucro_prod > 10:
        margem_lucro = "Médio"
    elif lucro_prod > 0:
        margem_lucro = "Baixo"
    elif lucro_prod == 0:
        margem_lucro = "Nulo"
    else:
        margem_lucro = "Prejuízo"




    table_precos.add_row(["Preço venda", round(preco_venda, 2), "100"])
    table_precos.add_row(["Custo de aquisição", round(custo_prod, 2), round(custo_prod * trans_porcem, 2)])
    table_precos.add_row(["Receita bruta", round(receita_bruta, 2), round(receita_bruta * trans_porcem, 2)])
    table_precos.add_row(["Custo fixo", round(custo_fixo, 2), round(custo_fixo * trans_porcem, 2)])
    table_precos.add_row(["Comissão de vendas", round(comissao_vendas_valor, 2), round(comissao_vendas_valor * trans_porcem, 2)])
    table_precos.add_row(["Impostos", round(imposto_valor, 2),round(imposto_valor * trans_porcem, 2)])
    table_precos.add_row(["Outros custos", round(custos, 2), round(custos * trans_porcem, 2)])
    table_precos.add_row(["Rentabilidade", round(rentabilidade, 2), round(rentabilidade * trans_porcem, 2)])
    table_precos.add_row(["Margem de lucro", margem_lucro, lucro_prod])

    print(f"\n{table_precos}")
    decisao()

def decisao():
        # Pergunta próximo passo ao usuário
    while True:
        escolha = input(f"\nVocê deseja retornar ao menu?\n[Sim/Não]: ")
        escolha = escolha.upper()
        if escolha == "SIM":
            os.system("cls")
            menu()
        elif escolha == "NÃO" or escolha == "NAO":
            print(f"\n\tAté mais!")
            exit()
        else:
            print(f"\n\tDigite um valor válido!")
            continue

# Função principal
def menu():
    # Exibe o menu e solicita a escolha do usuário
    escolha = int(input(f"\t     MENU\n\t| 1- Cadastrar |\n\t| 2- Listar    |\n\t| 3- Alterar   |\n\t| 4- Excluir   |\n\t| 5- Sair      |\n\nO que deseja fazer? "))
    
    # Verifica a escolha do usuário
    match escolha:
        # Caso a escolha seja 1 (Cadastrar)
        case 1:
            cadastrar_produto()  # Chama a função para cadastrar um produto

        # Caso a escolha seja 2 (Listar)
        # case 2:
            # consultar_dados()  

        # Caso a escolha seja 3 (Alterar)
        # case 3:
            # alterar_dados()  

        # Caso a escolha seja 4 (Excluir)
        # case 4:
            # excluir_dados()  
            
        # Caso a escolha seja 5 (Sair)
        case 5:
            print(f"Até mais!")  
            exit()  # Encerra o programa
            
        # Caso a escolha não seja válida
        case default:
            os.system("cls")
            print(f"\tDigite uma opção válida")  
            menu()  # Chama novamente a função principal para que o usuário faça uma nova escolha

# Chamada da função principal
menu()