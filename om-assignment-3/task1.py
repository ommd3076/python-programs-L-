x = int(input("Enter an number: "))
def factorial(x):
    res = 1
    while x > 1:
        res *= x
        x -= 1
    return res
    
print(f"Factorial of  {x} is : {factorial(x)}")