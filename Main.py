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
    salvar_tarefas(tarefas)
    print(f"Tarefa '{titulo}' adicionada com sucesso.")


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

def marcar_concluida(tarefas):

    try:
        id_concluir = int(input("Digite o ID da tarefa a ser marcada como concluída: "))
    except ValueError:
        print("ID inválido. Por favor, insira um número.")
        return
    
    for tarefa in tarefas:
        if tarefa["id"] == id_concluir:
            tarefa["concluida"] = True
            print(f"Tarefa '{tarefa['titulo']}' marcada como concluída.")
            return
    
    print("Tarefa não encontrada.")

def salvar_tarefas(tarefas):
    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)

def carregar_tarefas():
    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

tarefas = carregar_tarefas()

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        adicionar_tarefa(tarefas)
        
    elif opcao == "2":
        
        listar_tarefas(tarefas)

    elif opcao == "3":

        marcar_concluida(tarefas)

    elif opcao == "4":

        remover_tarefa(tarefas)

    elif opcao == "5":

        print("\nSaindo do Gerenciador de Tarefas. Até logo!")
        break

    else:

        print("\nOpção inválida. Por favor, escolha uma opção válida.")