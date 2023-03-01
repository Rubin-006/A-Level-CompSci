from time import sleep
from math import sqrt


class Processor:

    def __init__(self, num_of_process=0):
        self.p = num_of_process


    def fib_seq(self,i=0):
        while True:
            try:
                for i in range(i,10000000):
                    s = int((1/sqrt(5))*((((1+sqrt(5))/2)**i)-(((1-sqrt(5))/2)**i)),)
                    print(s)
                    sleep(1)
            except KeyboardInterrupt:
                self.fib_num_index = i
                print(i)
                next = input(f"What do you want to do next:\n1) Continue from {i}th term?")
                if next == "1":
                    self.fib_seq(self.fib_num_index)
                else:
                    break









a = Processor()

a.fib_seq()