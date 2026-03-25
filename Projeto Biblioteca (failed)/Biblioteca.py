biblioteca = [
 "Código Limpo", "O Programador Pragmático", "Algoritmos: Teoria e Prática",
    "Estruturas de Dados e Algoritmos em Python", "Padrões de Projeto",
    "Refatoração", "Arquitetura Limpa", "Entendendo Algoritmos",
    "Expressões Regulares", "Sistemas Operacionais Modernos",
    "Redes de Computadores", "Compiladores: Princípios, Técnicas e Ferramentas",
    "Introdução à Teoria da Computação", "Inteligência Artificial: Uma Abordagem Moderna",
    "O Mítico Homem-Mês", "Trabalho Eficaz com Código Legado",
    "Domain-Driven Design (DDD)", "Engenharia de Software",
    "Pense em Python", "Python Fluente"
]

#lista de livros alugados com seus alugantes
livros_alugados = []

#dicionario (dict)
usuarios = { 
  "Anthony" : {
    "senha":  "senha123"
   },

  "Hadassa" : {
    "senha": "senha123"
   }  
}

# iniciar sem usuário
usuario_logado = None

def login():
  print("\n---- Área de Login ---\n")
  situacao = input("Digite uma opção: \n0- Voltar ao Menu \n1- Fazer Login  \n2- Cadastrar ")
  
  if situacao == "0":
    print("Voltando ao menu...")
    return #para voltar ao menu

  elif situacao == "1":
   login_input = input("Digite seu login: ")
   senha_input = input("Digite sua senha: ") 

# Verificação de login

#se login existir em usuarios e a senha seja igual, logar usuário
  if login_input in usuarios and usuarios[login_input]["senha"] == senha_input:
     usuario_logado = login_input
     print("Login realizado!")
     print(f"\nOlá, {usuario_logado}!")
     return usuario_logado #  retornando o valor pro resto do codigo
  
  elif situacao == "2":
   print("\n---- Cadastro de Usuário ----\n")
   print("Digite 0 para voltar")
   login_novo = input("Login de Usuário: ")
   senha_novo = input("Senha do Usuário: ")

   if login_novo == "0":
      print("Voltando ao menu...")
      return 
  else:
#  usando update interno no dict   chave(login) = valor(senha)
      usuarios[login_novo] = {
          "senha" : senha_novo 
          }
      print("Usuário cadastrado com sucesso!\n")
      print("Faça Login. Voltando ao menu...")
      return
    
    

def pegar_livro():
  print("\n--- Área de Seleção ----\n")
  print("Digite 0 para voltar")
  livro_escolhido = input("Digite o nome do livro desejado:\n ")
  if livro_escolhido == "0":
     print("Voltando ao menu...")
     return
  else:
  #  index retorna o indice do livro escolhido
   indice_livro =  biblioteca.index(livro_escolhido)
  #  pop tira o livro escolhido e armazena numa variável

    # confirmação e consentimento de taxa 
   confirmacao = input(f"\nVocê escolheu o livro: {livro_escolhido}\nA taxa de aluguel é de R$5,00 e a data de devolução em até três dias, ficando sujeito à multa em casos de atrasos.\nDeseja prosseguir? (1- Sim  2- Não)")

   if confirmacao == "1":
#  criando um novo registro
      biblioteca.pop(indice_livro) 
      registro = {
                "Livro": livro_escolhido,
                "Id": usuario_logado
            }
      livros_alugados.append(registro)
      print("\nAluguel realizado!")
   else:
    print("Voltando ao menu...")
    return


def devolver_livro():
    print("\n---- Área de Devolução ----\n")
    print("Digite 0 para voltar")
    livro_devolvido = input("Qual livro deseja devolver?")
    dias_alugados = input(int(f"Você alugou o livro {livro_devolvido} há quantos dias?"))
    if dias_alugados > 3:
          dias_extra = dias_alugados - 3
          total = 9 + (0,3 * 5 * dias_extra)
          print("Você passou do prazo de devolução de três dias.\nMulta de atraso = R$9,00\nJuros por atraso = 30%/dia")
          print(f"Total a ser pago = R${total} ")
    print("\nLivro devolvido!")   
    else:
    print("\nLivro devolvido!")   


    if livro_devolvido == "0":
      print("Voltando ao menu...")
      return
    else:
      # para cada um na contagem dos livros alugados faça:
      for i in range(len(livros_alugados)):
        # se no indice, no campo livro no registro for o livro de devoluçao
        if livros_alugados[i]["Livro"] == livro_devolvido:
        # 1. Removemos o registro completo da lista de empréstimos
          registro_removido = livros_alugados.pop(i)  
        # 2. Pegamos apenas o nome do livro do registro e devolvemos à biblioteca
          biblioteca.append(registro_removido["Livro"])
          break # pra parar quando encontrar

        #cobrança de taxa
        
 

def exibir_meusLivros():
    print("\n---- Seus livros alugados ----\n")
    for registro in livros_alugados:
        if registro["Id"] == usuario_logado:
            print(f"📖{registro['Livro']}")
        else:
          print("Você não possui livros alugados.")

print("---- Bem vindo a Biblioteca! -----")
while True:
  print("\nEscolha uma opção:")
  print("1. Exibir lista de livros disponíveis")
  print("2. Exibir meus livros alugados")
  print("3. Pegar livro")
  print("4. Devolver livro")
  print("5. Fazer login ou se cadastrar")
  print("6. Sair\n")
  escolha = int(input())

  if escolha == 1:
    print("---- Biblioteca ----")
    for livro in biblioteca:
     print(f"\n• {livro}")
    print("---- ---------- ----")

  elif escolha == 2:
    if usuario_logado != None:
     exibir_meusLivros()
    else:
      print("Você precisa fazer Login primeiro")

  elif escolha == 3:
     if usuario_logado != None:
      pegar_livro()
     else:
      print("Você precisa fazer Login primeiro")

  elif escolha == 4:
    if usuario_logado != None:
     devolver_livro()
    else:
      print("Você precisa fazer Login primeiro")

  elif escolha == 5:
    #  atualizamos a variável global com o resultado da função
    usuario_logado = login()

  elif escolha == 6:
   break


