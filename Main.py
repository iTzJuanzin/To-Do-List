from manager import GerenciadorTarefas


def mostrar_menu():
    print("\n====== Gerenciador de Tarefas ======")
    print("1 - Adicionar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Marcar Tarefa como Concluída")
    print("4 - Remover Tarefa")
    print("5 - Sair")


def main():
    gerenciador = GerenciadorTarefas()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título: ")
            gerenciador.adicionar_tarefa(titulo)

        elif opcao == "2":
            gerenciador.listar_tarefas()

        elif opcao == "3":
            id_tarefa = int(input("ID da tarefa: "))
            gerenciador.marcar_concluida(id_tarefa)

        elif opcao == "4":
            id_tarefa = int(input("ID da tarefa: "))
            gerenciador.remover_tarefa(id_tarefa)

        elif opcao == "5":
            print("Até logo 👋")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
