def count_xs(s):
    x_count = 0
    for i in s:
        if i == "x":
            x_count += 1
    return x_count

def test_count_xs():
    print('Tester count_xs... ', end='')
    assert 0 == count_xs('foo bar hei')
    assert 1 == count_xs('x')
    assert 4 == count_xs('xxCoolDragonSlayer99xx')
    print('OK')

test_count_xs()