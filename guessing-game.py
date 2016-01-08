from random import randint


print "Hello, there! Welcome to the number guessing game!"

name = raw_input("What's your name? ")

while True:
    random_number = randint(1, 100)

    print "%s, I'm thinking of a number between 1 and 100." % (name)
    print "Try to guess my number!"

    # print random_number

    guess = 0
    guess_count = 0

    while guess != random_number:
        try:
            guess = int(raw_input("Your guess? "))
        except ValueError:
            print "That's not a valid number. Try again."
        else:
            if guess < 1 or guess > 100:
                print "Your guess was not between 1-100. Try again."
            else:
                guess_count += 1
                # print guess_count
                if guess > random_number:
                    print "Your guess is too high, try again."
                elif guess < random_number:
                    print "Your guess is too low, try again."
                else:
                    print "Well done, %s! You found my number in %d tries!" % (name, guess_count)

    print "Do you want to play again?"

    play_again = raw_input("Enter 'Y' for YES or 'N' for NO: ")
    if play_again != "Y" and play_again != "y":
        print "Goodbye!"
        break
