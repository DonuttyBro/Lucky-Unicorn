import random

#main routine goes here
tokens = ["deadshot", "harley quinn", "harley quinn", "harley quinn", "captain boomerang", "captain boomerang", "captain boomerang", "amanda waller", "amanda waller", "amanda waller"]
STARTING_BALANCE = 100

balance = STARTING_BALANCE
#tesing loop to generate 20 tokens
for item in range(0,100):
    chosen = random.choice(tokens)
    
    #adjust balance
    if chosen == "deadshot":
        balance +=5
    elif chosen == "amanda waller":
        balance -= 1
    else:
        balance -= 0.5

#output
print()
print("Starting Balance: ${}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))