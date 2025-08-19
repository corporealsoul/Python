class point:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def distance_to(self):
        from math import sqrt
        return sqrt(self.num1**2 + self.num2**2)

pointing = point(2, 4)
print(pointing.distance_to())