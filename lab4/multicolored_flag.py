from uib_inf100_graphics.simple import canvas, display

def draw_multicolored_flag(canvas,x1,y1,x2,y2,colors):
    n = len(colors)

    n_length = (x2 - x1) / n
    for i, color in enumerate(colors):
        xa = x1 + i * n_length
        xb = xa + n_length
        canvas.create_rectangle(xa,y1,xb,y2,fill= color, outline = "")


