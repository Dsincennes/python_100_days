print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_to_add = bill * (tip/100)
new_sum = round((tip_to_add + bill) / 7, 2)
print(f"Each person should pay: ${new_sum}")

