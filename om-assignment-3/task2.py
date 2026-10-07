import math
n = int(input("Enter an number: "))
def sq(n):
    a = math.sqrt(n)
    return a

def lg(n):
    b = math.log(n)
    return b
def si(n):
    c = math.sin(n)
    return c

print("Square root: ", sq(n))
print("Log: ", lg(n))
print("Sine: ", si(n))