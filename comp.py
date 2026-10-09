print("game start")
choices = ["rock" , "paper" , "sis"]
import random 

#loop

a = input("click yes if you waana play if not then no")
while a == "yes":
    comp = random.choice(choices)
    user = input(" enter rock or paper or sis ") 
    if user == comp:
        print(" tie play agan")
    elif user == "rock" and comp == "sis" :
        print(" you win try again ")
    elif user == "rock" and comp == "paper" :
        print(" you loose tey again  ")
    elif user == "paper" and comp == "sis" :
        print(" you loose try again ")
    elif user == "paper" and comp == "rock" :
        print("you win ")
    elif user == "sis" and comp == "rock" :
        print(" you loose try again ")
    elif user == "sis" and comp == "paper":
        print("you win")
    else:
        print("invalid")
    a = input("Do you want to play again? yes/no: ")
print("end")