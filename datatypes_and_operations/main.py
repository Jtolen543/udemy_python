print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to provide? 10, 12, or 15: ")) / 100
total_people = int(input("How many people are splitting the bill? "))
cost = "{:.2f}".format(total_bill * (1 + tip) / total_people, 2)
print(f"Each person should pay: ${cost}")
