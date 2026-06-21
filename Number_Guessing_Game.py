print("🎮 Number Guessing Game")
print("Guess a number between 1 and 10")

import random
Secret_Number = random.randint(1, 10)

Guess = int(input("Guess the Number :")) 

if Guess == Secret_Number :
    print("Congaratulation, You Won🎊")
elif Secret_Number < Guess :
        print("To High🚀")
        print("Try again👍")
else :
    print("To Low😱")  
    print("Try again👍")
