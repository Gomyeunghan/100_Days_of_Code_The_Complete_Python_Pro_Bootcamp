import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def deal_card():
    card = random.choice(cards)
    return card

def calculate_score(card_list):
    card_sum = sum(card_list)

    if card_sum == 21 and len(card_list) == 2:
        return  0
    elif card_sum > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
        card_sum = sum(card_list)
    return card_sum

def calculate_winner(c_score , u_score):
    if c_score ==  u_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return "Win, you has Blackjack"
    elif c_score > 21:
        return "Opponent went over. You win"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > u_score:
        return "You lose"
    elif c_score < u_score:
        return "You win"



def play_game():
    print(art.logo)
    game_over = False
    u_score = -1
    c_score = -1
    u_card_list = []
    c_card_list = []

    for _ in range(2):
        u_card_list.append(deal_card())
        c_card_list.append(deal_card())

    while not game_over:
        u_score = calculate_score(u_card_list)
        c_score = calculate_score(c_card_list)
        print(f'Your cards: {u_card_list}, current score: {u_score}')
        print(f"Computer's first card: {c_card_list[0]}")
        if u_score == 0 or c_score == 0 or u_score > 21:
            game_over = True
        else:
            get_card = input("Type 'y' to get another card, type 'n' to pass: ") == 'y'
            if get_card :
                u_card_list.append(deal_card())
            else :
                game_over = True

    while c_score != 0 and c_score < 17:
        c_card_list.append(deal_card())
        c_score = calculate_score(c_card_list)
    print(f"Your final hand : {u_card_list}, final score: {u_score}")
    print(f"Computer's final hand: {c_card_list} final score: {c_score}")
    print(calculate_winner(c_score, u_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()

# computer_card_data = []
# user_card_data = []
#
# def winer_calc(user_score, computer_score):
#     if user_score <= 21 or computer_score > 21:
#         if user_score > computer_score:
#             print("You won!")
#     else :
#         print("You lost!")
#
#
# for i in range(2):
#     user_random_number = random.randint(0, len(cards)-1)
#     user_card_data.append(cards[user_random_number])
# for i in range(2):
#     computer_random_number = random.randint(0, len(cards)-1)
#     computer_card_data.append(cards[computer_random_number])
#
# print(f"Your cards : {user_card_data}, current score : {sum(user_card_data)}\n"
#       f"Computers's first card :{computer_card_data[0]}\n " )
# get_card = input("Type 'y' to get another card, type 'n' to pass : ")
#
# if get_card == "y":
#     user_random_number = random.randint(0, len(cards) - 1)
#     user_card_data.append(cards[user_random_number])
#     print(f"Your cards : {user_card_data}, current score : {sum(user_card_data)}\n"
#           f"Computers's first card :{computer_card_data[0]}\n ")
#     while(sum(user_card_data) < 22):
#         get_card = input("Type 'y' to get another card, type 'n' to pass : ")
#         if get_card == "y":
#             user_random_number = random.randint(0, len(cards) - 1)
#             user_card_data.append(cards[user_random_number])
#             print(f"Your cards : {user_card_data}, current score : {sum(user_card_data)}\n"
#                   f"Computers's first card :{computer_card_data[0]}\n ")
#
#     if sum(user_card_data) > 21:
#         print(f"Your final hand :{user_card_data} final score : {sum(user_card_data)} ")
#         print(f"Computer's final hand :{computer_card_data} final score : {sum(computer_card_data)}\n ")
#         print("You went over. You lose")
#         input("Do you want to play a game of Blackjack? Type 'y' or 'n' :")
# elif get_card == "n":
#     if sum(computer_card_data) < 22:
#         while(sum(computer_card_data) < 21):
#             computer_random_number = random.randint(0, len(cards) - 1)
#             computer_card_data.append(cards[computer_random_number])
#         print(f"Your final hand :{user_card_data} final score : {sum(user_card_data)} ")
#         print(f"Computer's final hand :{computer_card_data} final score : {sum(computer_card_data)}\n ")
#         winer_calc(sum(user_card_data), sum(computer_card_data))
#
#     else:
#         user_random_number = random.randint(0, len(cards)-1)
#         user_card_data.append(cards[user_random_number])
#         print(f"Your final hand :{user_card_data} final score : {sum(user_card_data)} ")
#         print(f"Computer's final hand :{computer_card_data} final score : {sum(computer_card_data)}\n ")
#         winer_calc(sum(user_card_data), sum(computer_card_data))
