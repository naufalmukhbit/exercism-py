import re
def is_valid(isbn):
    if re.search(r'[^0-9X\-]|X(?=.)',isbn):
        return False
    else:
        numbers_raw = re.findall(r'[0-9X]', isbn)
        if len(numbers_raw) != 10:
            return False
        numbers = [10 if i == 'X' else int(i) for i in numbers_raw]
        return sum([numbers[i] * (10-i) for i in range(len(numbers))]) % 11 == 0
