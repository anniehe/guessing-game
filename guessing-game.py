from random import randint

random_number = randint(1, 100)
guess = 0
guess_count = 0

print "Hello there! Welcome to the number guessing game!"

name = raw_input("What's your name? ")

print "%s, I'm thinking of a number between 1 and 100." % (name)
print "Try to guess my number!"

# print random_number

while guess != random_number:
    guess = int(raw_input("Your guess? "))
    guess_count += 1
    # print guess_count

#     if guess is incorrect:
#         give hint
#     else:
#         congratulate player
