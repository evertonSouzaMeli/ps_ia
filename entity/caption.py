class Caption:
    def __init__(self, path, date, time, local):
        self.path = path
        self.date = date
        self.time = time
        self.local = local

    def toString(self):
        return self.path, self.date, self.time, self.local
