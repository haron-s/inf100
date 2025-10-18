def shopping_list_to_dict(shopping_list):
    shop_list = [foodnum for foodnum in shopping_list.split("\n")]
    return {foodname: num for foodnum in foodnum.split(" ") for foodnum in shop_list}
    
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

if __name__ == '__main__':
    test_shopping_list_to_dict()
