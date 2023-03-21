

def bitwise(registers,operation):
    mask_operations = ["AND", "OR", "XOR"]
    converted_value = ""
    mask = ""
    if operation not in mask_operations:
        for i in registers:
            match i:
                case "0":
                    converted_value += "1"
                case "1":
                    converted_value += "0"
    elif operation in mask_operations:
        while len(mask) != len(registers): mask = [i for i in input("Enter mask:\n>>")]
        match operation:
            case "AND":
                for pair in list(zip(registers,mask)):
                    if (pair[0] == "1") and (pair[1] == "1"): converted_value += "1"
                    else: converted_value += "0"
            case "OR":
                for pair in list(zip(registers,mask)):
                    if (pair[0] == "0") and (pair[1] == "0"): converted_value += "0"
                    else: converted_value += "1"
            case "XOR":
                for pair in list(zip(registers,mask)):
                    if (pair[0] == pair[1]): converted_value += "0"
                    else: converted_value += "1"
    
    return converted_value

print(bitwise([i for i in input("Enter Registers:\n>>")],input("Enter the operation (AND,NOT,OR,XOR) \n>>")))