import random as rd
from idlelib.colorizer import color_config
from time import sleep

def games(user_choice,computer_choice,user_score,computer_score):
    if user_choice == 0 and computer_choice == 0:
        print()
        print(f"\tUser_choice:{user_choice}\t\t\tComputer_choice:{computer_choice}")
        print("\n\t\t\t\"Match is Draw..\"")
        print(f"\n\tUser_score{user_score}\t\t\tComputer_score{computer_score}")
    elif user_choice == 0 and computer_choice == 2:
        print()
        print(f"\tUser_choice:{user_choice}\t\t\tComputer_choice:{computer_choice}")
        user_score=user_score+1
        print("\n\t\t\t\"user is winner..\"")
        print(f"\n\tUser_score{user_score}\t\t\tComputer_score{computer_score}")
    elif user_choice == 0 and computer_choice == 1:
        print()
        print(f"\tUser_choice:{user_choice}\t\t\tComputer_choice:{computer_choice}")
        computer_score=computer_score+1
        print("\n\t\t\t\"computer is the winner..\" ")
        print(f"\n\tUser_score:{user_score}\t\t\tComputer_score:{computer_score}")

    elif user_choice == 1 and computer_choice == 1:
        print()
        print(f"\tUser_choice:{user_choice}\t\t\tComputer_choice:{computer_choice}")
        print("\n\t\t\t\"match is Draw \"")
        print(f"\n\tUser_score:{user_score}\t\t\tComputer_score:{computer_score}")

    elif user_choice == 1 and computer_choice == 0:
        print()
        print(f"\tUser_choice:{user_choice}\t\t\tComputer_choice:{computer_choice}")
        print("\n\t\t\t\"User is winner..\"")
        user_score=user_score+1
        print(f"\n\tUser_score:{user_score}\t\t\tComputer_score:{computer_score}")

    elif user_choice == 1 and computer_choice == 2:
        print()
        print(f"\tUser_choice:{user_choice}\t\t\tComputer_choice:{computer_choice}")
        print("\n\t\t\t\"Computer is winner..\" ")
        computer_score=computer_score+1
        print(f"\n\tUser_score:{user_score}\t\t\tComputer_score:{computer_score}")

    elif user_choice == 2 and computer_choice == 0:
        print()
        print(f"\tUser_choice:{user_choice}\t\t\tComputer_choice:{computer_choice}")
        print("\n\t\t\t\"Computer is winner..\"")
        computer_score=computer_score+1
        print(f"\n\tUser_score:{user_score}\t\t\tComputer_score:{computer_score}")

    elif user_choice == 2 and computer_choice == 1:
        print()
        print(f"\tUser_choice:{user_choice}\t\t\tComputer_choice:{computer_choice}")
        print("\n\t\t\t\"user is winner...\" ")
        user_score=user_score+1
        print(f"\n\tUser_score:{user_score}\t\t\tComputer_score:{computer_score}")

    elif user_choice == 2 and computer_choice == 2:
        print()
        print(f"\tUser_choice:{user_choice}\t\t\tComputer_choice:{computer_choice}")
        print("\n\t\t\t\"match is Draw \"")
        print(f"\n\tUser_score:{user_score}\t\t\tComputer_score:{computer_score}")
    return computer_score,user_score

choice='y'
computer_score = 0
user_score=0
print("\n*****WELCOME TO ROCK PAPER SCISSOR GAME*****\n")
sleep(.5)
while choice=="y" or choice=="Y":
    user_choice=int(input("Plz select your choice:\n(NOTE:press \"0\" for Rock. \"1\" for Paper. \"2\" for Scissor)\n"))

    Rock='''✊'''
    paper='''✋'''
    scissor='''✌️'''
    if user_choice>2 or user_choice<0:
        print("your are invalid enter")
    else:
        game = [Rock, paper, scissor]
        print("\tUser's choice\t\tComputer's choice\n")
        print("\t",game[user_choice],end="\t")
        if user_choice == 0:
            print("Rock",end="\t\t\t\t")
        elif user_choice == 1:
            print("Paper",end="\t\t\t\t")
        elif user_choice == 2:
            print("Scissor",end="\t\t\t\t")
        computer_choice = rd.randint(0, 2)
        list = ["Rock", "paper", "Scissor"]
        print(game[computer_choice],end="\t")
        print(list[computer_choice],end="\n")

        a,b=games(user_choice,computer_choice,user_score,computer_score)

        sleep(.5)
        computer_score=a
        user_score=b
        choice=input("\nDo you want to continue..(y/n):\n")
        print()
        sleep(.5)
else:
    print(f"Users choice:{b}\t\tComputers choice:{a}\n")
    if a>b:
        print("\t\t\"Computer Won\"\n\tbetter Luck next time")
    elif b>a:
        print("\t\t\t\"Hurray\"!...\n\t\tYou have won the Match..")
    else:
        print("\t\tIts a Draw... \n\tbetter luck next time")