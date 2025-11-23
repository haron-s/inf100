def len_geometric_sublist_starting_at(a, start_i):
    quotient = a[start_i+1] / a[start_i]
    initial_value = a[start_i]
    length = 0

    for i in range(start_i, len(a)):
        if round(initial_value * quotient ** (length)) != a[i]:
            return length
        length += 1
    return length

a = [4, 8, 8, 16, 3, 9, 27, 81, 32]

# Test 1: fra i=2, er lengste subliste 8, 16 med k = 2, har lengden 2
actual = len_geometric_sublist_starting_at(a, 2)
expected = 2       
assert expected == actual

# Test 2: fra i=3, er lengste subliste 16, 3 med k = 0.1875, har lengden 2
actual = len_geometric_sublist_starting_at(a, 3)
expected = 2
assert expected == actual

# Test 3: fra i=4, er lengste subliste 3, 9, 27, 81 med k = 3, har lengden 4
actual = len_geometric_sublist_starting_at(a, 4)
expected = 4
assert expected == actual
