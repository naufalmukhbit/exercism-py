import re
def decode(string):
    decoded = ""
    for m in re.findall(r'\d+.|.', string):
        decoded += int(m[:-1]) * m[-1] if len(m) > 1 else m
    return decoded


def encode(string):
    encoded = ""
    for m in re.finditer(r'(.)\1*', string):
        group = m.group(0)
        encoded += str(len(group)) + group[0] if len(group) > 1 else group
    return encoded