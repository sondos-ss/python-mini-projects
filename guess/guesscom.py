import random

def guess(x):
    num=random.randint(1,x)
    guess=0
    while num!=guess:
        guess= int(input(f"guess a number between 1 and{x} : "))

        if guess<num:
            print("sorry , too low")
        elif guess>num:
            print("sorry, too high")

    print(f"congrats , you have guessed the number {num} correct")    


def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        guess=random.randint(1,x)
        feedback=input(f"Is {guess} is low (l)or high (h) or correct (c)  ")
        if feedback =='h':
           high=guess-1
        elif feedback=='l':
            low= guess+1   

    print(f"the computer guess your number {guess} correctly")










computer_guess(10)



    

