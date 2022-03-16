import random

#main routine goes here

STARTING_BALANCE = 100

balance = STARTING_BALANCE
#tesing loop to generate 20 tokens
for item in range(0,10):
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

print()
#output
print()
print("Starting Balance: ${}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))