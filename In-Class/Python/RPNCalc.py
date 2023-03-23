

def RPN_Calc(expression):
    stack = expression.split()
    while len(stack) != 1:
        for i in stack:
            try:
                a = float(i)+0
            except ValueError:
                index = stack.index(i) + 1
                calc = stack[:index]
                for _ in range(len(calc)): stack.pop(0)
                calc[2] = calc[2] if calc[2] != "^" else "**"
                ans = eval(f"{calc[0]}{calc[2]}{calc[1]}")
                stack.insert(0, ans)
                print(stack)
    return(f"{stack[0]}")



print(RPN_Calc(input("Enter expression:\n>>")))