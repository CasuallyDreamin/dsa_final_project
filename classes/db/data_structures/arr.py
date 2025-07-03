class arr:
    def __init__(self, size: int = 7):
        self.size = size
        self.array = size * [None]

    def insert(self, idx: int, data):
        self.array[idx] = data

    def get(self, idx: int):
        return self.array[idx]
    
    def __repr__(self):
        return str(self.array)
