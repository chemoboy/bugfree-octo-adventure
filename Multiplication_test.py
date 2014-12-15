# Multiplication test
# import module
from random import randint

# set score to zero and turns to zero
score = 0
turns = 0

#Pick a number
x = int(raw_input("Please enter a number:"))

# Generate a random number
y = randint(1, 12)

# Ask the question
print "Your number is %d and the random number is %d" % (x, y)

print "What is %d x %d ?" % (x, y)

guess = int(raw_input())

if guess == (x * y):
    print "Correct"
    score += 1
else:
    print "Wrong"
  
print "Your score is %d " % score



