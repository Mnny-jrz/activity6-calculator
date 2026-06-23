class StudentGWA:
    def __init__(self, filename):
        self.filename = filename
class StudentGWA:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        with open(self.filename, 'r') as file:
            data = [line.strip().split() for line in file.readlines()]
        return data
class StudentGWA:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        with open(self.filename, 'r') as file:
            data = [line.strip().split() for line in file.readlines()]
        return data

    def find_highest_gwa(self):
        data = self.read_data()
        top_student = min(data, key=lambda x: float(x[1]))
        return top_student
