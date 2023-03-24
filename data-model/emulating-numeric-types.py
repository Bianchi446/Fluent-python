

# Implementing Vector 

import math 

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)


v1 = Vector(2, 5)
v2 = Vector(10, 5)

print(v1)
print(v2)

print(v2 + v1)
print(abs(v2 + v1))

