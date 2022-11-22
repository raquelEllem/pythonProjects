import random
logo = """"

   _____                       _   _            _   _                 _               
  / ____|                     | | | |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   

"""
def guees(attempts):
    print(f"You have {attempts} attempts remaining to guess the number.")
    for _ in range(attempts):
        guess = int(input("Make a guess: "))
        if guess > answer:
            print("Too low.")
        elif guess < answer:
            print("Too high.")
        else:
            print(f"You got it! The answer was {answer}.")
            break
        print("Guess again.")
        print(f"You have {attempts - 1 - _} remaining to guess the number.")

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1, 100)
print(answer)
difficulty = input("Choose a difficulty. Type 'easy' ot 'hard': ").lower()
if difficulty == 'easy':
    guees(10)
elif difficulty == 'hard':
    guees(5)
else:
    print("Invalid!")
