from time import sleep
from math import sqrt


class Processor:

    def __init__(self, num_of_process=0):
        self.p = num_of_process
        self.fib_num_index = 0
        

    def choices(self,a=self.fib_num_index,b,c):
        next = input(
            f"What do you want to do next:\n1. Continue from {i}th term?"
            )

    def triangular(self,i=0):
        run = True
        while run:
            try:
                for i in range(i,10_000_000):
                    num = 0.5*i*(i+1)
                    print(num)
            except KeyboardInterrupt:
                self.tri_num_index = i

            

    def fib_seq(self,i=0):
        run = True
        while run:
            try:
                for i in range(i,10_000_000):
                    s = int((1/sqrt(5))*((((1+sqrt(5))/2)**i)-(((1-sqrt(5))/2)**i)),)
                    print(s)
                    sleep(1)
            except KeyboardInterrupt:
                self.fib_num_index = i
                next = input(f"What do you want to do next:\n1) Continue from {i}th term?")
                if next == "1":
                    self.fib_seq(self.fib_num_index)
                else:
                    run = False









a = Processor()

a.fib_seq()