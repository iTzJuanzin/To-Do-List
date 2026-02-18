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