import random
while True:
    user_choose = input("Enter your choose rock/paper/scissors: ")
    user_choose = user_choose.lower()
    while user_choose != "paper" and user_choose != "rock" and user_choose != "scissors":
        user_choose = input("{} not valid. Please choose between rock/paper/scissors: ".format(user_choose))
        user_choose = user_choose.lower()

    computer_choose = ''
    choose = random.randint(0, 3)
    if choose == 1:
        computer_choose = "rock"
    elif choose == 2:
        computer_choose = "paper"
    elif choose == 3:
        computer_choose = "scissors"

    print("Computer choose: {}".format(computer_choose))

    if user_choose == computer_choose:
        print("Draw")
    elif user_choose == "rock":
        if computer_choose == "paper":
            print("You Wins!")
        else:
            print("Computer Wins!")
    elif user_choose == "paper":
        if computer_choose == "rock":
            print("Computer Win!")
        else:
            print("You Wins!")
    elif user_choose == "scissors":
        if computer_choose == "rock":
            print("Computer Wins!")
        else:
            print("You Win!")

    play = input("Do you want to play again y/n: ")

    if play == 'n' or play == 'N':
        break
