def calculate_price(price, discount = 10):
    final_price = price - (price * discount)/100
    return final_price

result1 = calculate_price(1000)
result = calculate_price(1000, 20)
print(f"Prices are: {result1} and {result}")