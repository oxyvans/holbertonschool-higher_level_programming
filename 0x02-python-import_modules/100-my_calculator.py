#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    argv = sys.argv

    if len(argv) < 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    o = argv[2]

    if (o == '+'):
        print(f"{a} + {b} = {add(a, b)}")
    elif (o == '-'):
        print(f"{a} - {b} = {sub(a, b)}")
    elif (o == '*'):
        print(f"{a} * {b} = {mul(a, b)}")
    elif (o == '/'):
        print(f"{a} / {b} = {div(a, b)}")
    else:
        print(f"Unknown operator. Available operators: +, -, * and /")
        exit(1)
