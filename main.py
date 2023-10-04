
import random
rock = '''
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock , paper , scissor]

user_choice = int(input("what do you choose? Type 0 for rock , 1 for paper or 2 for scissor"))
if user_choice >= 3 or user_choice < 0:
    print("you typed invalid number")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0 , 2)
    print("computer chose:")
    print(game_images[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("you win!")
    elif computer_choice == 0 and user_choice == 2:
        print("you lose!")
    elif computer_choice > user_choice:
        print("you lose!")
    elif user_choice > computer_choice:
        print("you win!")
    elif computer_choice == user_choice:
        print("It's a draw!")

 