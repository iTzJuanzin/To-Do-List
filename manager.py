from models import Tarefa
from storage import salvar_tarefas, carregar_tarefas


class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = carregar_tarefas()
        self.proximo_id = self._gerar_proximo_id()

    def _gerar_proximo_id(self):
        if not self.tarefas:
            return 1
        return max(t.id for t in self.tarefas) + 1

    def adicionar_tarefa(self, titulo):
        tarefa = Tarefa(self.proximo_id, titulo)
        self.tarefas.append(tarefa)
        self.proximo_id += 1
        salvar_tarefas(self.tarefas)

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
                salvar_tarefas(self.tarefas)
                return
        print("Tarefa não encontrada.")

    def marcar_concluida(self, id_tarefa):
        for tarefa in self.tarefas:
            if tarefa.id == id_tarefa:
                tarefa.marcar_concluida()
                salvar_tarefas(self.tarefas)
                return
        print("Tarefa não encontrada.")
