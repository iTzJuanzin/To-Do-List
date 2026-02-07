import json

def mostrar_menu():
    print("\n====== Gerenciador de Tarefas ======")
    print("1 - Adicionar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Marcar Tarefa como Concluída")
    print("4 - Remover Tarefa")
    print("5 - Sair")

def adicionar_tarefa(tarefas):

    titulo = input("Digite o título da tarefa: ").strip()

    tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo, 
        "concluida": False
    }

    tarefas.append(tarefa)


def listar_tarefas(tarefas):

    print("\n" + "-" * 30)


    if not tarefas: 
        print("\nNenhuma tarefa cadastrada.")
    else:
        print("\nLista de Tarefas:")
        for tarefa in tarefas:

            status = "Concluída" if tarefa["concluida"] else "Pendente"

            print(f"ID: {tarefa['id']}, Título: {tarefa['titulo']}, Status: {status}")

    print("-" * 30)


def remover_tarefa(tarefas):

    try:
        id_remover = int(input("Digite o ID da tarefa a ser removida: "))
    except ValueError:
        print("ID inválido. Por favor, insira um número.")
        return  

    for tarefa in tarefas:
        if tarefa["id"] == id_remover:
            tarefas.remove(tarefa)
            print(f"Tarefa '{tarefa['titulo']}' removida com sucesso.")
    
        for i, t in enumerate(tarefas, start=1):
                t["id"] = i
            
        return

    print("Tarefa não encontrada.")

    
    tarefas = []

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            adicionar_tarefa(tarefas)
            
        elif opcao == "2":
            if not tarefas: 
                print("\nNenhuma tarefa cadastrada.")
            else:
                print("\nLista de Tarefas:")
                for tarefa in tarefas:

                    status = "Concluída" if tarefa["concluida"] else "Pendente"

                    print(f"ID: {tarefa['id']}, Título: {tarefa['titulo']}, Status: {status}")
            
            
        elif opcao == "3":

            print("\nMarcar Tarefa como Concluída")

        elif opcao == "4":

            print("\nRemover Tarefa")

        elif opcao == "5":

            print("\nSaindo do Gerenciador de Tarefas. Até logo!")
            break

        else:

            print("\nOpção inválida. Por favor, escolha uma opção válida.")
