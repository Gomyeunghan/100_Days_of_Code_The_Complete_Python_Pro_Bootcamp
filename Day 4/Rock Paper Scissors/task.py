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
data = [rock, paper, scissors]

player_data = int(input("What do tou choose? Type 0 for Rock , 1 for Paper or 2 for Scissors."))
computer_data = random.randint(0,2)
def print_data(player_data , computer_data):
    print(data[player_data])
    print("Computer chose:\n")
    print(data[computer_data])


if player_data == computer_data :
    print_data(player_data, computer_data)
    print("Draw!")
elif player_data == 0 and computer_data == 1:
    print_data(player_data, computer_data)
    print("You Lose!")
    if computer_data == 2:
        print("You Win!")
elif player_data == 1 and computer_data == 0:
    print_data(player_data, computer_data)
    print("You Win!")
    if computer_data == 2:
        print("You Lose!")
elif player_data == 2 and computer_data == 1:
    print_data(player_data, computer_data)
    print("You Win!")
    if computer_data == 0:
        print("You Lose!")
elif player_data >= 3 or player_data <= 0 :
    print("You typed an invalid number. You lose!")
