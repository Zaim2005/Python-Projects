import random
import time
options  = [ "+", "-" , "*" ]
operator = random.choice(options)
maxi = 20
mini = 3



def generator():
    left = random.randint(mini , maxi)
    right = random.randint(mini , maxi)
    expr = str(left)+ " " +operator+ " " + str(right)
    answer = eval(expr)
    return expr , answer

for i in range(10):
    start = time.time()
    expr , answer = generator()
    wrong = 0
    while True:
        ans = input("Q#" + str(i + 1) + " is : "+ expr +  " = " )
        if ans == str(answer) :
            break
        
        wrong +=1
        

    end = time.time()
total = end - start
print("Well done!! you finished it in : " , total , "seconds")
print("you gave " , wrong , "wrong anwers")


