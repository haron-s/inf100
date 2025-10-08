def get_next_head_position(head_pos, direction): 
    row, col = head_pos

    if direction == "north":
        next_pos = (row - 1, col)
    elif direction == "south": 
        next_pos = (row + 1, col)
    elif direction == "west":
        next_pos = (row, col - 1)
    elif direction == "east":
        next_pos = (row, col + 1)
    return next_pos

def subtract_one_from_all_positives(grid):
    for row in grid:
        for i, value in enumerate(row):
            if value > 0:
                row[i] = value - 1