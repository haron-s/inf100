def get_geometric_quotient(a):
    if len(a) < 2:
        return 1
    elif a[1] / a[0] == 0:
      return None  

    quotient = a[1] // a[0]
    initial_value = a[0]
    for i, value in enumerate(a):
        if initial_value * quotient ** (i) != value:
            return None
    return quotient 
        
actual = get_geometric_quotient([3, 6, 12])
expected = 2
assert expected == actual

# Test 2
actual = get_geometric_quotient([4, 8, 8, 16, 3, 9, 27, 32])
expected = None
assert expected is actual

# Test 3
actual = get_geometric_quotient([42])
expected = 1
assert expected == actual
