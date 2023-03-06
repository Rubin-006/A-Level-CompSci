class Vector:
    
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,vec):
        return Vector(self.x+vec.x,self.y+vec.y,self.z+vec.z)

    def __sub__(self,vec):
        return Vector(self.x-vec.x,self.y-vec.y,self.z-vec.z)


    def __str__(self):
        return f"{self.x}i+{self.y}j+{self.z}k"
    

v = Vector(1,1,1)
u = Vector(5,7,3)

print(v)
print(v-v)
print(v-u)