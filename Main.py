import json

def mostrar_menu():
    print("\n====== Gerenciador de Tarefas ======")
    print("1 - Adicionar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Marcar Tarefa como Concluída")
    print("4 - Remover Tarefa")
    print("5 - Sair")


class Tarefa:
    def __init__(self, id, titulo):
        self.id = id
        self.titulo = titulo
        self.concluida = False

    def marcar_concluida(self):
        self.concluida = True

    def __str__(self):
        status = "Concluída" if self.concluida else "Pendente"
        return f"ID: {self.id}, Título: {self.titulo}, Status: {status}"
            
class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
        self.proximo_id = 1
        self.carregar_tarefas()

    def adicionar_tarefa(self, titulo):
        tarefa = Tarefa(self.proximo_id, titulo)
        self.tarefas.append(tarefa)
        self.proximo_id += 1
        self.salvar_tarefas()

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
            return
        for tarefa in self.tarefas:
            print(tarefa)
    
    def remover_tarefa(self, id_tarefa):
        for tarefa in self.tarefas:
            if tarefa.id == id_tarefa:
                self.tarefas.remove(tarefa)
                self.salvar_tarefas()
                return
        print("Tarefa não encontrada.")

    def marcar_concluida(self, id_tarefa):
        for tarefa in self.tarefas:
            if tarefa.id == id_tarefa:
                tarefa.marcar_concluida()
                self.salvar_tarefas()
                return
        print("Tarefa não encontrada.")

    def salvar_tarefas(self):
        with open("tarefas.json", "w", encoding="utf-8") as f:
            json.dump(
                [t.__dict__ for t in self.tarefas],
                f,
                indent=4,
                ensure_ascii=False
            )

    def carregar_tarefas(self):
        try:
            with open("tarefas.json", "r", encoding="utf-8") as f:
                dados = json.load(f)
                for t in dados:
                    tarefa = Tarefa(t["id"], t["titulo"], t["concluida"])
                    self.tarefas.append(tarefa) 
                if self.tarefas:
                    self.proximo_id = max(t.id for t in self.tarefas) + 1
        except FileNotFoundError:
            pass
            
gerenciador = GerenciadorTarefas()

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Digite o título da tarefa: ")
        gerenciador.adicionar_tarefa(titulo)
        
    elif opcao == "2":
        
        gerenciador.listar_tarefas()

    elif opcao == "3":

        id_tarefa = int(input("Digite o ID da tarefa a ser marcada como concluída: "))
        gerenciador.marcar_concluida(id_tarefa)

    elif opcao == "4":

        id_tarefa = int(input("Digite o ID da tarefa a ser removida: "))
        gerenciador.remover_tarefa(id_tarefa)

    elif opcao == "5":

        print("\nSaindo do Gerenciador de Tarefas. Até logo!")
        break

    else:

        print("\nOpção inválida. Por favor, escolha uma opção válida.")