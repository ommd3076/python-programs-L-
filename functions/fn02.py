price = int(input("Enter price: "))

discount = int(input("Enter discount: "))

def cal(price, discount):
    if price < 0:
        return "Invalid price"

    elif discount < 0:
        return "Invalid discount"

    elif discount > 50:
        return "Discount cannot exceed 50%"

    final = (price * discount) / 100
    
    return price - final
x = cal(price, discount)
print("Final price: ", x)