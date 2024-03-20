import csv

class CSVReaderWriter:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            return list(reader)

    def write(self, data):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
