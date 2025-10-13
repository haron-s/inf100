from move_snake_helpers import get_next_head_position, subtract_one_from_all_positives
import random
from score import save_score

def move_snake(app):
    app.head_pos= get_next_head_position(app.head_pos, app.direction)
    if not is_legal_move(app.head_pos, app.board):
        app.state = "gameover"
        save_score(app.score)
        return
    
    if app.board[app.head_pos[0]][app.head_pos[1]] == -1:
        add_apple_at_random_location(app.board)
        app.snake_size += 1
        app.score += 1
    subtract_one_from_all_positives(app.board)

    row, col = app.head_pos
    app.board[row][col] = app.snake_size

def add_apple_at_random_location(grid):
    max_random_attempts = int(len(grid) * len(grid[0]) * 0.1)

    for i in range(max_random_attempts):
        row = random.randrange(len(grid))
        col = random.randrange(len(grid[0]))

        if grid[row][col] == 0:
            grid[row][col] = -1
            return

    valid_apple_pos = [
        (i,j)
        for i, row in enumerate(grid)
        for j, value in enumerate(row)
        if value == 0
    ]

    apple_pos = valid_apple_pos.pop(random.randrange(len(valid_apple_pos)))

    grid[apple_pos[0]][apple_pos[1]] = -1

def is_legal_move(pos, board):
    row_n, col_n = len(board), len(board[0])

    if 0 <= pos[0] < row_n and 0 <= pos[1] < col_n:
        if board[pos[0]][pos[1]] <= 0:
            return True
    
    return False
