import re
def response(hey_bob):
    if not re.search(r'[a-z]',hey_bob):
        if re.search(r'\?$', hey_bob):
            return "Calm down, I know what I'm doing!"
        else:
            if re.search(r'[A-Z]', hey_bob):
                return "Whoa, chill out!"
            else:
                return "Fine. Be that way!"
    else:
        if re.search(r'\?$', hey_bob):
            return "Sure."
        else:
            return "Whatever."


