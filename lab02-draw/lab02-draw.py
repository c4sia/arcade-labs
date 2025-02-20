import arcade

arcade.open_window(800, 600, "m")

arcade.set_background_color(arcade.color.BLACK)

arcade.start_render()

def luna(x: int, y: int)-> None:
    """
        OBJ: Tener la luna para reutilizar.
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

#LUNA
arcade.draw_circle_filled(290, 364, 77, arcade.color.ASH_GREY)
arcade.draw_circle_filled(256, 395, 7, arcade.color.DAVY_GREY)
arcade.draw_circle_filled(256, 325, 18, arcade.color.DAVY_GREY)
arcade.draw_circle_filled(315, 420, 13, arcade.color.DAVY_GREY)
arcade.draw_circle_filled(315, 360, 12, arcade.color.DAVY_GREY)
arcade.draw_circle_filled(345, 330, 8, arcade.color.DAVY_GREY)
arcade.draw_arc_filled(255, 315, 26, 16, arcade.color.BLACK_OLIVE, 180, 360, 0)
arcade.draw_arc_filled(345, 327, 12, 10, arcade.color.BLACK_OLIVE, 180, 360, 0)
arcade.draw_arc_filled(315, 355, 20, 11, arcade.color.BLACK_OLIVE, 180, 360, 0)
arcade.draw_arc_filled(315, 413, 20, 10, arcade.color.BLACK_OLIVE, 180, 360, 0)


arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.DARK_MIDNIGHT_BLUE)

arcade.draw_line(250, 100, 330, 100, arcade.color.COOL_GREY,6)
arcade.draw_line(260, 94, 320, 94, arcade.color.COOL_GREY, 6)
arcade.draw_line(270, 88, 310, 88, arcade.color.COOL_GREY, 6)

def escribir_mensaje(mensaje: str, x: int, y: int, tamaño_letra: int) -> None:
    """
    OBJ: Escribir un mensaje de texto.
    PRE: -
    """
    arcade.draw_text(mensaje, x, y, arcade.color.WHITE, tamaño_letra)

escribir_mensaje("leon atilano gonzalez sotos", 40, 50, 80)

arcade.finish_render()
arcade.run()