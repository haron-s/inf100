from pathlib import Path

def string_to_list(string):
    earthquake_list = [
        [id, location, impact, time] for id, location, impact, time in (line.split(";") for line in string.splitlines())
    ]
    return earthquake_list

def get_impact(line):
    line = line.split(";")

    try:
        return float(line[2])
    except ValueError:
        return

def filter_earthquakes(earthquake_csv_string, threshold):
    earthquake_list = string_to_list(earthquake_csv_string)
    return "\n".join(
        ";".join([id,location,impact,time])
        for id, location, impact, time in earthquake_list
        if id == "id" if impact.isdigit()
    ) + "\n"

def test_get_impact():
    print('Tester get_impact... ', end='')
    assert 1.43 == get_impact('nc72666881;California;1.43;2016-07-27 00:19:43')
    assert 4.9 == get_impact('us20006i0y;Burma;4.9;2016-07-27 00:20:28')
    assert None is get_impact('us20006i0y;Burma;not_a_num;2016-07-27 00:20:28')
    print('OK')

def test_filter_earthquakes():
    print('Tester filter_earthquakes... ', end='')
    input_arg = '''\
id;location;impact;time
nc72666881;California;1.43;2016-07-27 00:19:43
us20006i0y;Burma;4.9;2016-07-27 00:20:28
nc72666891;California;0.06;2016-07-27 00:31:37
nc72666892;California;not_a_number;2016-08-23 03:21:18
'''
    # Test 1
    expected_value = '''\
id;location;impact;time
nc72666881;California;1.43;2016-07-27 00:19:43
us20006i0y;Burma;4.9;2016-07-27 00:20:28
'''
    actual_value = filter_earthquakes(input_arg, 1.1)
    assert expected_value.strip() == actual_value.strip()

    # Test 2
    expected_value = '''\
id;location;impact;time
us20006i0y;Burma;4.9;2016-07-27 00:20:28
''' 
    actual_value = filter_earthquakes(input_arg, 3.0)
    assert expected_value.strip() == actual_value.strip()

    # Test 3
    expected_value = 'id;location;impact;time\n'
    actual_value = filter_earthquakes(input_arg, 5.0)
    assert expected_value.strip() == actual_value.strip()
    print('OK')

if __name__ == '__main__':
    test_get_impact()
    test_filter_earthquakes()
