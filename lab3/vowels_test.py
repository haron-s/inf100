from pathlib import Path
import json

def load_test_data(file_path):
    content = Path(file_path).read_text(encoding="utf-8")
    data = json.loads(content)
    return data

def test_vokaler_count(vokaler_count_function):
    test_data = load_test_data(Path(__file__).parent / 'test_data.json')
    for case in test_data:
        input_text = case['input']
        expected_output = int(case['expected'])
        assert vokaler_count_function(input_text) == expected_output

if __name__ == "__main__":
    print('Testing vokaler_count... ', end='')
    from vowels import vowels  # Importerer funksjonen som skal testes
    test_vokaler_count(vowels)
    print('OK')
