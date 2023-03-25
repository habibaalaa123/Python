import random
x=random.randint(0,10)
score=100
for i in range (0,10):
    y=int(input("Please enter number between 1 and 10"))
    if y>10 or y<0:
       print("number is not in range")
    else:
        if y>x:
            print("the number is smaller than you entered")
            score-=10
        elif x>y:
            print("the number is bigger than you entered")
            score-=10
        else:
            print("number is correct")
            break
        z=input("wanna continue playing? if no please type exit if yes type any other letter")
        if z=="exit":
             break
print("you current score is",end=" ")
print(score)