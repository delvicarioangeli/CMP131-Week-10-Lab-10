#Angelina Del VIcario
#11/18/26
#CMP131
#Lab 10
#Problem 2
import random

def computer_choice():
    compChoice = random.randint(1,3)
    if compChoice ==1:
        return "rock"
    elif compChoice == 2:
        return "paper"
    else:
        return "sissors"

def userChoice():
    uchoice = int(input("Press 1 for rock, press 2 for paper or press 3 for sissors"))
    if uchoice == 1:
        return "Rock"
    elif uchoice == 2:
        return "Paper"
    else: 
        return "Sissors"

def determine_winner (c, u):
    if c == u:
        return "tie"
    elif (c =="rock" and u =="Paper") or (c == "paper" and u == "Sissors") or (c=="sissors" and u =="Rock"):
        return "User is the winner"
    else:
        return "Computer wins"

def results(winner):
  print (winner)



def main():
    compChoice = computer_choice()

    u_choice = userChoice()

    winner = determine_winner(compChoice, u_choice)
    results(winner)

main ()