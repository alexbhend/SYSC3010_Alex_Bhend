import random

class thermo:

    def __init__(self, temp):
        self.temp = temp

    def update(self):
        self.temp = random.randint(-30, 30)
        return self.temp
    
