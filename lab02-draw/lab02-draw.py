import arcade

arcade.open_window(800, 600, "m")

arcade.set_background_color(arcade.color.BLACK)

arcade.start_render()

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

arcade.draw_text("leon atilano gonzalez sotos", 20, 30, arcade.color.WHITE, 8)

arcade.finish_render()
arcade.run()