def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        distance = 0
        for i in range(len(strand_a)):
            distance += 1 if strand_a[i] != strand_b[i] else 0
        return distance
    else:
        raise ValueError("Strand lengths is not the same!")
