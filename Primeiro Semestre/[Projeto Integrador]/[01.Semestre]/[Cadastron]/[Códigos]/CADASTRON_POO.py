import os
from prettytable import PrettyTable

class Produto:
    def __init__(self, codigo, nome, descricao, custo_compra, custo_fixo, comissao, imposto, lucro):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.custo_compra = custo_compra
        self.custo_fixo = custo_fixo
        self.comissao = comissao
        self.imposto = imposto
        self.lucro = lucro

    def calcular_precos(self):
        self.preco_venda = (self.custo_compra) * (1 + ((self.custo_fixo + self.comissao + self.imposto + self.lucro) / 100))
        self.custos = self.preco_venda * ((self.custo_fixo + self.comissao + self.imposto) / 100)
        self.receita_bruta = self.preco_venda - self.custo_compra
        self.custo_fixo =  self.preco_venda*( self.custo_fixo/100)
        self.comissao_vendas_valor = (self.preco_venda*self.comissao)/100
        self.imposto_valor = (self.preco_venda*self.imposto)/100
        self.rentabilidade = (self.lucro*self.preco_venda)/100
        self.trans_porcem = 100/self.preco_venda
        
        if self.lucro > 20:
            self.margem_lucro = "Alto"
        elif self.lucro > 10:
            self.margem_lucro = "Médio"
        elif self.lucro > 0:
            self.margem_lucro = "Baixo"
        elif self.lucro == 0:
            self.margem_lucro = "Nulo"
        else:
            self.margem_lucro = "Prejuízo"

    def tabelas(self):
        table_precos = PrettyTable(["Descrição", "Valor", "%"])
        table_precos.add_row(["Preço venda", round(self.preco_venda, 2), "100"])
        table_precos.add_row(["Custo de aquisição", round(self.custo_compra, 2), round(self.custo_compra * self.trans_porcem, 2)])
        table_precos.add_row(["Receita bruta", round(self.receita_bruta, 2), round(self.receita_bruta * self.trans_porcem, 2)])
        table_precos.add_row(["Custo fixo", round(self.custo_fixo, 2), round(self.custo_fixo * self.trans_porcem, 2)])
        table_precos.add_row(["Comissão de vendas", round(self.comissao_vendas_valor, 2), round(self.comissao_vendas_valor * self.trans_porcem, 2)])
        table_precos.add_row(["Impostos", round(self.imposto_valor, 2),round(self.imposto_valor * self.trans_porcem, 2)])
        table_precos.add_row(["Outros custos", round(self.custos, 2), round(self.custos * self.trans_porcem, 2)])
        table_precos.add_row(["Rentabilidade", round(self.rentabilidade, 2), round(self.rentabilidade * self.trans_porcem, 2)])
        table_precos.add_row(["Margem de lucro", self.margem_lucro, self.lucro])
        print(table_precos)

def cadastrar_produto():
    os.system("cls")  
    print(f"\n\tCadastro de produto!")  
    codigo = int(input("\nCódigo do produto: "))
    nome = input("Nome do produto: ")
    descricao = input("Descrição: ")
    custo_compra = float(input("Custo de compra: R$ "))
    custo_fixo = float(input("Custo fixo/administrativo [%]: "))
    comissao = float(input("Comissão de vendas [%]: "))
    imposto = float(input("Imposto sobre a venda [%]: "))
    lucro = float(input("Margem de lucro [%]: "))

    produto = Produto(codigo, nome, descricao, custo_compra, custo_fixo, comissao, imposto, lucro)
    produto.calcular_precos()
    produto.tabelas()
    decisao()

def decisao():
    while True:
        escolha = input(f"\nVocê deseja retornar ao menu?\n[Sim/Não]: ").upper()
        if escolha == "SIM":
            os.system("cls")
            menu()
        elif escolha == "NÃO" or escolha == "NAO":
            print(f"\n\tAté mais!")
            exit()
        else:
            print(f"\n\tDigite um valor válido!")

def menu():
    escolha = int(input(f"\t     MENU\n\t| 1- Cadastrar |\n\t| 2- Listar    |\n\t| 3- Alterar   |\n\t| 4- Excluir   |\n\t| 5- Sair      |\n\nO que deseja fazer? "))
    if escolha == 1:
        cadastrar_produto()
    elif escolha == 5:
        print(f"Até mais!")
        exit()
    else:
        print(f"\tDigite uma opção válida")
        menu()

menu()