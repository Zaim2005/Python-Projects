import random
random_number = random.randint(-5,11)

while True:
    r = int(input("enter the number :- "))
    if r == random_number:
        print(" Congratulatins , you guess it right ",random_number)
        quit()

    elif r > random_number:
        print("your number is greater")
    elif r < random_number:
        print("your number is smaller")
