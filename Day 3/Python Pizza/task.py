print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

p_cost = 0
x_cheese_costs = 0
total = 0

if pepperoni == "Y" and size == "S":
    p_cost = 2
elif pepperoni == "Y":
    p_cost = 3

if extra_cheese == "Y":
    x_cheese_costs = 1

if size == "S":
    total += 15 + p_cost + x_cheese_costs
if size == "M":
    total += 20 + p_cost + x_cheese_costs
if size == "L":
    total += 25 + p_cost + x_cheese_costs

print(f"Your final bill is: ${total}.")