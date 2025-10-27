def get_next_pos(row, col, size):
    if col % 2 == 0:
        if col == 0:
            return row - 1, col
        return row, col - 1

    elif col % 4 == 1:
        if row == size - 1:
            return row, col - 1
        return row + 1, col + 1 

    else:
        if row == 0:
            return row, col - 1
        return row - 1, col + 1

def bit_list_to_raw_matrix(bit_list, qr_layout):