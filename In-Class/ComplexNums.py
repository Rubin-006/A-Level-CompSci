import math

class Complex(object):
    
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return Complex(self.real + no.real,self.imaginary+no.imaginary)
        
    def __sub__(self, no):
        return Complex(self.real-no.real,self.imaginary-no.imaginary)
        pass
        
    def __mul__(self, no):
        return Complex((self.real*no.real)-(self.imaginary*no.imaginary),(self.imaginary*no.real + self.real*no.imaginary))

    def __truediv__(self, no):
        return Complex(round((self.real*no.real+self.imaginary*no.imaginary)/((no.real**2)+(no.imaginary**2)),2),round((self.imaginary*no.real-self.real*no.imaginary)/((no.real**2)+(no.imaginary**2)),2))

    def mod(self):
        return Complex(math.sqrt((self.real**2)+(self.imaginary**2)), 0)


    def __str__(self):
        return f"{self.real}+{self.imaginary}i" if self.imaginary >=0 else f"{self.real}-{self.imaginary}i"



if __name__ == "__main__":
    #c = map(float, input().split())
    #d = map(float, input().split())
    #x = Complex(*c)
    #y = Complex(*d)
    #print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
    c = Complex(2,1)
    d = Complex(5,6)
    print(c/d)

