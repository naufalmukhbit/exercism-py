def is_isogram(string):
    for i in string.lower():
        if string.lower().count(i) > 1 and i.isalpha():
            return False
    return True
