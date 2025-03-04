import random
import time

# Simulated market data (price fluctuations)
def get_market_price():
    # Simulating price fluctuation (random)
    return round(random.uniform(95, 105), 2)

# Simulated trading strategy
class SimpleTrader:
    def __init__(self, initial_balance):
        self.balance = initial_balance  # The trader's cash balance
        self.position = 0  # Number of stocks owned
        self.stock_price = 0  # Current stock price

    def buy(self, price, quantity):
        cost = price * quantity
        if cost > self.balance:
            print("Insufficient funds to buy!")
        else:
            self.balance -= cost
            self.position += quantity
            print(f"Bought {quantity} stocks at {price} each, balance: {self.balance}")

    def sell(self, price, quantity):
        if quantity > self.position:
            print("Not enough stocks to sell!")
        else:
            self.balance += price * quantity
            self.position -= quantity
            print(f"Sold {quantity} stocks at {price} each, balance: {self.balance}")

    def trade_decision(self):
        # Simulate a decision: Buy if the price is below 100, sell if above 102
        if self.stock_price < 100 and self.balance >= self.stock_price:
            self.buy(self.stock_price, 1)  # Buy 1 stock
        elif self.stock_price > 102 and self.position > 0:
            self.sell(self.stock_price, 1)  # Sell 1 stock
        else:
            print(f"No action taken, current price: {self.stock_price}")

# Main loop to simulate trading activity
def simulate_trading():
    trader = SimpleTrader(initial_balance=1000)  # Initial balance of $1000

    for _ in range(10):  # Simulate 10 trading decisions
        price = get_market_price()
        trader.stock_price = price
        print(f"Current market price: {price}")
        trader.trade_decision()
        time.sleep(1)  # Simulate time delay (1 second)

if __name__ == "__main__":
    simulate_trading()
