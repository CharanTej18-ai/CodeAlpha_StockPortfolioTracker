
# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "TCS": 350
}

portfolio = {}

print("------ STOCK PORTFOLIO TRACKER ------")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock_name = input(
        "\nEnter stock name (or 'stop' to finish): "
    ).strip().upper()

    if stock_name == "STOP":
        break

    if stock_name not in stock_prices:
        print("Invalid stock name. Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    portfolio[stock_name] = (
        portfolio.get(stock_name, 0) + quantity
    )

total_investment = 0

print("\n----- YOUR PORTFOLIO -----")
print(f"{'Stock':<10}{'Quantity':<12}{'Price':<12}{'Value':<12}")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value

    print(
        f"{stock:<10}{quantity:<12}"
        f"${price:<11.2f}${value:<11.2f}"
    )

print("-" * 46)
print(f"Total Investment: ${total_investment:.2f}")

save = input("\nSave report to portfolio.txt? (yes/no): ").strip().lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("-----------------------------n")

        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            file.write(
                f"{stock}: Quantity={quantity}, "
                f"Price=${price:.2f}, Value=${value:.2f}\n"
            )

        file.write(f"\nTotal Investment: ${total_investment:.2f}\n")

    print("Report saved successfully in portfolio.txt")

print("Thank you for using Stock Portfolio Tracker!")
