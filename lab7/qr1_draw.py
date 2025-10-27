def draw_qr(canvas, x_left, y_top, size, qr):
    size_n = size / len(qr[0])

    for i, row in enumerate(qr):
        for j, cell in enumerate(row):
            color = get_value(cell)
            x_a, y_a = x_left + size_n * j, y_top + size_n * i
            x_b, y_b = x_a + size_n, y_a + size_n
            
            canvas.create_rectangle(x_a, y_a, x_b, y_b, fill= color, outline="")

def get_value(value):
    if value == 1:
        return "black"
    return

def display(matrix):
    from uib_inf100_graphics.simple import canvas, display as dsp
    canvas.create_rectangle(0, 0, 400, 400, fill='white', outline='')
    draw_qr(canvas, 25, 25, 350, matrix)
    dsp(canvas)