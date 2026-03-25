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
        print('Usuário já cadastrado.')
        return
    else:
        usuarios[usuario] = {
            "senha" : senha,
            "livros_emprestados" : {}
        }
    print("Cadastro Realizado!")


def login():
    print("--- LOGIN ---")
    usuario = input("Digite o nome de Usuário: ")
    senha = input("Digite a senha: ")

    if usuario in usuarios and usuarios[usuario]["senha"] == senha:
        menu_usuario(usuario)
        print("Login Realizado!")
    else:
        print("Usuário não encontrado.")


def listar_livros():
    print("\n--- Seus Livros ---")
#   pega o id ,  o items() junta as informações da chave
    for codigo, livro in livros.items():
        # Se a "situação" do livro for verdadeira (disponível), armazena "Disponível". Se for falsa, armazena "Emprestado".
        status = "Disponível" if livro["situação"] else "Emprestado"
        print(f"{codigo} - {livro["nome"]} - {status}")


def pegar_livro(usuario):
    listar_livros()
    codigo = input("Digite o código do livro que deseja: ")

    if codigo in livros and livros[codigo]['situação'] == True:
        livros[codigo]["situação"] = False
        data_emprestimo = datetime.date.today()

        usuarios[usuario]["livros_emprestados"][codigo] = data_emprestimo
        print("Livro emprestado!")
    else:
        print("Livro não encontrado ou indisponível.")


def devolver_livro(usuario):
    emprestados = usuarios[usuario]["livros_emprestados"]
    VALOR_MULTA_DIA = 2  # R$ 2 por dia de atraso
    DIAS_LIMITE = 7      # 7 dias sem multa

    if emprestados:
      for codigo, livro in emprestados:
          print(f"{codigo} - {livro["nome"]} ")

          codigo = input("Digite o código do livro que deseja devolver: ")

          if codigo in emprestados:
              data_emprestimo = emprestados[codigo]
              data_devolucao = datetime.date.today()
              dias = (data_devolucao - data_emprestimo).days

              multa = 0
              if dias > DIAS_LIMITE:
                  multa = (dias - DIAS_LIMITE) * VALOR_MULTA_DIA

                  livros[codigo]["situação"] = True
                  del emprestados[codigo]

                  print("Livro devolvido.")
                  print(f"Dias com o livro: {dias}")
                  print(f"Valor a pagar R${multa}")

              else:
                  print("Você não possui esse livro.")



def menu_principal():
    while True:
        print("\n=== BIBLIOTECA ===")
        print("1 - Cadastrar\n2 - Login\n 3 - Sair")

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
        print("1 - Listar livros\n2 - Pegar livro\n 3 - Devolver livro\n 4 - Sair")

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