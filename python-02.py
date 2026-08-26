#Program 2 [evaluates conditions] [tests control flow comprehension]. Next step: predict output, run code, submit result.
def check_Status(count):
    if count < 0:
        return "Empty"
    elif count < 5:
        return "Low"
    else:
        return "Optimal"

print(check_Status(-1))
print(check_Status(3))
print(check_Status(10))