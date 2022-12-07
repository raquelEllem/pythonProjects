import art_14
import game_data_14
import random


def print_data(compare_data, letter_choice):
    name = compare_data['name']
    description = compare_data['description']
    country = compare_data['country']
    followers_count = compare_data['follower_count']
    print(f"Compare {letter_choice}: {name}, a {description}, from {country}.")
    return followers_count


print(art_14.logo)
out = False
score = 0
while not out:
    compare_a = random.choice(game_data_14.data)
    followers_a = print_data(compare_data=compare_a, letter_choice='A')

    print(art_14.vs)

    compare_b = random.choice(game_data_14.data)
    while compare_a == compare_b:
        compare_b = random.choice(game_data_14.data)

    followers_b = print_data(compare_data=compare_b, letter_choice='B')

    option = input("Who has more followers? Type 'A' or 'B': ").upper()
    if option == 'A':
        if followers_a > followers_b:
            score += 1
            print(f"You right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            out = True
    elif option == 'B':
        if followers_a < followers_b:
            score += 1
            print(f"You right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            out = True
    else:
        print("Invalid Option!")



