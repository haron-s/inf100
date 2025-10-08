def test_largest_factor_of():
    print('Testing largest_factor_of... ', end='')
    assert 3 == largest_factor_of(6)
    assert 1 == largest_factor_of(7)
    assert 4 == largest_factor_of(8)
    print('OK')


def largest_factor_of(x):
    for i in range(1,x):
        if x % i == 0:
            largest_factor = i
    return largest_factor

test_largest_factor_of()