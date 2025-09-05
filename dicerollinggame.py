#Import random module to make random choices
import random
#Create a loop for two dice
while True:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    #show results
    print('You rolled a', dice1, 'and', dice2)
    print('Total:', dice1 + dice2)
    #Ask if they wanna play again
    roll_again = input('Roll again? (yes/no): ').lower()
    #If they don't type 'yes', exit loop
    if roll_again != "yes":
        print('Thanks for playing!')
        break