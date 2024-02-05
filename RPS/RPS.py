import random
user_wins=0
computer_wins=0
options=["rock","paper","scissors"]
while True:
    user_input=input("Type Rock/Paper/Scissors or Q to Quit: ").lower()
    if user_input=="q":
        break

    if user_input not in options:
        continue
    

    random_num=random.randint(0,2)
    #Rock:0  Paper:1  Scissors:3
    computer_pick= options[random_num]
    print("Computer picked : ",computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    elif user_input==computer_pick:
        print("draw!")
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")

print("Goodbye!")    