class Garden:
    def __init__(self, diagram, students=[
            "Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"
        ]):
        self.names = {"C": "Clover", "G": "Grass", "R": "Radishes", "V": "Violets"}
        diagram = diagram.split("\n")
        students = sorted(students)
        self.owner = {}
        for count,i in enumerate(range(0,len(diagram[0]),2)):
            self.owner[students[count]] = diagram[0][i:i+2]+diagram[1][i:i+2]

    def plants(self, student):
        return [self.names[i] for i in self.owner[student]]
