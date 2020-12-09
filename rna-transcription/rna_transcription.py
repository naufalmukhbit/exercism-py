def to_rna(dna_strand):
    translation = {"G":"C", "C":"G", "T":"A", "A":"U"}
    return "".join([translation[i] for i in dna_strand])
