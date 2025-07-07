# List:
# logo
# Do you want to play a game of Blackjack?
# list[11,2,3,4,5,6,7,8,9,10,10,10,10]
# Your cards(list)
# computers cards[list]
# input(Type get another card)
# if y:
#     add card to your cards
# if n:
#     calculate
#     do computers additions
#
# show final score
# ask replay
import art
import random


card_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def hit():
    your_cards.append(random.choice(card_list))
def final_calcs():
    while sum(your_cards) > 21 and 11 in your_cards:
        your_cards[your_cards.index(11)] = 1
    while sum(computer_cards) > 21 and 11 in computer_cards:
        computer_cards[computer_cards.index(11)] = 1
    your_score = sum(your_cards)
    computer_score = sum(computer_cards)
    print(
        f"Your final hand: {your_cards}, final score: {your_score}\nComputer's final hand: {computer_cards}, final score: {computer_score}")

    if computer_score > 21 and your_score > 21:
        draw()
    elif computer_score > 21:
        computer_went_over()
    elif your_score > 21:
        you_went_over()
    elif your_score > computer_score:
        you_win()
    elif your_score == computer_score:
        draw()
    else:
        you_lose()
def computer_cards_check():
    if sum(computer_cards) < 17:
        computer_cards.append(random.choice(card_list))
        computer_cards_check()




def you_went_over():
    print("You went over. You lose 😭")

def you_win():
    print("You win 😄")

def draw():
    print("Draw 🙃")

def blackjack_rizz():
    print(f"Your cards: {your_cards}, current score: {0}\nComputer's first card: {computer_cards[0]}\nYour final hand: {your_cards}, final score: {0}\nComputer's final hand: {computer_cards}, final score: {sum(computer_cards)}\nWin with a blackjack 😎")


def opp_blackjack_rizz():
    print(
        f"Your cards: {your_cards}, current score: {sum(your_cards)}\nComputer's first card: {computer_cards[0]}\nYour final hand: {your_cards}, final score: {sum(your_cards)}\nComputer's final hand: {computer_cards}, final score: {0}\nLose, opponent has Blackjack 😱")
def you_lose():
    print("You lose 😤")

def computer_went_over():
    print("Opponent went over. You win 😁")

def print_score():
    print(f"Your cards: {your_cards}, current score: {sum(your_cards)}\nComputer's first card: {computer_cards[0]}")

if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play = True
else:
    play = False
while play:
    computer_cards = [random.choice(card_list), random.choice(card_list)]
    your_cards = [random.choice(card_list), random.choice(card_list)]
    game = True
    while game:
        total = sum(your_cards)
        print("\n" * 20)
        print(art.logo)
        if (your_cards == [11,10] or your_cards == [10,11]) and (computer_cards == [10,11] or computer_cards == [11,10]):
            draw()
        elif your_cards == [11,10] or your_cards == [10,11]:
            blackjack_rizz()
        elif computer_cards == [10,11] or computer_cards == [11,10]:
            opp_blackjack_rizz()
        else:
            computer_cards_check()
            ask_for_hit = True
            while ask_for_hit:
                print_score()
                if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                    hit()
                    total = sum(your_cards)
                    if total > 21:
                        ask_for_hit = False
                else:
                    ask_for_hit = False
            print_score()
            final_calcs()
            inp = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
            if  inp == 'n':
                play = False
        game = False