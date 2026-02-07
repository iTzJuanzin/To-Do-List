import json

def mostrar_menu():
    print("\n====== Gerenciador de Tarefas ======")
    print("1 - Adicionar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Marcar Tarefa como Concluída")
    print("4 - Remover Tarefa")
    print("5 - Sair")

    tarefas = []

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            print("\nAdicionar Tarefa")

        elif opcao == "2":

            print("\nListar Tarefas")
            
        elif opcao == "3":

            print("\nMarcar Tarefa como Concluída")

        elif opcao == "4":

            print("\nRemover Tarefa")

        elif opcao == "5":

            print("\nSaindo do Gerenciador de Tarefas. Até logo!")
            break

        else:
            
            print("\nOpção inválida. Por favor, escolha uma opção válida.")
