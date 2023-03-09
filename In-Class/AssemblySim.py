
InstructionSet = {
    "SUB":"0000",
    "ADD":"0001",
    "LSL":"0010",
    "LSR":"0011",
    "AND":"0100",
    "ORR":"0101",
    "EOR":"0110",
    "STR":"0111",
    "LDR":"1000",
    "MOV":"1001",
    "HALT":"1010"
}


registers = {f"R{i}":0 for i in range(15)}

memory = {i:0 for i in range(15)}

with open(r"In-Class\assemblyCode.txt") as asm:
    r = asm.readlines()
    for line in r:
        line = line.split()
        if InstructionSet[line[0]] == "1001":
            registers[line[1]] = float(line[2])

        if InstructionSet[line[0]] == "0001":
            val = registers[line[2]] + registers[line[3]]
            registers[line[1]] = val
            print(val)
