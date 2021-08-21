from datetime import datetime as dt

class Operation:
    data = {}

    def __init__(self, data: dict):
        self.data = data

    def __getitem__(self, param):
        if param in self.data:
            return self.data[param]
        else:
            return None

    def __getattr__(self, param):
        if param in self.data:
            return self.data[param]
        else:
            return None
