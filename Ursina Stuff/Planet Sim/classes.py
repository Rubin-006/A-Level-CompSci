from numpy import *

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

class Body:
    
    AU = 1.496*(10**11)

    def __init__(self,T=1,radius=0,mass=0,x=0,y=0,z=0):
        self.pos = Vector(x,y,z)
        self.radius = radius
        self.mss = mass
        self.period = T
        self.angularDisplacment = 2*pi/self.period 
    
    def acceleration(self,mass_of_star):
        pass

    def force_of_attraction(self,mass_of_star):
        G = 6.67*(10**-11)
        return (G*self.mass*mass_of_star)/self.pos.get_mag()
    
class PlanetarySystem:

    def __init__(self,star,planets=[]):
        self.star = star
        self.planets = planets
        pass
