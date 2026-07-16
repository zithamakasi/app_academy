user = float(input("How many kilometers do yo want to drive?: "))
price = float(input("How much is the petrol per liter: R"))
liters_needed = user / 10
total_cost = liters_needed * price

print(round(total_cost, 2))