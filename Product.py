product = input("Enter the product name: ")
price = float(input("Enter the product price: "))
quantity = int(input("Enter the quantity: "))

total = price * quantity

print("\n----- Product Summary -----")
print(f"Product Name: {product}")
print(f"Price       : ${price:.2f}")
print(f"Quantity    : {quantity}")
print(f"Total Cost  : ${total:.2f}")

if(total > 50000):
    print("Eligible for free delivery.")
else:
    print("Delivery charge: 100")

