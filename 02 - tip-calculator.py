print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
value_tip = bill * tip / 100
person_pay = (bill + value_tip) / people
print(f"Each person should pay: $ {person_pay:.2f}")
