from ftplib import print_line


class Habitacion:
    """
    Clase que representa la habitación en la que se encontrará el jugador.
    """
    def __init__(self, descripcion, norte, sur, este, oeste):
        """
        Método para inicializar las variables del objeto.
        """
        self.descripcion = descripcion
        self.norte = norte
        self.sur = sur
        self.este = este
        self.oeste = oeste


def main():
    """
    Programa principal.
    """
    lista_habitaciones = []

    habitacion1 = Habitacion("No hay mucho que observar en esta habitación, tan solo te puedes percatar de unas paredes que recientemente han sido pintadas de blanco. Puedes seguir por el norte o el este.", 1, None, 1, None)
    lista_habitaciones.append(habitacion1)

    habitacion2 = Habitacion("Al no haber ventanas en este espacio, es imposible percibir el paso del tiempo. Está adornada con extrañas figuras. Has llegado a un extremo del lugar, solo puedes seguir por el sur o el este.", None, 1, 1, None)
    lista_habitaciones.append(habitacion2)

    pasillo_principal = Habitacion("Con suerte se puede ver a lo largo de este pasillo, en los cuadros observas a gente desconocida con algo en común: sus ojos son de color blanco. Tienes varios sitios por explorar: el norte, el este o el oeste.", 1, None, 1, 1)
    lista_habitaciones.append(pasillo_principal)

    pasillo_principal2 = Habitacion("Sigues estando en el pasillo principal, pero cuanto más avanzas, menos luz hay. Ya no hay cuadros y las paredes parecen estar en mal estado, logras ver los ladrillos. Puedes seguir por el norte, el sur o el oeste.", 1, 1, None, 1)
    lista_habitaciones.append(pasillo_principal2)

    cocina = Habitacion("Huele a moho y tampoco parece que alguien haya estado en esta cocina por al menos 2 años. Observas unos cristales rotos en el suelo y también un mensaje oculto escrito. No parece ser de algún idioma conocido. No puedes avanzar más, solo te queda retroceder. Puedes volver por el sur.", None, 1, None, None)
    lista_habitaciones.append(cocina)

    salon = Habitacion("Está todo a oscuras y no tienes manera tampoco de poder ver en la oscuridad. El interruptor está roto. Parece que puedes avanzar hacia el norte o el este, puedes retroceder hacia el oeste o el sur.", 1, 1, 1, 1)
    lista_habitaciones.append(salon)

    salon2 = Habitacion("Acabas de llegar al otro extremo del salón sorprendentemente sin luz. Te has tropezado por el camino con algo metálico pero no sabes qué es. Puedes retroceder por el sur o avanzar por el este.", 0, 1, 1, 0)
    lista_habitaciones.append(salon2)

    salon3 = Habitacion("Al no poder ver en la oscuridad, has seguido avanzando ciegamente y te has caído por un agujero de cierta profundidad. Lograste sobrevivir a la caída por el agua que hay, pero no por mucho tiempo. Algo en el fondo del agua te ha dejado inmovilizado. Definitivamente, la curiosidad mató al gato.", None, None, None, None)
    lista_habitaciones.append(salon3)

    habitacion_actual = 0

    done = False
    while done == False:
        print_line("")
        print(lista_habitaciones[habitacion_actual].descripcion)
        direccion = input("¿Hacia donde deseas avanzar?")
        if direccion.lower() == "norte":
            siguiente_habitacion = 1
            if siguiente_habitacion == None:
                print("No puedes ir en esa dirección.")
            else:
                habitacion_actual = siguiente_habitacion

main()

