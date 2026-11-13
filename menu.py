import json

def carregar_produtos():
    arquivo = open("produtos.json", "r", encoding="utf-8")
    produtos = json.load(arquivo)
    arquivo.close()
    return produtos

def salvar_produtos(produtos):
    arquivo = open("produtos.json", "w", encoding="utf-8")
    json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()

produtos = carregar_produtos()

def mostrar_item(item):
    print(f"id: {item['id']} nome: {item['nome']} categoria: {item['categoria']} preço: {item['preco']} quantidade em estoque: {item['estoque']}")

def disponiveis():
    global produtos
    produtos = carregar_produtos()
    print("---> Mostrando produtos disponiveis <---")
    for x in produtos:
        mostrar_item(x)
    print("")

def valor():
    global produtos
    produtos = carregar_produtos()
    print("---> Pesquisando valor de algum produto <---")
    pesquisa = input("Qual o nome do produto: ")
    encontrou = False
    for x in produtos:
        if pesquisa.casefold() in x["nome"].casefold():
            print(f"Produto: {x['nome']} | Preço: {x['preco']}")
            encontrou = True
    if not encontrou:
        print("Produto não encontrado.")
    print("")

def pesquisar():
    global produtos
    produtos = carregar_produtos()
    print("---> Pesquisando produtos por categoria <---")
    pesquisa = input("Pesquisar por: (categoria) ")
    encontrou = False
    for x in produtos:
        if pesquisa.casefold() in x["categoria"].casefold():
            mostrar_item(x)
            encontrou = True
    if not encontrou:
        print("Nenhuma categoria encontrada.")
    print("")

def nome():
    global produtos
    produtos = carregar_produtos()
    print("---> Pesquisando produto por nome <---")
    pesquisa = input("Qual o nome do produto? ")
    encontrou = False
    for x in produtos:
        if pesquisa.casefold() in x["nome"].casefold():
            mostrar_item(x)
            encontrou = True
    if not encontrou:
        print("Produto não encontrado.")
    print("")

def adicionar():
    global produtos
    produtos = carregar_produtos()
    print("---> Adicionar novo produto <---")
    try:
        id = int(input("Digite o id do novo produto: "))
        nome_prod = input("Digite o nome do produto: ")
        categoria = input("Digite a categoria do produto: ")
        preco = float(input("Digite o preço do produto: "))
        estoque = int(input("Digite a quantidade do estoque do produto: "))

        novo_produto = {
            "id": id,
            "nome": nome_prod,
            "categoria": categoria,
            "preco": preco,
            "estoque": estoque
        }
        produtos.append(novo_produto)
        salvar_produtos(produtos)
        print("Novo produto criado e salvo com sucesso!")
    except ValueError:
        print("Erro nos valores digitados.")
    print("")

def remover():
    global produtos
    produtos = carregar_produtos()
    print("---> Removendo produto <---")
    try:
        id = int(input("Digite o id do produto que quer remover: "))
        removido = False
        for x in produtos:
            if x["id"] == id:
                produtos.remove(x)
                salvar_produtos(produtos)
                print("Produto Removido")
                removido = True
                break
        if not removido:
            print("ID não encontrado.")
    except ValueError:
        print("Digite um ID válido.")
    print("")

def mudarpreco():
    global produtos
    produtos = carregar_produtos()
    print("---> Mudando preço <---")
    pesquisa = input("Qual o nome do produto vc quer mudar o preço: ")
    try:
        novo_preco = float(input("Qual o novo preço: "))
        encontrado = False
        for x in produtos:
            if x["nome"].casefold() == pesquisa.casefold():
                x["preco"] = novo_preco
                salvar_produtos(produtos)
                print("Preço mudado")
                encontrado = True
                break
        if not encontrado:
            print("Produto não encontrado.")
    except ValueError:
        print("Preço inválido.")
    print("")

def mudarestoque():
    global produtos
    produtos = carregar_produtos()
    print("---> Mudando o estoque <---")
    pesquisa = input("Qual o nome do produto vc quer mudar o estoque: ")
    try:
        novo_estoque = int(input("Qual o novo estoque: "))
        encontrado = False
        for x in produtos:
            if x["nome"].casefold() == pesquisa.casefold():
                x["estoque"] = novo_estoque
                salvar_produtos(produtos)
                print("Estoque mudado")
                encontrado = True
                break
        if not encontrado:
            print("Produto não encontrado.")
    except ValueError:
        print("Estoque inválido.")
    print("")

while True:
    print("O que quer fazer: ")
    print("1 - Pesquisar produtos disponiveis")
    print("2 - Pesquisar valor de algum produto")
    print("3 - Pesquisar categoria")
    print("4 - Pesquisar um produto por nome")
    print("5 - Adicionar um novo produto")
    print("6 - Remover algum produto")
    print("7 - Mudar o preço de algum produto")
    print("8 - Mudar o estoque de algum produto")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        disponiveis()
    elif opcao == "2":
        valor()
    elif opcao == "3":
        pesquisar()
    elif opcao == "4":
        nome()
    elif opcao == "5":
        adicionar()
    elif opcao == "6":
        remover()
    elif opcao == "7":
        mudarpreco()
    elif opcao == "8":
        mudarestoque()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida, tente novamente!")