import math

class Circle:

    def __init__(self, radius = 1):
        self.radius = radius

    def getPerimeter(self):
        return 2 * self.radius * math.pi

    def getArea(self):
        return self.radius * self.radius * math.pi

    def setRadius(self, radius):
        self.radius = radius


c1 = Circle()
print('Radius of c1: '+str(c1.radius))
c1.setRadius(23)
print('Updated radius of c1: '+str(c1.radius))
print('Perimeter of c1: '+str(c1.getPerimeter()))
print('Area of c1: '+str(c1.getArea()))