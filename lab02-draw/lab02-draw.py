import arcade

def dibujar_luna(x: int, y: int)-> None:
    """
        OBJ: Dibujar una luna.
        PRE: -
    """
    # LUNA
    arcade.draw_circle_filled(x, y, 77, arcade.color.ASH_GREY)
    arcade.draw_circle_filled(x-34, y+31, 7, arcade.color.DAVY_GREY)
    arcade.draw_circle_filled(x-34, y-39, 18, arcade.color.DAVY_GREY)
    arcade.draw_circle_filled(x+25, y+56, 13, arcade.color.DAVY_GREY)
    arcade.draw_circle_filled(x+25, y-4, 12, arcade.color.DAVY_GREY)
    arcade.draw_circle_filled(x+55, y-34, 8, arcade.color.DAVY_GREY)
    arcade.draw_arc_filled(x-35, y-49, 26, 16, arcade.color.BLACK_OLIVE, 180, 360, 0)
    arcade.draw_arc_filled(x+55, y-37, 12, 10, arcade.color.BLACK_OLIVE, 180, 360, 0)
    arcade.draw_arc_filled(x+25, y-9, 20, 11, arcade.color.BLACK_OLIVE, 180, 360, 0)
    arcade.draw_arc_filled(x+25, y+49, 20, 10, arcade.color.BLACK_OLIVE, 180, 360, 0)

def dibujar_oceano() -> None:
    """
    OBJ: Dibujar un océano.
    PRE: -
    """
    arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.DARK_MIDNIGHT_BLUE)

def dibujar_sombra_luna(x: int, y:int, grosor: int) -> None:
    """
    OBJ: Dibujar la sombra de una luna.
    PRE: -
    """
    arcade.draw_line(x, y, x+80, y, arcade.color.COOL_GREY,grosor)
    arcade.draw_line(x+10, y-6, x+70, y-6, arcade.color.COOL_GREY, grosor)
    arcade.draw_line(x+20, y-12, x+60, y-12, arcade.color.COOL_GREY, grosor)

def escribir_mensaje(mensaje: str, x: int, y: int, tamaño_letra: int) -> None:
    """
    OBJ: Escribir un mensaje de texto.
    PRE: -
    """
    arcade.draw_text(mensaje, x, y, arcade.color.WHITE, tamaño_letra)


def main() -> None:
    """
    OBJ: Iniciar el dibujo.
    PRE: -
    """
    #Iniciar ventana
    arcade.open_window(800, 600, "m")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.start_render()

    #Dibujo
    dibujar_oceano()
    escribir_mensaje("leon atilano gonzalez sotos", 40, 50, 6)
    dibujar_sombra_luna(250, 100, 6)
    dibujar_luna(290, 364)

    #Finalizar dibujo
    arcade.finish_render()
    arcade.run()

main()
