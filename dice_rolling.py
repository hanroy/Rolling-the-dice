import random
min= 1
max= 6
answer = raw_input ("do you want roll the dice ?")

while True:
        if answer  == "y" or answer == "yes":
                print  ("Rolling the dices - The value is :") 
                print random.randint(min, max)
                answer = raw_input("do you want roll the dice again?")
      
        else:
                print ("Thanks for playing!")
                break

