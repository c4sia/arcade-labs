import arcade


# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3

class Moon:
    def __init__(self, x, y, grosor, change_x, change_y, color_luna1, color_luna2, color_luna3, color_sombra):
        """
        """
        self.x = x
        self.y = y
        self.grosor = grosor
        self.change_x = change_x
        self.change_y = change_y
        self.color_luna1 = color_luna1
        self.color_luna2 = color_luna2
        self.color_luna3 = color_luna3
        self.color_sombra = color_sombra

    def dibujar_oceano(self) -> None:
        """
        OBJ: Dibujar un océano.
        PRE: -
        """
        arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.DARK_MIDNIGHT_BLUE)

    def dibujar_luna(self) -> None:
        """
            OBJ: Dibujar una luna con su sombra.
            PRE: -
        """
        # LUNA
        arcade.draw_circle_filled(self.x, self.y, 77, self.color_luna1)
        arcade.draw_circle_filled(self.x - 34, self.y + 31, 7, self.color_luna2)
        arcade.draw_circle_filled(self.x - 34, self.y - 39, 18, self.color_luna2)
        arcade.draw_circle_filled(self.x + 25, self.y + 56, 13, self.color_luna2)
        arcade.draw_circle_filled(self.x + 25, self.y - 4, 12, self.color_luna2)
        arcade.draw_circle_filled(self.x + 55, self.y - 34, 8, self.color_luna2)
        arcade.draw_arc_filled(self.x - 35, self.y - 49, 26, 16, self.color_luna3, 180, 360, 0)
        arcade.draw_arc_filled(self.x + 55, self.y - 37, 12, 10, self.color_luna3, 180, 360, 0)
        arcade.draw_arc_filled(self.x + 25, self.y - 9, 20, 11, self.color_luna3, 180, 360, 0)
        arcade.draw_arc_filled(self.x + 25, self.y + 49, 20, 10, self.color_luna3, 180, 360, 0)

        #SOMBRA
        arcade.draw_line(self.x-40, self.y-264, self.x+40, self.y-264, self.color_sombra, self.grosor)
        arcade.draw_line(self.x-30, self.y-270, self.x+30, self.y-270, self.color_sombra, self.grosor)
        arcade.draw_line(self.x-20, self.y-276, self.x+20, self.y-276, self.color_sombra, self.grosor)

    def on_update(self):

        self.x += self.change_x
        self.y += self.change_y



class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.BLACK)
        self.moon = Moon(290, 364, 6, 0, 0, arcade.color.ASH_GREY, arcade.color.DAVY_GREY, arcade.color.BLACK_OLIVE, arcade.color.COOL_GREY)

    def on_draw(self):
        self.clear()
        self.moon.dibujar_luna()
        self.moon.dibujar_oceano()

    #def on_mouse_motion(self, x, y, dx, dy):
    #    self.moon.x = x
    #    self.moon.y = y

    def on_update(self, delta_time):
        self.moon.on_update()

    def on_release_key(self, key, modifiers):
        """
        """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.moon_change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.moon.change_y = 0

    def on_press_key(self, key, modifiers):
        """
        Se llama a la función cuando el usuario presiona una tecla.
        """
        if key == arcade.key.LEFT:
            self.moon.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.moon.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.moon.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.moon.change_y = -MOVEMENT_SPEED


def main():
    window = MyGame()
    arcade.run()


main()