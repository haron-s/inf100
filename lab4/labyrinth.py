from numpy import rot90 

def rotate(grid, clockwise):
    if clockwise: rotated_grid = rot90(grid, -1)
    else: rotated_grid = rot90(grid, 1)

    return rotated_grid.tolist()
    