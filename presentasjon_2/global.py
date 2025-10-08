numbers = [1,4,6,3]

def multiply_list_elements(list):
    for i, num in enumerate(numbers):
        numbers[i] = num * 2
    return numbers

print(multiply_list_elements(numbers))
