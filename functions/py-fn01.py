def discounts(x,y):
    w = (x * y )/ 100
    return x - w
x = int(input("Enter the price: "))
y = int(input("Enter the dsicount [%]: "))
z = discounts(x,y)
print("Final: ", z)