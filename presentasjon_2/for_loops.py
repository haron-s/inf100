MyNumList = [1,5,6,6]
MyStringList = ["for","loops","in","python"]

sum_of_numbers = 0
for num in MyNumList:
    sum_of_numbers += num
print(sum_of_numbers)

sum_of_strings = ""
for string in MyStringList:
    for char in string:
        sum_of_strings += char
    sum_of_strings += " "
print(sum_of_strings)