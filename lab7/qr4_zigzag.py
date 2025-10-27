def get_next_pos(row, col, size):
    if col % 2 == 0:
        if col == 0:
            return row - 1, col
        return row, col - 1

    if col % 4 == 1:
        if row == size - 1:
            return row, col - 1
        return row + 1, col + 1

    if row == 0:
        return row, col - 1
    return row - 1, col + 1

def bit_list_to_raw_matrix(bit_list, qr_layout):
    invalid_pos = (
        qr_layout["fixed_positions"]["zeros"]
        + qr_layout["fixed_positions"]["ones"]
        + qr_layout["meta_positions"]["first"]
        + qr_layout["meta_positions"]["second"]
    )
    invalid = {tuple(p) for p in invalid_pos}  

    size = qr_layout["side_length"]
    matrix = [[0] * size for _ in range(size)]

    row, col = size - 1, size - 1
    i = 0

    while i < len(bit_list):
        if (row, col) not in invalid:
            matrix[row][col] = bit_list[i]
            i += 1

        n_row, n_col = get_next_pos(row, col, size)

        if not (0 <= n_row < size and 0 <= n_col < size):
            break
        row, col = n_row, n_col

    return matrix