def should_flip(row, col, mask_no):
    masks = [
        lambda row, col: (row + col) % 2 == 0,
        lambda row, col: row % 2 == 0,
        lambda row, col: col % 3 == 0,
        lambda row, col: (row + col) % 3 == 0,
        lambda row, col: (row//2 + col//3) % 2 == 0,
        lambda row, col: (row*col) % 2 + (row*col) % 3 == 0,
        lambda row, col: ((row*col) % 2 + (row*col) % 3) % 2 == 0,
        lambda row, col: ((row+col) % 2 + (row*col) % 3) % 2 == 0,
    ]
    return masks[mask_no](row, col)

def flip_bit(bit):
    return 1 - bit