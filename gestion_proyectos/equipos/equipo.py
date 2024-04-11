class Equipo():


    def __init__(self, sueldo, necesitan_supervision, nombre_equipo, nombres=[],):
        self.sueldo = sueldo
        self.necesitan_supervision = necesitan_supervision
        self.nombres = nombres
        self.nombre_equipo = nombre_equipo


    def __str__(self):
        nombres_string = ", ".join(self.nombres)
        string_resultado = f"El proyecto fua asignado al equipo de {self.nombre_equipo}, el cual está conformado por {len(self.nombres)} personas, sus nombres son {nombres_string}, en total cobrarán {self.sueldo} dólares por finalizar el proyecto y"

        return string_resultado + " necesitan supervisión\n" if self.necesitan_supervision else string_resultado + " no necesitan supervisión\n"
