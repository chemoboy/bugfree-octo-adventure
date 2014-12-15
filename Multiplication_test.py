# Multiplication test
from random import randint

#Pick a number
x = int(raw_input("Please enter a number:"))

# Generate a random number
y = randint(1, 12)

# Ask the question
print "Your number is %d and the random number is %d" % (x, y)

print "What is %d x %d ?" % (x, y)

print "Answer is %d" % (x * y)

guess = int(raw_input())

if guess == (x * y):
    print "Correct"
else:
    print "Wrong"
  
