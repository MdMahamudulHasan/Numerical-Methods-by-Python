# Defining the function
def f(x):
    return x*x*x - x - 1

# Implementing Bisection Method using for-loop without max_iter
def bisection(x0, x1, e):
    results = []

    print(f"n      x0       f(x0)          x1       f(x1)         x2        f(x2)       Update")
    
    # For loop with an arbitrary large number of iterations (acts like a while loop)
    for step in range(1, 1000):  # Large number to ensure the loop continues until condition is met
        x2 = (x0 + x1) / 2
        update = ""

        # Check if the result is within the tolerable error
        if abs(f(x2)) < e:
            results.append(f"{step}  {x0:.6f}   {f(x0):.6f}    {x1:.6f}    {f(x1):.6f}    {x2:.6f}    {f(x2):.6f}  \n Root found at x2 = {x2:.6f}, f(x2) = {f(x2):.6f}")
            break

        # Update either x0 or x1 based on the sign of f(x2)
        if f(x0) * f(x2) < 0:
            x1 = x2
            update = "x1 = x2"
        else:
            x0 = x2
            update = "x0 = x2"

        # Append results including the update in the same line
        results.append(f"{step}  {x0:.6f}   {f(x0):.6f}    {x1:.6f}    {f(x1):.6f}    {x2:.6f}    {f(x2):.6f}   {update}")

    return results

# Input Section
if __name__ == "__main__":
    # Input initial guesses and tolerable error
    x0 = float(input("Enter the first guess (x0): "))
    x1 = float(input("Enter the second guess (x1): "))
    e = float(input("Enter the tolerable error (e): "))

    # Ensure that f(x0) * f(x1) < 0
    if f(x0) * f(x1) >= 0:
        print("The initial guesses do not bracket the root.")
    else:
        results = bisection(x0, x1, e)
        for result in results:
            print(result)
