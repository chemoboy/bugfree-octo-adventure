# Multiplication test
from random import rand

#Pick a number
x = int(raw_input("Please enter a number"))

# Generate a random number
y = rand(1, 10)

# Ask the question
guess = int(raw_input("What is %d x %d ? ") % x, y

if guess == x * y:
    print "Correct"
else:
    print "Wrong"
  
