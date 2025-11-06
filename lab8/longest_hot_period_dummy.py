

def longest_hot_period(temperatures, threshold):
    i_array, i_list = [], []
    for i, temp in enumerate(temperatures):
        if temp >= threshold:
            i_list.append(i)
        elif i_list:
            i_array.append(i_list)
            i_list = []
    if i_list:
        i_array.append(i_list)
    
    if i_array:
        longest_stretch = max(i_array, key=len)
        longest_period = (longest_stretch[0], longest_stretch[-1]+1)
    else:
        longest_period = (-1, -1)

    return longest_period

    
            

def test_longest_hot_period():
    print('Testing longest_hot_period... ', end='')
    temps = [25, 23, 19, 22, 24, 25, 21, 25, 26]

    threshold = 22
    expected_start, expected_end = 3, 6
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    threshold = 23
    expected_start, expected_end = 0, 2
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    threshold = 15
    expected_start, expected_end = 0, 9
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    threshold = 21
    expected_start, expected_end = 3, 9
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    threshold = 25
    expected_start, expected_end = 7, 9
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    threshold = 30
    expected_start, expected_end = -1, -1
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    print('OK')

if __name__ == '__main__':
    test_longest_hot_period()
