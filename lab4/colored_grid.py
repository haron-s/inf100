from uib_inf100_graphics.simple import canvas, display

def draw_grid(canvas, x1, y1, x2, y2, color_grid):
    width = (x2 - x1) / len(color_grid[0])
    height = (y2 - y1) / len(color_grid)
    for y, column in enumerate(color_grid):
        for x, row in enumerate(column):
            x_a, y_a = x1 + width * x, y1 + height * y
            x_b, y_b = x_a + width, y_a + height
            canvas.create_rectangle( x_a, y_a, x_b, y_b, fill= row)

