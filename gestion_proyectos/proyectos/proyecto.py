class Proyecto():

    def __init__(self, titulo_proyecto):
        self.titulo_proyecto = titulo_proyecto

    def __str__(self):
        return f"Proyecto principal: Título: {self.titulo_proyecto}"