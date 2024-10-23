def f(x):
    return 2*x*x*x - 2*x*x -5

def bijection (a, b):
    if f(a) * f(b) >= 0:
        print(f"No root in range of[{a}:{b}")
        return
    accuracy = 0.000014
    c = (a+b)/2
    
    while abs(f(c)) > accuracy:
        c = (a+b)/2
        
        if f(c) > 0:
            b = c
            print("b = c")
        else:
            a = c
            print("a = c")
    
    print(f"Root is: {c}")

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))

bijection(a,b)