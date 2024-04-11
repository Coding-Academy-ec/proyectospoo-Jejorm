from gestion_proyectos.proyectos.proyecto import Proyecto

class Tarea(Proyecto):

    def __init__(self, descripcion_tarea, fecha_limite):
        self.descripcion_tarea = descripcion_tarea
        self.fecha_limite = fecha_limite

    def __str__(self):
        return f"Tarea con descripción: \n\t{self.descripcion_tarea} y fecha límite: {self.fecha_limite}"
