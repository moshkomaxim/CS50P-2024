def main():
    n1, operation, n2 = input("Expression: ").split(" ")
    result = do_math(int(n1), operation, int(n2))
    print(f"{result:.1f}")

def do_math(n1, o, n2):
    match o:
        case "+":
            return n1 + n2
        case "-":
            return n1 - n2
        case "*":
            return n1 * n2
        case "/":
            return n1 / n2
        case _:
            return "Error"

main()