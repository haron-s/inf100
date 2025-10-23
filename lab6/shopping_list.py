from pathlib import Path

def shopping_list_to_dict(shopping_list):
    return dict(
        (name, int(quantitiy))
        for quantitiy, name in (
            element.split(" ")
            for element in shopping_list.split("\n")
            if element.strip()
            )
        )

def shopping_list_file_to_dict(path):
    try:
        return shopping_list_to_dict(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"Error: file '{path}' not found.")
        return {}


def test_shopping_list_to_dict():
    print('Tester shopping_list_to_dict... ', end='')
    arg = '2 brød\n3 pizza\n10 poteter\n1 kaffe\n1 ost\n14 epler\n'
    expected = {
        'brød': 2,
        'pizza': 3,
        'poteter': 10,
        'kaffe': 1,
        'ost': 1,
        'epler': 14,
    }
    actual = shopping_list_to_dict(arg)
    assert expected == actual
    print('OK')

def test_shopping_list_file_to_dict():
    print('Tester shopping_list_file_to_dict... ', end='')
    expected = {
        'brød': 2,
        'pizza': 3,
        'poteter': 10,
        'kaffe': 1,
        'ost': 1,
        'epler': 13,
    }
    actual = shopping_list_file_to_dict('handleliste.txt')
    assert expected == actual
    print('OK')

if __name__ == '__main__':
    test_shopping_list_to_dict()
    test_shopping_list_file_to_dict()