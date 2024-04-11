from gestion_proyectos.equipos.equipo import Equipo
from gestion_proyectos.proyectos.proyecto import Proyecto
from gestion_proyectos.tareas.tarea import Tarea


def main():
    nombres_equpo_1 = ["Juan", "Karla", "Rebeca", "Francisco"]
    proyecto_1 = Proyecto("Crear sistema de ventas para un e-commerce.\n")
    tarea_1 = Tarea("Organizar los grupos de acuerdo a su experiencia", "2024-05-12")
    tarea_2 = Tarea("Dividir las caracteristícas a cada miembro del equipo", "2024-05-25\n")
    equipo_1 = Equipo(1500, False, 'e-commerce specialist', nombres_equpo_1)

    nombres_equpo_2 = ["Tatiana", "Pedro", "Eduardo", "Sofía"]
    proyecto_2 = Proyecto("Rediseñar el sistema de compras de un supermercado\n")
    tarea_3 = Tarea("Realizar un prototipo inicial del diseño final", "2024,06-07")
    tarea_4 = Tarea("Implementar el diseño y las características por partes", "2024-06-28\n")
    equipo_2 = Equipo(1250, True, 'sales engineer team', nombres_equpo_2)

    nombres_equpo_3 = ["Verónica", "Mateo", "Anthony", "Raquel"]
    proyecto_3 = Proyecto("Programar un sistema de videovigilancia para un almacén de ventas al por-mayor de primera necesidad\n")
    tarea_5 = Tarea("Comprar los suministros necesarios para el proyecto", "2024-07-09")
    tarea_6 = Tarea("Verificar la instalación correcta de los suministros", "2024-07-14\n")
    equipo_3 = Equipo(1700, False, 'security field', nombres_equpo_3)

    print("Proyectos a realizar:\n")
    print(proyecto_1)
    print(tarea_1)
    print(tarea_2)
    print(equipo_1)

    print("- - - - - - - - - -\n")

    print(proyecto_2)
    print(tarea_3)
    print(tarea_4)
    print(equipo_2)

    print("- - - - - - - - - -\n")

    print(proyecto_3)
    print(tarea_5)
    print(tarea_6)
    print(equipo_3)


if __name__ == "__main__":
    main()
