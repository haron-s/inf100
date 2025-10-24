from pathlib import Path

def safe_float(value):
    try:
        return float(value)
    except ValueError:
        return value

def string_to_list(string):
    earthquake_list = [
        [id, location, safe_float(impact), time]
        for id, location, impact, time in (line.split(";") for line in string.splitlines())
    ]
    return earthquake_list

def get_impact(line):
    line = line.split(";")

    try:
        return float(line[2])
    except ValueError:
        pass

def filter_earthquakes(earthquake_csv_string, threshold):
    earthquake_list = string_to_list(earthquake_csv_string)

    return "\n".join(
        ";".join([id,location,str(impact),time])
        for id, location, impact, time in earthquake_list
        if isinstance(impact, float) and impact > threshold or id == "id"
    ) + "\n"

def filter_earthquakes_file(source_filename, target_filename, threshold):
    csv_file = Path(source_filename).read_text(encoding="utf-8")
    Path(target_filename).write_text(filter_earthquakes(csv_file, threshold), encoding="utf-8")

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

def test_filter_earthquakes_file():
    print('Tester filter_earthquakes_file... ', end='')

    def read_file(path):
        with open(path, 'rt', encoding='utf-8') as f:
            return f.read()

    filter_earthquakes_file('earthquakes_simple.csv',
                            'earthquakes_above_7.csv', 7.0)
    expected_value = (
        'id;location;impact;time\n'
        'us100068jg;Northern Mariana Islands;7.7;2016-07-29 17:18:26\n'
        'us10006d5h;New Caledonia;7.2;2016-08-11 21:26:35\n'
        'us10006exl;South Georgia Island region;7.4;2016-08-19 03:32:22\n'
    )
    actual_value = read_file('earthquakes_above_7.csv')
    assert expected_value.strip() == actual_value.strip()
    print('OK')

    # Manuell test: Åpne earthquakes_above_7.csv og se at innholdet stemmer

if __name__ == '__main__':
    test_get_impact()
    test_filter_earthquakes()
    test_filter_earthquakes_file()
