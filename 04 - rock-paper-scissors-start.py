import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock, paper, scissors]
choice_user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if 0 > choice_user > 2:
    print("You typed an invalid number!")
    exit()
print(images[choice_user])


print("Computer chose:")
choice_computer = random.randint(0,2)
print(images[choice_computer])

if choice_user == choice_computer:
    print("It's a draw!")
elif choice_user == 0 and choice_computer == 2:
    print("You win!")
elif choice_user < choice_computer:
    print("You lose!")
elif choice_user == 2 and choice_computer == 0:
    print("You lose!")
elif choice_user > choice_computer:
    print("You win!")
print("_")

