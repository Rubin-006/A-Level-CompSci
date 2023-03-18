
InstructionSet = {
    "SUB":"0000",
    "ADD":"0001",
    "LSL":"0010",
    "LSR":"0011",
    "BGT":"0100",
    "BLT":"0101",
    "BEQ":"0110",
    "BNE":"0111",
    "LDR":"1000",
    "MOV":"1001",
    "CMP":"1010",
    "HALT":"1011"
}
registers = {f"R{i}":0 for i in range(15)}
memory = {i:0 for i in range(15)}

add = lambda a,b: a+b
sub = lambda a,b: a-b
bgt = lambda a,b: a>b
blt = lambda a,b: a<b
beq = lambda a,b: a==b
bne = lambda a,b: a!=b

def create_branch(branch_name,data):
    haris = False
    with open(data) as file:
        lines = file.readlines()
        lines_of_branch = []
        for line in lines:
            if haris and (line[0] == " "):
                lines_of_branch.append(line)
            else:
                haris = False
            if line == branch_name:
                haris = True
    print(lines_of_branch)

create_branch("b1:\n",r"In-Class\assemblyCode.txt")


with open(r"In-Class\assemblyCode.txt") as asm:
    r = asm.readlines()
    branch = None
    for line in r:
        line = line.split()
        try:
            match InstructionSet[line[0]]:
                case "1001": # MOV
                    registers[line[1]] = float(line[2])
                case "0001": # ADD
                    num = add(registers[line[2]],registers[line[3]])
                    registers[line[1]] = num
                case "1010": # CMP
                    nums = [registers[line[1]],registers[line[2]]]
                case "0100": # BGT
                    cmp_res = bgt(nums[0],nums[1])
                    if cmp_res: branch = f"{line[1]}:"
                case "0101": # BLT
                    cmp_res = blt(nums[0],nums[1])
                    if cmp_res: branch = f"{line[1]}:"
                case "0110": # BEQ
                    cmp_res = beq(nums[0],nums[1])
                    if cmp_res: branch = f"{line[1]}:"
                case "0111": # BNE
                    cmp_res = bne(nums[0],nums[1])
                    if cmp_res: branch = f"{line[1]}:"
                case "1011":
                    break
        except KeyError:
            pass
            

print(registers)
                