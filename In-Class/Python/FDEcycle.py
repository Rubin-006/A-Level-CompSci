
class Computer:

    def __init__(self):
        self.RAM = {f"{i:08b}":"000 00000" for i in range(10)}
        self.addresses = list(self.RAM.keys())
        self.registers = {
            "PC": self.addresses[0],
            "SR": None,
            "CIR": None,
            "MAR": None,
            "MDR": None,
            "ACC": None,
            "GPR": None,
            "GPR": None,
            "GPR": None
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

    def fetch(self):
        data = self.registers["PC"]
        self.registers["MAR"] = self.registers["PC"]
        self.registers["MDR"] = self.RAM[self.registers["MAR"]]
        self.registers["PC"] = self.addresses[self.addresses.index(data) + 1]
        self.registers["CIR"] = self.registers["MDR"]
        print("PC:", self.registers["PC"])
        print("MAR:", self.registers["MAR"])
        print("MDR:", self.registers["MDR"])
        print("CIR:", self.registers["CIR"])
    
    def decode(self):
        instruction = self.opcode[self.registers["MDR"][:3]]
        data = self.registers["MDR"][3:]
        return (instruction,data)

    def execute(self):
        instruction, data = self.decode()
        match instruction:
            case "store":
                print("Stored value magically")
            case "load":
                print("Loaded Value Magically")
            case "add":
                data1 = int((((self.RAM[bin(int(self.registers["MAR"],2) - 1)]))[3:]),2)
                data2 = int(data,2)
                print(data1+data2)

    def cycle(self):
        while True:
            try:
                self.fetch()
                self.execute()
            except:
                break

def main():
    comp = Computer()
    comp.RAM["00000000"] = "00000001"
    comp.RAM["00000001"] = "01000001"
    comp.fetch()
    comp.execute()
    comp.fetch()
    comp.execute()

if __name__ == "__main__":
    main()