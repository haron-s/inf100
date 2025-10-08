def sequence_for(n):
    sequence = ""
    for i in range(n+1):
        sequence += str(i) + " "
    return sequence

def test_sequence_for():
    print("Tester sequence_for... ", end="")
    assert "0 1 2 3 4 5 " == sequence_for(5)
    assert "0 1 2 3 4 5 6 7 8 9 10 " == sequence_for(10)
    assert "0 " == sequence_for(0)
    print("OK")

def sequence_while(n):
    sequence = ""
    i = 0
    while i <= n:
        sequence+= str(i) + " "
        i += 1

    return sequence
        
test_sequence_for()

def test_sequence_while():
    print("Tester sequence_while... ", end="")
    assert "0 1 2 3 4 5 " == sequence_while(5)
    assert "0 1 2 3 4 5 6 7 8 9 10 " == sequence_while(10)
    assert "0 " == sequence_while(0)
    print("OK")

test_sequence_while()