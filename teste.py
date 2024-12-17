import mysql.connector

# Conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='10203040',
    database='cdd_db',
)

cursor = conexao.cursor()

def adicionar_livro():
    codigo = input("Digite o código do livro: ")
    descricao = input("Digite a descrição do livro: ")
    area = input("Digite a área do livro: ")
    
    # Inserir livro no banco de dados
    sql = "INSERT INTO cdd (codigo, descricao, area) VALUES (%s, %s, %s)"
    cursor.execute(sql, (codigo, descricao, area))
    conexao.commit()
    
    print(f'Livro com código "{codigo}" adicionado com sucesso!')

def editar_livro():
    id_livro = int(input("Digite o ID do livro que deseja editar: "))
    novo_codigo = input("Digite o novo código do livro: ")
    nova_descricao = input("Digite a nova descrição do livro: ")
    nova_area = input("Digite a nova área do livro: ")
    
    # Atualizar livro no banco de dados
    sql = "UPDATE cdd SET codigo = %s, descricao = %s, area = %s WHERE id = %s"
    cursor.execute(sql, (novo_codigo, nova_descricao, nova_area, id_livro))
    conexao.commit()
    
    if cursor.rowcount > 0:
        print(f'Livro com ID "{id_livro}" editado com sucesso!')
    else:
        print(f'Livro com ID "{id_livro}" não encontrado.')

def remover_livro():
    id_livro = int(input("Digite o ID do livro que deseja remover: "))
    
    # Remover livro do banco de dados
    sql = "DELETE FROM cdd WHERE id = %s"
    cursor.execute(sql, (id_livro,))
    conexao.commit()
    
    if cursor.rowcount > 0:
        print(f'Livro com ID "{id_livro}" removido com sucesso!')
    else:
        print(f'Livro com ID "{id_livro}" não encontrado.')

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar Livro")
        print("2. Editar Livro")
        print("3. Remover Livro")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_livro()
        elif opcao == '2':
            editar_livro()
        elif opcao == '3':
            remover_livro()
        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
menu()

# Fecha a conexão com o banco de dados ao final
cursor.close()
conexao.close()
