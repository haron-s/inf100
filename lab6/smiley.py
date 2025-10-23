def draw_smiley_in_box(canvas, x_left, y_top, x_right, y_bot):
    # Forenklet smilefjes: bare en gul sirkel.
    # TODO: (frivillig) Bytte ut med din egen kode for å tegne smilefjes
    canvas.create_oval(x_left, y_top, x_right, y_bot, fill='yellow')