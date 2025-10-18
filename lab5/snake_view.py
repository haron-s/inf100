
def draw_board(canvas, x1, y1, x2, y2, board, info_mode):
    width = (x2 - x1) / len(board[0])
    height = (y2 - y1) / len(board)
    
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            color = get_color(cell)
            x_a, y_a = x1 + width * x, y1 + height * y
            x_b, y_b = x_a + width, y_a + height
            
            canvas.create_rectangle(x_a, y_a, x_b, y_b, fill=color)
            if info_mode:
                canvas.create_text(
                    x_a + width/2,
                    y_a + height/2,
                    text=f'{y},{x}\n{cell}'
                )



def get_color(value):
    if value == 0:
        value = "lightgray"
    elif value > 0:
        value = "orange"
    else:
        value = "cyan"
    return value



