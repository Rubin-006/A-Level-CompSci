
InstructionSet = {
    "0000":"SUB",
    "0001":"ADD",
    "0010":"LSL",
    "0011":"LSR",
    "0100":"AND",
    "0101":"ORR",
    "0110":"EOR",
    "0111":"STR",
    "1000":"LDR",
    "1001":"MOV",
    "1010":"HALT"
}


registers = {f"R{i}":0 for i in range(15)}

memory = {i:0 for i in range(15)}

with open(r"In-Class\assemblyCode.txt") as asm:
    r = asm.readlines()
    for line in r:
        line = line.split()
        if InstructionSet[line[0]] == "MOV":
            registers[line[1]] = float(line[2])

        if InstructionSet[line[0]] == "ADD":
            val = registers[line[2]] + registers[line[3]]
            registers[line[1]] = val
            print(val)
