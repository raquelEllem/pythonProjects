from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print("Welcome to the secret auction program.")
out = False
users = {}
while out is False:
    name = input("What is your name? ")
    bid = float(input("What's your bid? $ "))
    users[name] = bid
    option = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if option == 'no':
        out = True
    else:
         clear()

print(f"The bid max is ${max(users.values())}")


