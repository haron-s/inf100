def vowels(text):
    sum_vokaler = 0
    for i in text:
        if i in "aeiouAEIOU":
            sum_vokaler += 1
    return sum_vokaler

def main():
    from pathlib import Path
    import json
    content = Path("strings.json").read_text(encoding="utf-8")
    data = json.loads(content)
    vowels(data)
    for i in data:
        print(f'"{i}": {vowels(i)}')

if __name__ == "__main__":
    main()