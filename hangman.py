import random

from collections import Counter

somewords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon
 cherry papaya berry pech lychee muskmelon'''

somewords = somewords.split(' ')

print(somewords,"somewords")

word = random.choice(somewords)

print("word",word)


if __name__ == '__main__':

    print("guess the word! hint: word is a name of a fruit")

    for i in word:

        print('__', end= ' ')
    print()

    playing = True
    letterGussed = ' '

    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances != 0 ) and flag == 0:
            print()
            chances -=1
