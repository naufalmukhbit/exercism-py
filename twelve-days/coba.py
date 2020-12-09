start_sentence = "On the twelfth day of Christmas my true love gave to me: "
days = [
    ["first", "a Partridge in a Pear Tree."], 
    ["second", "two Turtle Doves, and "], 
    ["third", "three French Hens, "], 
    ["fourth", "four Calling Birds, "], 
    ["fifth", "five Gold Rings, "], 
    ["sixth", "six Geese-a-Laying, "], 
    ["seventh", "seven Swans-a-Swimming, "], 
    ["eighth", "eight Maids-a-Milking, "], 
    ["ninth", "nine Ladies Dancing, "], 
    ["tenth", "ten Lords-a-Leaping, "], 
    ["eleventh", "eleven Pipers Piping, "], 
    ["twelfth", "twelve Drummers Drumming, "]
]
def recite(start_verse, end_verse):
    if start_verse == end_verse:
        start_sentence = "On the "+ days[start_verse-1][0] +" day of Christmas my true love gave to me: "
        return [start_sentence + "".join([days[i][1] for i in range(end_verse)])]
    else:
        return [recite(n, n)[0] for n in range(start_verse, end_verse+1)]

print(recite(2,2))