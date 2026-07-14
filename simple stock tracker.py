# Simple Stock Tracker

stocks = {
    "TCS": {"quantity": 10, "price": 3500},
    "Infosys": {"quantity": 5, "price": 1500},
    "Reliance": {"quantity": 8, "price": 2800}
}

total_investment = 0

print("----- Stock Tracker -----")

for stock, details in stocks.items():
    investment = details["quantity"] * details["price"]
    total_investment += investment

    print(f"{stock}")
    print(f"Quantity : {details['quantity']}")
    print(f"Price    : ₹{details['price']}")
    print(f"Investment : ₹{investment}\n")

print("-------------------------")
print(f"Total Investment = ₹{total_investment}")