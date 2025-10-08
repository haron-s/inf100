def draw_belgian_flag(canvas, x1, y1, x2, y2):
    x_flag_increment = (x2 - x1)/3
    #black
    canvas.create_rectangle(x1, y1, x1 + x_flag_increment, y2, fill= "black", outline="")
    #yellow
    canvas.create_rectangle(x1 + x_flag_increment, y1, x1 + 2*x_flag_increment, y2, fill= "yellow", outline="")
    #red
    canvas.create_rectangle(x1+x_flag_increment*2, y1, x2, y2, fill= "red", outline="")

