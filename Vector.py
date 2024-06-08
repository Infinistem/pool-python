import math
class Vector: # im a 2d matrix that can have operations perfored on it
    def __init__(self,xpos, ypos):
        self.x = xpos
        self.y = ypos
    def add(self, vect): 
        self.x += vect.x
        self.y += vect.y
    def sub(self, vect):
        self.x -= vect.x
        self.y -= vect.y
    def mult(self, val):
        self.x *= val
        self.y *= val
    def div(self, val): 
        self.x /= val
        self.y /= val
    def dotpr(self, vect): 
        return Vector(self.x * vect.x, self.y * vect.y)
    def angle(self): # arctangent 
        return math.atan2(self.x, self.y)
    def length(self): # distance formula
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))
    @staticmethod
    def minusO(self, v1, v2):
        return Vector(v1[0] - v2[0], v1[1] - v2[1])
    @staticmethod # belongs to class, not instances
    def projectUontoV(u, v):
        v2 = u.dupe()
        v2.mult(u.dotpr(v) / v.dotpr(v))
        return v2
    def dupe(self):
        return Vector(self.x, self.y)
    def assign(self, x, y):
        self.x = x
        self.y = y