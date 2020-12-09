import re
def abbreviate(words):
    return "".join(re.findall(r'(?<![a-z0-9\'])[a-z0-9]',words.lower())).upper()
