import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def is_blackjack(cards):
    blackjack = False
    if 11 in cards and 10 in cards:
        blackjack = True
    return blackjack


def calculate_score(list_cards):
    """Take a list of cards and return the score calculated from the cards"""
    score = sum(list_cards)
    if 11 in list_cards and score > 21:
        list_cards.remove(11)
        list_cards.append(1)
        return sum(list_cards)
    else:
        return sum(list_cards)


def winner(sc_computer, sc_user, cards_user, cards_computer):
    if sc_user > 21 or sc_computer > 21:
        print(f"Your cards: {cards_user}, final score: {sum(cards_user)}")
        print(f"Computer's final hand: {cards_computer}, final score: {sum(cards_computer)}")
        if sc_user > 21:
            print("You went over! You lose!")
        else:
            print("You WIN!")
    elif sc_computer == sc_user and sc_computer > 21:
        print(f"Your cards: {cards_user}, final score: {sum(cards_user)}")
        print(f"Computer's final hand: {cards_computer}, final score: {sum(cards_computer)}")
        print("It's a draw!")
    elif sc_computer == 21 or sc_user == 21:
        print(f"Your cards: {cards_user}, final score: {sum(cards_user)}")
        print(f"Computer's final hand: {cards_computer}, final score: {sum(cards_computer)}")
        if sc_user == 21:
            print("You win!")
        else:
            print("Computer win!")


def game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user = [random.choice(cards), random.choice(cards)]
    computer = [random.choice(cards), random.choice(cards)]
    if is_blackjack(computer):
        print("Computer is Winner. It's a blackjack!")
        print(f"Your cards: {user}, final score: {sum(user)}")
        print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
    elif is_blackjack(user):
        print("User is Winner. It's a blackjack!")
        print(f"Your cards: {user}, final score: {sum(user)}")
        print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
    else:
        print(f"Your cards: {user}, current score: {sum(user)}")
        print(f"Computer's first card: {computer[0]}")

        scores_computer = calculate_score(computer)
        scores_users = calculate_score(user)

        winner(sc_user=scores_users, sc_computer=scores_computer, cards_computer=computer, cards_user=user)

        out = False
        while not out:
            option = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if option == 'y':
                user.append(random.choice(cards))
                scores_users = calculate_score(user)
                if sum(user) < 21:
                    print(f"Your cards: {user}, current score: {sum(user)}")
                winner(sc_user=scores_users, sc_computer=scores_computer, cards_computer=computer, cards_user=user)
                if sum(user) >= 21:
                    out = True
            elif option == 'n':
                end = False
                while not end:
                    computer.append(random.choice(cards))
                    scores_computer = calculate_score(computer)
                    if calculate_score(computer) >= 16:
                        end = True
                winner(sc_user=scores_users, sc_computer=scores_computer, cards_computer=computer, cards_user=user)
                if 21 > sum(computer) > 16:
                    print(f"Your cards: {user}, final score: {sum(user)}")
                    print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
                out = True
            else:
                print("Invalid option!")


print(logo)
game()
end_game = False
while not end_game:
    option = input("Would you like play again? Type 'y' to yes or 'n' to no: ").lower()
    if option == 'y':
        print(logo)
        game()
    elif option == 'n':
        end_game = True
    else:
        print("Invalid option!")


