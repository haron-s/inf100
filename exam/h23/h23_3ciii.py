def longest_geometric_sublist(a):
    ...

    


        
def get_quotient(a, i):
    try:
        return a[i+1] / a[i]
    except IndexError:
        return None


# Test
a = [4, 8, 8, 16, 3, 9, 27, 32]
actual = longest_geometric_sublist(a)
expected = [3, 9, 27]   
assert expected == actual