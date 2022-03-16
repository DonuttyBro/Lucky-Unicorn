import random
#set balance for testing purposes
balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play...")
while play_again =="":

    #increase # of rounds played
    rounds_played += 1

    #print round number
    print()
    print("*** Round #{} ***".format(rounds_played))

    chosen_num = random.randint(1,100)
    
    #adjust balance
    #if the random # is between 1 and 5 user gets a unicorn (add $5 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "deadshot"
        balance +=5
    elif 6 <= chosen_num <= 36:
        chosen = "amanda waller"
        balance -= 1
    else:
        if chosen_num % 2 == 0:
            chosen = "captain boomerang"
        else:
            chosen = "harley quinn"
        balance -= 0.5

    print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit")
