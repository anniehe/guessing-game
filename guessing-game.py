from random import randint

random_number = randint(1, 100)

print "Hello there! Welcome to the number guessing game!"

name = raw_input("What's your name? ")

print "%s, I'm thinking of a number between 1 and 100." % (name)
print "Try to guess my number!"

# print random_number

# choose random number between 1 and 100
# while True:
#     get guess
#     if guess is incorrect:
#         give hint
#     else:
#         congratulate player
