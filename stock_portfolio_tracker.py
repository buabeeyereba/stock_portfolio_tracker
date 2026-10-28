print("=" * 50)

print("Welcome to Buabee's Stock Portfolio Tracker".center(50))

print("=" * 50)

prices = {"AAPL": 180, "GOOGL": 500}
grand_total = 0

while True:
    stock_name = input("Enter Stock name: ").strip().upper()
    if stock_name in prices:
        quantity = int(input("Enter Quantity:  "))
        investment = prices[stock_name] * quantity
        grand_total += investment
        print(f"Added {quantity} shares of {stock_name} (${investment:.2f})")
    else:
        print(f"{stock_name} not found in list")

    try_again = input("do you want to try again?  ").strip().lower()

    if try_again == "no":
        break
print(f"\nGrand Total Portfolio Value: {grand_total}")

file = open("portfolio", "w")
file.write(f"Final Portfolio Total: ${grand_total}\n")
file.close()

print("Portfolio Saved to portfolio.txt file!")