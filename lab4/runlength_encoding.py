
def compress(raw_binary):
    
    count = 0
    run_length = []
    
    for i, binary_val in enumerate(raw_binary):
        if i == 0 and binary_val == "1":
            run_length.append(count)
            count += 1
        elif i == 0:
            count += 1
        elif binary_val == raw_binary[i-1]:
            count += 1
        else:
            run_length.append(count)
            count = 1
    run_length.append(count)

    return run_length

def decompress(compressed_binary):
    raw_binary = ""

    for i, value in enumerate(compressed_binary):
        if i % 2 == 0: raw_binary+= "0" * value
        else: raw_binary += "1" * value
        
    return raw_binary        
            

def test_compress():
    print('Tester compress... ', end='')
    assert([2, 3, 4, 4] == compress('0011100001111'))
    assert([0, 2, 1, 8, 1] == compress('110111111110'))
    assert([4] == compress('0000'))
    print('OK')

def test_decompress():
    print('Tester decompress... ', end='')
    assert('0011100001111' == decompress([2, 3, 4, 4]))
    assert('110111111110' == decompress([0, 2, 1, 8, 1]))
    assert('0000' == decompress([4]))
    print('OK')

test_compress()
test_decompress()