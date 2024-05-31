def mostrar_menu():
    menu = (
        "\nMenu:\n"
        "1. Adicionar aluno\n"
        "2. Listar todos os alunos\n"
        "3. Atualizar aluno\n"
        "4. Remover aluno\n"
        "5. Sair"
    )
    return menu

def adicionar_aluno(alunos):
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)
    return f"Aluno '{nome}' adicionado com sucesso."

def listar_alunos(alunos):
    if not alunos:
        return "Nenhum aluno cadastrado."
    else:
        lista = "Lista de alunos:\n"
        lista += "\n".join(f"{i+1}. {nome}" for i, nome in enumerate(alunos))
        return lista

def atualizar_aluno(alunos):
    nome_antigo = input("Digite o nome do aluno que deseja atualizar: ")
    if nome_antigo in alunos:
        novo_nome = input("Digite o novo nome do aluno: ")
        indice = alunos.index(nome_antigo)
        alunos[indice] = novo_nome
        return f"Aluno '{nome_antigo}' atualizado para '{novo_nome}'."
    else:
        return f"Aluno '{nome_antigo}' não encontrado."

def remover_aluno(alunos):
    nome = input("Digite o nome do aluno que deseja remover: ")
    if nome in alunos:
        alunos.remove(nome)
        return f"Aluno '{nome}' removido com sucesso."
    else:
        return f"Aluno '{nome}' não encontrado."

def main():
    alunos = []
    while True:
        menu = mostrar_menu()
        print(menu)
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            msg = adicionar_aluno(alunos)
            print(msg)
        elif opcao == '2':
            msg = listar_alunos(alunos)
            print(msg)
        elif opcao == '3':
            msg = atualizar_aluno(alunos)
            print(msg)
        elif opcao == '4':
            msg = remover_aluno(alunos)
            print(msg)
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()