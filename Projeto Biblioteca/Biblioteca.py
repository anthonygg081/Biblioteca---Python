import datetime

usuarios = {}

livros = {
    1: {"nome": "Dom Casmurro", "autor": "Machado de Assis", "situação": True},
    2: {"nome": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "situação": True},
    3: {"nome": "Cem Anos de Solidão", "autor": "Gabriel García Márquez)", "situação": True},
    4: {"nome": "Orgulho e Preconceito", "autor": "Jane Austen", "situação": True}
}

def cadastrar():
    print("\n--- Cadastro de Usuário ---")
    usuario = input("Digite o nome de Usuário: ")
    senha = input("Digite a senha: ")

    if usuario in usuarios:
        print('\nUsuário já cadastrado.')
        return
    else:
        usuarios[usuario] = {
            "senha" : senha,
            "livros_emprestados" : {}
## estrutra de usuarios:
## usuarios = {
##     "usuario1": { "senha": "123", "livros_emprestados": {livros} }
        }
    print("\nCadastro Realizado!")


def login():
    print("\n--- LOGIN ---")
    usuario = input("Digite o nome de Usuário: ")
    senha = input("Digite a senha: ")

    if usuario in usuarios and usuarios[usuario]["senha"] == senha:
        print("\nLogin Realizado!")
        menu_usuario(usuario)
    else:
        print("\nUsuário não encontrado.")


def listar_livros():
    print("\n--- Livros ---")
#   pega o id ,  o items() junta as informações da chave
    for codigo, livro in livros.items():
        # Se a "situação" do livro for verdadeira (disponível), armazena "Disponível". Se for falsa, armazena "Emprestado".
        status = "Disponível" if livro["situação"] else "Emprestado"
        print(f"{codigo} - {livro["nome"]} - {status}")


def pegar_livro(usuario):
    listar_livros()
    codigo = int(input("\nDigite o código do livro que deseja: "))

    if codigo in livros and livros[codigo]['situação']:
        livros[codigo]["situação"] = False
        data_emprestimo = datetime.date.today()

        usuarios[usuario]["livros_emprestados"][codigo] = data_emprestimo
        print("\nLivro emprestado!")
    else:
        print("\nLivro não encontrado ou indisponível.")


import datetime

def devolver_livro(usuario):
    emprestados = usuarios[usuario]["livros_emprestados"]
    VALOR_MULTA_DIA = 2 
    DIAS_LIMITE = 7      

    if not emprestados:
        print("\nVocê não possui livros emprestados.")
        return

    print("\n--- Seus Livros Emprestados ---")
    for codigo, data_emprestimo in emprestados.items():
        print(f"Código: {codigo} - Data do Empréstimo: {data_emprestimo}")

    try:
        codigo = int(input("\nDigite o código do livro: "))
        
        if codigo in emprestados:
            # Aqui 'emprestados[codigo]' já é a data diretamente
            data_do_emprestimo = emprestados[codigo] 
            data_devolucao = datetime.date.today()
            dias = (data_devolucao - data_do_emprestimo).days
            
            # ... resto do código de multa ...
            multa = 0
            if dias > DIAS_LIMITE:
                multa = (dias - DIAS_LIMITE) * VALOR_MULTA_DIA
            
            # Atualiza o status geral dos livros e remove do usuário
            livros[codigo]["situação"] = True
            del emprestados[codigo]

            print(f"\nSucesso! Livro devolvido.")
            print(f"Dias com o livro: {dias}")
            if multa > 0:
                print(f"Valor da multa: R${multa}")
        else:
            print("\nCódigo não encontrado na sua lista de empréstimos.")
            
    except ValueError:
        print("\nPor favor, digite um número válido para o código.")

def menu_principal():
    while True:
        print("\n=== BIBLIOTECA ===")
        print("1 - Cadastrar\n2 - Login\n3 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar()
        elif escolha == "2":
            login()
        elif escolha == "3":
            return
        else:
            print("opção inválida")

        
def menu_usuario(usuario):
    while True:
        print(f"\n--- Menu Usuário ({usuario}) ---")
        print("1 - Listar livros\n2 - Pegar livro\n3 - Devolver livro\n4 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            listar_livros()
        elif escolha == "2":
            pegar_livro(usuario)
        elif escolha == "3":
            devolver_livro(usuario)
        elif escolha == "4":
            return
        else:
            print("opção inválida")

menu_principal()