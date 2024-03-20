import pickle

class PickleReaderWriter:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'rb') as file:
            return pickle.load(file)

    def write(self, data):
        with open(self.filename, 'wb') as file:
            pickle.dump(data, file)


