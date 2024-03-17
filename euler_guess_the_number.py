import random

import math

lower = int(input("enter lower bound:- "))

upper = int(input("enter upper bound:- "))

# generate the random number between the lower and upper

x = random.randint(lower,upper)

print("x value",x)

print("\n\tyou've only ", round(math.log(upper - lower + 1,2)), 
      " chances to guess the integer!\n")

count = 0

while count < math.log(upper - lower + 1,2):
    count +=1

    guess = int(input("guess a number"))

    if x == guess:
        print(f"you are correct {count}")
        break
    elif x > guess:
        print("you guessed too small")

    elif x < guess:
        print("you guessed too high")

if count >= math.log(upper - lower + 1, 2):
    print(f"the number is {x}")
    print("\nBetter Luck Next time!")