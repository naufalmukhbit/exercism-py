def score(x, y):
    dis = (x**2 + y**2) ** 0.5
    return 10 if dis <= 1 else 5 if dis <= 5 else 1 if dis <= 10 else 0
