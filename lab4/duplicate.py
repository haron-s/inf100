def test_duplicate():
    print('Testing duplicate...', end=' ', flush=True)

    # Test 1
    arg = [2, 3, 10, 3, 4]
    return_val = duplicate(arg)
    expected = [4, 6, 20, 6, 8]
    assert return_val is None
    assert expected == arg

    # Test 2
    arg = [3, 2]
    duplicate(arg)
    duplicate(arg)
    expected = [12, 8]
    assert expected == arg

    print('OK')

def test_duplicated():
    print('Testing duplicated...', end=' ', flush=True)

    # Test 1
    arg = [2, 3, 10, 3, 4]
    return_val = duplicated(arg)
    expected = [4, 6, 20, 6, 8]
    assert return_val == expected
    assert arg == [2, 3, 10, 3, 4]

    # Test 2
    arg = [3, 2]
    return_val = duplicated(duplicated(arg))
    expected = [12, 8]
    assert return_val == expected
    assert arg == [3, 2]

    print('OK')

def test_duplicate_2d():
    print('Testing duplicate_2d...', end=' ', flush=True)

    # Test 1
    arg = [
        [2, 3, 4],
        [4, 1, 0]
    ]
    return_val = duplicate_2d(arg)
    expected = [
        [4, 6, 8],
        [8, 2, 0]
    ]
    assert return_val is None
    assert expected == arg

    # Test 2
    arg = [[3, 2], [2, 1], [1, 0]]
    duplicate_2d(arg)
    duplicate_2d(arg)
    expected = [[12, 8], [8, 4], [4, 0]]
    assert expected == arg

    print('OK')

def test_duplicated_2d():
    print('Testing duplicated_2d...', end=' ', flush=True)

    # Test 1
    arg = [
        [2, 3, 4],
        [4, 1, 0]
    ]
    return_val = duplicated_2d(arg)
    expected = [
        [4, 6, 8],
        [8, 2, 0]
    ]
    assert return_val == expected
    assert arg == [
        [2, 3, 4],
        [4, 1, 0]
    ]

    # Test 2
    arg = [[3, 2], [2, 1], [1, 0]]
    return_val = duplicated_2d(duplicated_2d(arg))
    expected = [[12, 8], [8, 4], [4, 0]]
    assert return_val == expected
    assert arg == [[3, 2], [2, 1], [1, 0]]

    print('OK')

def duplicate(numbers):
    numbers[:] = [n*2 for n in numbers]

def duplicated(numbers):
    return [n * 2 for n in numbers]

def duplicate_2d(grid):
    for row in grid:
        row[:] = [n * 2 for n in row]

def duplicated_2d(grid):
    return [[n*2 for n in row] for row in grid]

def main():
    test_duplicate()
    test_duplicated()
    test_duplicate_2d()
    test_duplicated_2d()

if __name__ == "__main__":
    main()