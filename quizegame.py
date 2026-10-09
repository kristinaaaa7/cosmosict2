print("welcome to quize game")

game = input("do you want to play game ")
score = 0
if game != "yes" and game != "YES" and game != "Yes":
    quit()
print(" game is start....")
print("1. what is the capital of nepal?")
print ("1.pokhara 2.kathmandu 3.new dehli 4.gulmi?")
answer = input("enter the answer  ?")
if answer =="kathmandu" or answer =="2":
    print("you are correct")
    score+=1
else:
    print("incorrect.")

print ("1. Which planet is known as the Red Planet?")
print(" A) Venus B) Mars C) JupiterD) Saturn")
answer = input("enter the answer ?")
if answer =="Mars" or answer =="B" or answer =="b":
    print("you are correct")
    score+=1
else:
    print("incorrect.")

print("2. What does HTML stand for?")
print("A) Hyper Text Markup Language B) High Text Machine Language  C) Hyper Transfer Markup Language D) Home Tool Markup Language")
answer = input("enter the answer ?")
if answer == "hyper text mark up language" or answer == "A" or answer == "a":  
    print("you are correct")
    score+=1
else:
    print("incorrect.")
print(f"total score is {score}")

def ready():
    pass
