
class Computer:

    def __init__(self):
        self.RAM = {f"{i:08b}":"00000000" for i in range(256)}
        self.registers = {
            "PC":None,
            "SR":None,
            "CIR":None,
            "MAR":None,
            "MDR":None,
            "ACC":None,
            "GPR":None,
            "GPR":None,
            "GPR":None
        }
        self.opcode = {
            "000": "store",
            "001": "load",
            "010": "add",
            "011": "sub",
            "100": "AND",
            "101": "OR",
            "110": "XOR",
            "111": "NOT"
        }

    def ALU(self):

        pass



def fetch():
    pass

def decode():
    pass

def execute():
    pass

def main():
    comp = Computer()

if __name__ == "__main__":
    main()