def score(word):
    scores = {"aeioulnrst":1, "dg":2, "bcmp":3, "fhvwy":4, "k":5, "jx":8, "qz":10}
    total_score = 0
    for letter in word.lower():
        for i in scores:
            if letter in i:
                total_score += scores[i]
                break
    return total_score