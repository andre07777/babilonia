from models import Autor, Categoria, Livro, db  

def criar_banco():
    try:
        db.connect()
        db.create_tables([Autor, Categoria, Livro], safe=True)
        print("Banco de dados e tabelas criados com sucesso!")
    except Exception as e:
        print(f"Erro ao criar banco de dados: {e}")
    finally:
        db.close()

def menu():
    while True:
        print("\nBem-vindo ao Sistema de Biblioteca!")
        print("Escolha uma opção:")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Atualizar Livro")
        print("4. Remover Livro")
        print("5. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            adicionar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            atualizar_livro()
        elif opcao == "4":
            remover_livro()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

def adicionar_livro():
    print("Adicionar Livro")
    titulo = input("Título do livro: ")
    autor_nome = input("Nome do autor: ")
    categoria_nome = input("Nome da categoria: ")
    ano = int(input("Ano de publicação: "))

    autor, created = Autor.get_or_create(nome=autor_nome)
    categoria, created = Categoria.get_or_create(nome=categoria_nome)

    Livro.create(titulo=titulo, autor=autor,
                 categoria=categoria, ano_publicacao=ano)
    print(f"Livro '{titulo}' adicionado com sucesso!")

def listar_livros():
    livros = Livro.select()
    for livro in livros:
        print(
            f"{livro.titulo} - {livro.autor.nome} - {livro.categoria.nome} - {livro.ano_publicacao}")

def atualizar_livro():
    listar_livros()
    id_livro = int(input("Digite o ID do livro a ser atualizado: "))
    livro = Livro.get_by_id(id_livro)

    novo_titulo = input(
        f"Novo título (deixe em branco para manter '{livro.titulo}'): ")
    if novo_titulo:
        livro.titulo = novo_titulo

    novo_ano = input(f"Novo ano de publicação (deixe em branco para manter '{
                     livro.ano_publicacao}'): ")
    if novo_ano:
        livro.ano_publicacao = int(novo_ano)

    livro.save()
    print(f"Livro '{livro.titulo}' atualizado com sucesso!")

def remover_livro():
    listar_livros()
    id_livro = int(input("Digite o ID do livro a ser removido: "))
    livro = Livro.get_by_id(id_livro)
    livro.delete_instance()
    print(f"Livro '{livro.titulo}' removido com sucesso!")

if __name__ == "__main__":
    criar_banco()  
    menu()
