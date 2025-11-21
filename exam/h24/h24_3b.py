def add_total_lab_score_verbose(data):
    total_sum = 0
    for element in data:
        if element[:3] == "lab":
            total_sum += data[element]
    data["total_lab_score"] = total_sum

def add_total_lab_score(data):
    data["total_lab_score"] = sum(
        value for key, value in data.items()
        if key[:3] == "lab"
    )
    
def test_add_total_lab_score():
    print('Testing add_total_lab_score...', end='')

    # Test A
    data = {
        'student_name': 'Kari',
        'lab1': 20,
        'lab2': 22,
        'lab3': 23,
    }
    add_total_lab_score(data)
    assert data == {
        'student_name': 'Kari',
        'lab1': 20,
        'lab2': 22,
        'lab3': 23,
        'total_lab_score': 65,
    }

    # Test B
    data = {
        'course_id': 'FNI100',
        'labA': 25,
        'labB': 25,
    }
    add_total_lab_score(data)
    assert data == {
        'course_id': 'FNI100',
        'labA': 25,
        'labB': 25,
        'total_lab_score': 50,
    }
    print(' OK')

test_add_total_lab_score()