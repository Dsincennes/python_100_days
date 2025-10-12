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

game_list = [rock, paper, scissors]

value = int(input("Welcome to Rock Paper Scissors, Choose 0 for rock, 1 for paper, 2 for scissors.\nYou Choose: 2"))

print(game_list[value])

comp = random.randint(0,2)
print(f"computer chose: \n{game_list[comp]}")

if comp == 0 and value == 0:
    print("Tie")
if comp == 0 and value == 1:
    print("You win")
if comp == 0 and value == 2:
    print("You Lose")

if comp == 1 and value == 0:
    print("You Lose!")
if comp == 1 and value == 1:
    print("Tie!")
if comp == 1 and value == 2:
    print("You Win!")

if comp == 2 and value == 0:
    print("You Win!")
if comp == 2 and value == 1:
    print("You Lose!")
if comp == 2 and value == 2:
    print("Tie!")