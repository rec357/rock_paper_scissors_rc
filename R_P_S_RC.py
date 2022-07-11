from tkinter import N

import random
#we need to add random



options = ["rock", "paper", "scissors"]

print("Rock, Paper, Scissors, Shoot!")


name = input("Please enter your name: ")

print("Player One is: {}".format (name))

print ("Let's Play!")

player_one_pick = input ("Pick one: Rock, Paper, or Scissors\n")

computer_player_pick = random.choice (options)

print("The computer choice is: {}".format (computer_player_pick))

if player_one_pick == "rock" and computer_player_pick == "rock" : 
    outcome = "tie" 

elif player_one_pick == "paper" and computer_player_pick == "paper" : 
    outcome = "tie" 

elif player_one_pick == "scissors" and computer_player_pick == "scissors" : 
    outcome = "tie" 

elif player_one_pick == "rock" and computer_player_pick == "scissors" : 
    outcome = "Player One Wins!" 

elif player_one_pick == "rock" and computer_player_pick == "paper" : 
    outcome = "Computer Player Wins!" 

elif player_one_pick == "paper" and computer_player_pick == "scissors" : 
    outcome = "Computer Player Wins!" 

elif player_one_pick == "paper" and computer_player_pick == "rock" : 
    outcome = "Player One Wins!" 

elif player_one_pick == "scissors" and computer_player_pick == "rock" : 
    outcome = "Computer Player Wins!" 

elif player_one_pick == "scissors" and computer_player_pick == "paper" : 
    outcome = "Player One Wins!" 

else : 
    outcome = "invalid!"

print("Outcome is: {}".format (outcome))