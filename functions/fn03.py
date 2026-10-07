price = int(input("Enter price: "))
discount = int(input("Enter discount: "))
mem = bool(input("Member Status: "))
def cal(price, discount, member):
    if price < 0:
        return "Invalid price"

    elif discount < 0:
        return "Invalid discount"

    elif discount > 50:
        return "Discount cannot exceed 50%"
    
    elif member == TRUE:
        return "yes"
        
    final = (price * discount) / 100
    fp = price - final
    
    if member == TRUE:
        return (fp * 5) / 100
    
    
x = cal(price, discount)
print("Final price: ", x)