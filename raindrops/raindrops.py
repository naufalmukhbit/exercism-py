def convert(number):
    sound = ""
    sound += "Pling" if number % 3 == 0 else ""
    sound += "Plang" if number % 5 == 0 else ""
    sound += "Plong" if number % 7 == 0 else ""
    sound = str(number) if sound == "" else sound
    return sound
