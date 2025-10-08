def test_alternate_sign_sum():
    print('Tester alternate_sign_sum...', end=' ', flush=True)
    assert 3 == alternate_sign_sum([1, 2, 3, 4, 5])
    assert 30 == alternate_sign_sum([10, 20, 30, 40, 50])

    a = [-10, 20, -30, 40, -50]
    assert -150 == alternate_sign_sum(a)
    assert [-10, 20, -30, 40, -50] == a  # Sjekk at funksjon ikke er destruktiv
    print('OK')


def alternate_sign_sum(nums):
    alt_sum = 0
    for index, num in enumerate(nums):
        if index % 2 == 0:
            alt_sum += num
        else:
            alt_sum -= num
    return alt_sum

test_alternate_sign_sum()