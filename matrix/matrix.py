class Matrix:
    def __init__(self, matrix_string):
        self.matrix_table = []
        for i in list(matrix_string.split("\n")):
            self.matrix_table.append(list(map(int, i.split(" "))))

    def row(self, index):
        return self.matrix_table[index-1]

    def column(self, index):
        return [i[index-1] for i in self.matrix_table]
