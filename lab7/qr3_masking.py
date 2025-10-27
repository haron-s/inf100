from qr_masking_helpers import should_flip, flip_bit
from qr2_matrix_completion import set_fixed_fields, set_meta_fields
def get_masked_matrix(matrix, mask_no):
    return [
        [
            flip_bit(col)if should_flip(i, j, mask_no) else col
            for j, col in enumerate(row)
        ]
        for i, row in enumerate(matrix)
    ]

def score_matrix(matrix):
    sum_one = sum(cell == 1 for row in matrix for cell in row)
    sum_zero = sum(cell == 0 for row in matrix for cell in row)

    return abs(sum_one - sum_zero)

def get_refined_matrix(raw_matrix, error_correction_level, qr_layout):
    best_matrix = []
    best_score = 0
    for i in range(8):
        matrix = get_masked_matrix(raw_matrix, i)
        matrix = set_meta_fields(matrix, error_correction_level, i, qr_layout)
        matrix = set_fixed_fields(matrix, qr_layout)
        
        if score_matrix(matrix) >= best_score:
            best_matrix = matrix     
               
    return best_matrix