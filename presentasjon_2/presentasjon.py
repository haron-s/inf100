def multiply_list_elements(myList):
    for i, num in enumerate(myList):
        myList[i] = num * 2
    return myList

def multiply_list_elements_nondestructive(myList):
    newList = []
    for num in myList:
        newList.append( num * 2)
    return newList

def main():
    numbers = [1,4,6,3]

    result = multiply_list_elements_nondestructive(numbers)
    print(f'Ikke destruktiv:\n{result}')
    print(f'{numbers}\n')

    result = multiply_list_elements(numbers)
    print(f'Destruktiv:\n{result}')
    print(numbers)

if __name__ == "__main__":
    main()