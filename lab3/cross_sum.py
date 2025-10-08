def cross_sum(x):
    num_list = [int(i) for i in str(x)]
    tverrsum = 0
    for num in num_list:
        tverrsum += num
    return tverrsum

def nth_cross_sum(n,x):
    number = 0
    nth = 0
    while nth != n:
        #tverrsum
        tverrsum = sum(int(i) for i in str(number)) 

        #inkrementerer
        if tverrsum == x: #inkrementerer nth hver gang vi finner en tverrsum som stemmer
            nth += 1
        if nth != n: #inkrementerer nummeret vi er på så lenge nth ikke er lik n
            number += 1
    return number

def test_nth_cross_sum():
    print('Tester nth_cross_sum... ', end='')
    assert nth_cross_sum(3, 7) == 25
    assert nth_cross_sum(1, 10) == 19
    assert nth_cross_sum(2, 10) == 28
    assert nth_cross_sum(10, 2) == 2000
    print('OK')

test_nth_cross_sum()