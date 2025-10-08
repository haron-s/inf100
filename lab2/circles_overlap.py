import math

def circles_overlap(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    if distance == r1 + r2 or distance < r1 + r2:
        return True
    else:
        return False

def test_circles_overlap():
    print('Testing circles_overlap...', end='')

    # Sirkel1 med sentrum (0, 0) og radius 1
    # Sirkel2 med sentrum (1, 1) og radius 1
    # Overlapper
    assert circles_overlap(0, 0, 1, 1, 1, 1) is True

    # Sirkel1 med sentrum (0, 0) og radius 2
    # Sirkel2 med sentrum (4, 1) og radius 2
    # Overlapper ikke
    assert circles_overlap(0, 0, 2, 4, 1, 2) is False

    # Sirkel1 med sentrum (0, 0) og radius 3
    # Sirkel2 med sentrum (5, 0) og radius 2
    # De overlapper hverandre i et enkelt punkt
    assert circles_overlap(0, 0, 3, 5, 0, 2) is True
    print('OK')

test_circles_overlap()
