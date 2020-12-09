import re
isbn1 = "3-598-21508-8"
isbn2 = "3-598-21507-X"
isbn3 = "3-598-2X507-9"

# num1 = re.findall(r'[0-9X]', isbn2)
# print(list(map(int, ['10' if i == 'X' else i for i in num1])))

# print(re.findall(r'[0-9X]', isbn2))
print(re.search('X', isbn2))