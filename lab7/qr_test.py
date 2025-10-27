from qr1_draw import *
from qr2_matrix_completion import *
from qr3_masking import *
from qr4_zigzag import *

def test_set_fixed_fields():
    print('Testing set_fixed_fields...', end='')
    matrix = [
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
    ]
    sample_layout = {
        'about': 'A fake and incomplete QR layout for testing only',
        'side_length': 5,
        'fixed_positions': {
            'zeros': [
                [3, 2], [3, 3], [3, 4], [4, 2], [4, 3], [4, 4]
            ],
            'ones': [
                [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2]
            ]
        }
        # skipping keys 'byte_capacity', 'meta_positions' and 'meta_patterns'
        # since they are irrelevant here 
    }
    set_fixed_fields(matrix, sample_layout)
    assert matrix == [
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0],
    ]

    print(' OK')

def test_set_meta_fields():
    print('Testing set_meta_fields...', end='')
    # For easier visualization the test uses a matrix of strings rather
    # than 0's and 1's, but ultimately 1's and 0's should also work
    matrix = [
        ['-', '|', '-', '|', '-'],
        ['|', '-', '|', '-', '|'],
        ['-', '|', '-', '|', '-'],
        ['|', '-', '|', '-', '|'],
        ['-', '|', '-', '|', '-'],
    ]
    sample_layout = {
        'about': 'A fake and incomplete QR layout for testing only',
        'side_length': 5,
        # skipping key 'fixed_positions' since it is irrelevant here 
        'meta_positions': {
            'first': [
                [0, 0], [0, 1], [0, 2]
            ],
            'second': [
                [0, 4], [4, 4], [3, 1]
            ]
        },
        'meta_patterns': {
            'L': [
                ['A', 'B', 'C'], # mask_no = 0
                ['a', 'b', 'c']  # mask_no = 1
            ],
            'Q': [
                ['Q', 'R', 'S'], # mask_no = 0
                ['q', 'r', 's']  # mask_no = 1
            ],
        }
    }
    err_corr = 'L'
    mask_no = 0
    set_meta_fields(matrix, err_corr, mask_no, sample_layout)
    assert matrix == [
        ['A', 'B', 'C', '|', 'A'],
        ['|', '-', '|', '-', '|'],
        ['-', '|', '-', '|', '-'],
        ['|', 'C', '|', '-', '|'],
        ['-', '|', '-', '|', 'B'],
    ]

    err_corr = 'Q'
    mask_no = 1
    set_meta_fields(matrix, err_corr, mask_no, sample_layout)
    assert matrix == [
        ['q', 'r', 's', '|', 'q'],
        ['|', '-', '|', '-', '|'],
        ['-', '|', '-', '|', '-'],
        ['|', 's', '|', '-', '|'],
        ['-', '|', '-', '|', 'r'],
    ]

    print(' OK')

def test_get_masked_matrix():
    print('Testing get_masked_matrix...', end='')
    blank_5x5_matrix = [[0] * 5 for _ in range(5)]

    actual = get_masked_matrix(blank_5x5_matrix, 0)
    expected = [
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
    ]
    assert expected == actual
    assert blank_5x5_matrix == [[0] * 5 for _ in range(5)]

    actual = get_masked_matrix(expected, 1)
    expected = [
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
    ]
    assert expected == actual
    print(' OK')

def test_score_matrix():
    print('Testing get_score_matrix...', end='')
    arg = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert 5 == score_matrix(arg)

    arg = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]
    assert 1 == score_matrix(arg)
    print(" OK")

def test_get_next_pos_basic():
    print('Testing get_next_pos (basic)...', end='')
    size = 25
    # De første flyttene
    assert (24, 23) == get_next_pos(24, 24, size)
    assert (23, 24) == get_next_pos(24, 23, size)
    assert (23, 23) == get_next_pos(23, 24, size)
    ...
    # Når vi har sikksakket helt til topps
    assert (0, 23) == get_next_pos(0, 24, size)
    assert (0, 22) == get_next_pos(0, 23, size)
    assert (0, 21) == get_next_pos(0, 22, size)
    assert (1, 22) == get_next_pos(0, 21, size)
    assert (1, 21) == get_next_pos(1, 22, size)
    assert (2, 22) == get_next_pos(1, 21, size)
    ...
    # Når vi har ned helt til bunns igjen
    assert (24, 20) == get_next_pos(24, 21, size)
    assert (24, 19) == get_next_pos(24, 20, size)
    ...
    # Siste kolonne
    assert (24, 0) == get_next_pos(24, 1, size)
    assert (23, 0) == get_next_pos(24, 0, size)
    assert (22, 0) == get_next_pos(23, 0, size)
    print(' OK')
def test_get_next_pos_5x5():
    print('Testing get_next_pos (5x5)...', end='')

    size = 5
    expected = [
        [24, 11, 10, 9, 8],
        [23, 13, 12, 7, 6],
        [22, 15, 14, 5, 4],
        [21, 17, 16, 3, 2],
        [20, 19, 18, 1, 0]
    ]
    actual = [[-1] * size for _ in range(size)]
    row, col = 4, 4
    for i in range(size * size):
        actual[row][col] = i
        row, col = get_next_pos(row, col, size)

    assert expected == actual
    print(' OK')
def test_get_next_pos_9x9():
    print('Testing get_next_pos (9x9)...', end='')
    size = 9
    expected = [
        [80, 55, 54, 53, 52, 19, 18, 17, 16],
        [79, 57, 56, 51, 50, 21, 20, 15, 14],
        [78, 59, 58, 49, 48, 23, 22, 13, 12],
        [77, 61, 60, 47, 46, 25, 24, 11, 10],
        [76, 63, 62, 45, 44, 27, 26, 9, 8],
        [75, 65, 64, 43, 42, 29, 28, 7, 6],
        [74, 67, 66, 41, 40, 31, 30, 5, 4],
        [73, 69, 68, 39, 38, 33, 32, 3, 2],
        [72, 71, 70, 37, 36, 35, 34, 1, 0]
    ]
    
    actual = [[-1] * size for _ in range(size)]
    row, col = 8, 8
    for i in range(size * size):
        actual[row][col] = i
        row, col = get_next_pos(row, col, size)

    assert expected == actual
    print(' OK')

def test_bit_list_to_raw_matrix():
    print('Testing bit_list_to_raw_matrix...', end='')
    # To make the test easier to read, bit_list contain distinct elements here
    # (in actual applications, bit_list would only have 0's and 1's)
    arg_bit_list = list(range(1, 72))
    arg_qr_layout = {
        'about': 'A fake and incomplete QR layout for testing only',
        'side_length': 9,
        'fixed_positions': {
            'ones': [
                [1, 3], [1, 4], 
            ],
            'zeros': [
                [2, 3], [2, 4],
            ]
        },
        'meta_positions': {
            'first': [
                [5, 2], [5, 3]
            ],
            'second': [
                [6, 2], [6, 3]
            ]
        }
        # key 'meta_patterns' skipped, since it is irrelevant for this task
    }

    expected = [
        [ 0, 50, 49, 48, 47, 20, 19, 18, 17],
        [ 0, 52, 51,  0,  0, 22, 21, 16, 15],
        [71, 54, 53,  0,  0, 24, 23, 14, 13],
        [70, 56, 55, 46, 45, 26, 25, 12, 11],
        [69, 58, 57, 44, 43, 28, 27, 10,  9],
        [68, 59,  0,  0, 42, 30, 29,  8,  7],
        [67, 60,  0,  0, 41, 32, 31,  6,  5],
        [66, 62, 61, 40, 39, 34, 33,  4,  3],
        [65, 64, 63, 38, 37, 36, 35,  2,  1]
    ]
    actual = bit_list_to_raw_matrix(arg_bit_list, arg_qr_layout)
    assert expected == actual
    print(' OK')

if __name__ == '__main__':
    # sample_grid = [
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    #     [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    #     [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
    #     [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
    #     [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    #     [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    #     [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
    #     [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
    #     [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # ]
    
    # display(sample_grid)

    test_set_fixed_fields()
    test_set_meta_fields()
    test_get_masked_matrix()
    test_score_matrix()
    test_get_next_pos_basic()
    test_get_next_pos_5x5()
    test_get_next_pos_9x9()
    test_bit_list_to_raw_matrix()