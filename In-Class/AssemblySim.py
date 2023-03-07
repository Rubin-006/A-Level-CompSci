
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
    "1001":"HALT"
}


registers = {f"R{i}":0 for i in range(15)}

memory = {i:0 for i in range(15)}