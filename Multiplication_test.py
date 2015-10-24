# Multiplication test
# import module
from random import randint

# set score to zero and turns to zero
score = 0
turns = 0

while turns < 10:
    turns += 1
    #Pick a number
    x = int(raw_input("Please enter a number:"))

    # Generate a random number
    y = randint(1, 12)

    # Ask the question
    #print "Your number is %s and the random number is %s" % (x, y)

    print "What is %s x %s ?" % (x, y)

    guess = int(raw_input())

    if guess == (x * y):
        print "Correct"
        score += 1
    else:
        print "Wrong"
      
    print "Your score is %s after %s turns" % (score, turns)



