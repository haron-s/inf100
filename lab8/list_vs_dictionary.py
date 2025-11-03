def key_value_getter(d):
    print("Dictionary keys:")
    for key in d:
        print(key)

    print("\nDictionary values:")
    for value in d.values():
        print(value)

    print("\nDictionary keys/value:")
    for key,value in d.items():
        print(f'{key} {value}')

def index_value_getter(a):
    print("List indices:")
    for i in range(len(a)):
        print(i)

    print("\nList values:")
    for i in range(len(a)):
        print(a[i])

    print("\nDictionary keys/value:")
    for i, value in enumerate(a):
        print(f'{i} {value}')
    