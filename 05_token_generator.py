import random

#main routine goes here

tokens = ["deadshot", "harley quinn", "captain boomerang", "amanda waller"]
balance = 100

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
    print("Token: {} , Balance: ${}".format(chosen, balance))