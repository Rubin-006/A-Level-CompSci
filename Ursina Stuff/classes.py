from math import sqrt

class Vector:
    
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,vec):
        return Vector(self.x+vec.x,self.y+vec.y,self.z+vec.z)

    def __sub__(self,vec):
        return Vector(self.x-vec.x,self.y-vec.y,self.z-vec.z)

    def __mul__(self,num):
        if isinstance(num,(float,int)):
            return Vector(num*self.x,num*self.y,num*self.z)
        
        if isinstance(num, Vector):
            return self.x*num.x+self.y*num.y+self.z*num.z
        
    def __truediv__(self,num):
        return Vector(self.x/num,self.y/num,self.z/num)

    def get_mag(self):
        return sqrt(self.x**2+self.y**2+self.z**2)
    
    def normalise(self):
        mag = self.get_mag()
        return Vector(self.x/mag,self.y/mag,self.z/mag)

    def __str__(self):
        if (self.y < 0) and (self.z < 0):
            return f"{self.x}i{self.y}j{self.z}k"
        elif self.y < 0:
            return f"{self.x}i{self.y}j+{self.z}k"
        elif self.z < 0:
            return f"{self.x}i+{self.y}j{self.z}k"
        else:
            return f"{self.x}i+{self.y}j+{self.z}k" 
        

grav = lambda m,n,r: (m*n)/r**2

class StellarBody:

    def __init__(self,r=0,m=0):
        self.r = r
        self.m = m
