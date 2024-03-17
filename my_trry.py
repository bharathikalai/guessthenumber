import random

def guss_the_number():

    computer_guss = random.randint(1,5)

    guss = 0

    print("welcome the number guess game")
    print("computer : i have chossen a number between 1 to 5 can you guss it ")

    while True:
        human = int(input("enter the number"))

        guss +=1

        if human > computer_guss:
            print("you gussing is high")

        elif human < computer_guss:
            print("you guss is low")
        else:
            print(f"you are correct total attamt{guss} the correct value is {computer_guss}")
            break


guss_the_number()

    

