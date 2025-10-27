def set_fixed_fields(matrix, qr_layout):
    for zeros in qr_layout["fixed_positions"]["zeros"]:
        row, col = zeros

        matrix[row][col] = 0

    for ones in qr_layout["fixed_positions"]["ones"]:
        row, col = ones

        matrix[row][col] = 1
    return matrix

def set_meta_fields(matrix, err_corr, mask_no, qr_layout):
    for i, coords in enumerate(qr_layout["meta_positions"]["first"]):
        row, col = coords

        matrix[row][col] = qr_layout["meta_patterns"][err_corr][mask_no][i]

    for i, coords in enumerate(qr_layout["meta_positions"]["second"]):
        row, col = coords

        matrix[row][col] = qr_layout["meta_patterns"][err_corr][mask_no][i]
    return matrix
    