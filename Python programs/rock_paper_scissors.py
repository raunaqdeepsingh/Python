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
game = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, and 2 for scissors. \n"))
print(game[player_choice])
print("\n Computer chooses: \n")

computer_choice = random.randint(0,2)
print(game[computer_choice])

if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == 0 and computer_choice == 1) or (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 0):
    print("You lose")
else:
    print("You win")