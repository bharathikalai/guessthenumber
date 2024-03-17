import random
name = input("what is your name?")   #i am entering my name

print("Good Luck ! ", name)    # printing my name

words = ['bharathi','ragul']   # store the value in tuple

word = random.choice(words)   # using random stored the value in word

print("guess the characters")  # print this statement

guesses = ''

turns = 12

while turns > 0:

    failed = 0

    for char in word:
        print("the real gusses",guesses)
        if char in guesses:
            
            print(char, end= " ")

        else:
            print("_")

            failed +=1

    if failed == 0:
        print("you win")
        print("the word is: ", word)
        break

    print()
    guess = input("guess a character")

    guesses += guess

    if guesses not in word:
        turns -=1

        print("wrong")

        print("you have", + turns, 'more guesses')

        if turns == 0:
            print("you loose")