from avvik import count_values_larger_than


def main():
    test_count_values_larger_than()


def test_count_values_larger_than():
    print('Testing count_values_larger_than...', end=' ')

    # Test A
    values = [2, 5, 3, -7, 2, 10]
    threshold = 4
    expected = 2
    actual = count_values_larger_than(values, threshold)
    assert expected == actual

    # Test B
    values = [2, 5, 3, 1, 10]
    threshold = 2
    expected = 3
    actual = count_values_larger_than(values, threshold)
    assert expected == actual

    print('OK')


if __name__ == '__main__':
    main()
