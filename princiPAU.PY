from modelos import Produto, listar_produtos

def menu():
    print("""
    -------------------------
          MENU PRODUTOS
    -------------------------
    0 - SAIR
    1 - CADASTRAR
    2 - LISTAR PRODUTOS
    -------------------------
    """)
def cadastrar():
    nome = input("Qual o nome do produto: ")
    preco = float(input("Qual o preço: R$ "))
    categoria = input("Qual a categoria: ")

    produto = Produto(nome, preco, categoria)
    produto.salvar()

def mostrar():
    for produto in listar_produtos():
        produto.mostrazar()
        
while True:
    menu()
    opçao = input("Escolha uma opção: ")
    if opçao == "0":
        break
    elif opçao == "1": cadastrar()
    elif opçao == "2": mostrar()
    else: print("Opção inválida.")