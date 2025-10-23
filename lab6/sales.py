from pathlib import Path

def total_income(path):
    content = Path(path).read_text(encoding="utf-8").splitlines()[1:]
    products = {
        name:{
            "cost" : int(cost),
            "price" : int(price),
            "sold" : int(sold)
        }
        for name, cost, price, sold in (line.split(",") for line in content)
    }

    return sum((p["price"] - p["cost"]) * p["sold"] for p in products.values())

def test_total_income():
    print('Tester total_income... ', end='')
    expected = (
        (50 - 10) * 100
        + (100 - 20) * 50
        + (500 - 50) * 10
        + (1000 - 100) * 5
        + (10000 - 500) * 2
    )
    actual = total_income('sales.csv')
    assert expected == actual, f'{expected=}, {actual=}'
    print('OK')

test_total_income()