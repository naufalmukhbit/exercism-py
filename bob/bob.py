import re
def response(hey_bob):
    if re.search(r'\?(?!\s+\w)', hey_bob):
        return "Calm down, I know what I'm doing!" if hey_bob.isupper() else "Sure."
    else:
        if hey_bob.isupper():
            return "Whoa, chill out!"
        elif re.search(r'\w+',hey_bob):
            return "Whatever."
        else:
            return "Fine. Be that way!"
