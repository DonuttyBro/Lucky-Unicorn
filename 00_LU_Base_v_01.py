import random
#Functions go here...
# checks for a yes no response
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        
        
        if response == "yes" or response == "y":
            response = "yes"
            return response


        elif response == "no" or response == "n":
            response = "no"
            return response


        else:
         print("Please answer yes / no")

# displays instructions, returns ""
def instructions():
    statement_generator("How to Play", "*")
    print()
    print("Choose a starting amount (minimum $1, maximum $10.)")
    print()
    print("Then press <enter> to play. You will get either Amanda Waller, Captain Boomerang, Harley Quinn or Deadshot")
    print()
    print("It costs $1 per round. Depending on your prize you might win some of the money back. Here's the payout amounts...")
    print("Deadshot: $5.00 balance increase")
    print("Harley Quinn: $0.50 balance decrease")
    print("Captain Boomerang: $0.50 balance decrease")
    print("Amanda Waller: $1.00 balance decrease")
    return ""

# checks for an integer between low and high
def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            #ask the question
            response = int(input(question))

            #if the amount is too low / too high give
            if low < response <= high:
                return response
            #output an error
            else:
                print(error)
        except ValueError:
            print(error) 

#prints decorative statement
def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)


    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

#Main routine goes here...
statement_generator("Welcome to the Lucky Shot Game", "*")

played_before = yes_no("Have you played the game before? ")


if played_before == "no":
   instructions()

print("program continues")

#Ask user how much they want to play with

how_much = num_check("How much would you like to play with? ", 0, 10)

print("You have asked to play with ${}".format(how_much))

balance = how_much

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
        prize_decoration = "!"
        balance +=5
    elif 6 <= chosen_num <= 36:
        chosen = "amanda waller"
        prize_decoration = "A"
        balance -= 1
    else:
        if chosen_num % 2 == 0:
            chosen = "captain boomerang"
            prize_decoration = "C"
        else:
            chosen = "harley quinn"
            prize_decoration = "H"
        balance -= 0.5
    
    outcome = "You got a {}. Your balance is ${:.2f}".format(chosen, balance)

    statement_generator(outcome, prize_decoration)

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit")
