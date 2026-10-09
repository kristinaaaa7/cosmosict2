#number guess number
print("guess he number from 1 to 100 ")

import random 

num =  random.randint(1,100)
a =0

print("enter your guess number")

while a != num:
    a = int(input("enter the num"))
    if a < num:
        print("too low. try again") 

    elif a > num:
        print("to high. try again")

    else:
        print("you are correct")




print("end of the code")





 
          

