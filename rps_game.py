"""This program is a rock-paper-scissors game. The user chooses rock, paper or scissors and the computer does the same at random. The outcomes are compared and the winner will be announced."""

from random import randint # imports randint function from random module
options = ["ROCK", "PAPER", "SCISSORS"]
message = {
  "tie" : "Yawn it's a tie!",
  "won" : "Yay you won!",
  "lost" : "Aww you lost!"
  }
def decide_winner(user_choice, computer_choice): # function with 2 arguments in printing out the outcome of the game
  print (f"You chose {user_choice} !") # user_choice and computer_choice are not yet defined here
  print (f"The computer chose {computer_choice} !") 
  if user_choice == computer_choice:
    print (message["tie"]) # prints value attached to the key "tie" from the message list
  elif user_choice == "ROCK" and computer_choice == "SCISSORS":
    print (message["won"])
  elif user_choice == "PAPER" and computer_choice == "ROCK":
    print (message["won"])
  elif user_choice == "SCISSORS" and computer_choice == "PAPER":
    print (message["won"])
  else:
    print (message["lost"])
def play_RPS(): #function to receive input from user and generate one from computer
  user_choice = input("Enter Rock, Paper, or Scissors: ")
  user_choice = user_choice.upper()
  computer_choice = options[randint(0, 2)] # chooses an item at a random index position from options list
  decide_winner(user_choice, computer_choice) # calls the function decide_winner by inputing the 2 arguments

play_RPS()
