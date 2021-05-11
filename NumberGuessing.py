import random
import math


# guess input of guess int
def guessInt():
    return int(input("Guess an integer "))
    
# Intitial hint: Checks to see if the number is prime
def primeCheck(number):
    i  = 2 
    prime = True

    while i <= math.floor(math.sqrt(number)) and prime == True:
        if number % i == 0:
            prime = False
        else:
            i += 1

    if prime == True and number != 1:
        print('The number is prime.')
    else:
        print('The number is not prime.')

# Checks the guess from the user and incriments the count of number of guesses
def checkGuess(number, guess, guessCount):
    guessCount += 1
    if guess == number:
        print("You got it!")
        print("It took " + str(guessCount) + " guess(es). You get " + str(6-guessCount) + " points.")
        return True
    else:
        print ("That's not it.")
        return False


# Hint 2: Checks to see if the number is a triangle number
def triangleCheck(number):
    i = 1
    j = 1
    triangle = False

    while i + j <= number:
        j += 1
        i += j
        if i == number:
            triangle = True
        

    if triangle == True or number == 1:
        print('The number is a triangle number.')
    else:
        print('The number is not a triangle number.')

#start main

# user create range
difficulty = input("Enter 1 for easy, 2 for hard or 3 for impossible: ")
if int(difficulty) in range(1,4):
    max = pow(10,int(difficulty))
    print("You will be searching for an integer between 1 and " + str(max) + '.')
else:
    print("Error: You entered a number that wasn't 1, 2, or 3. You are a failure.")
    sys.exit()

# create number
number = random.randint(1,max)

# create count
guessCount = 0

# hint 1: prime or not
print('Hint 1:')
primeCheck(number)

# guess 1
guess = guessInt()
if checkGuess(number, guess, guessCount) == True:
    sys.exit()
guessCount += 1

# hint 2: less than or greater than previous guess
print("Hint 2: ")
if guess < number:
    print("The number is greater than " + str(guess))
else:
    print("The number is less than " + str(guess))

# guess 2
guess = guessInt()
if checkGuess(number, guess, guessCount) == True:
    quit()
guessCount += 1

# hint 3: triangle number or not
print("Hint 3: ")
triangleCheck(number)

# guess 3
guess = guessInt()
if checkGuess(number, guess, guessCount) == True:
    quit()
guessCount += 1

# hint 4: less than or greater than previous guess
print("Hint 4: ")
if guess < number:
    print("The number is greater than " + str(guess))
else:
    print("The number is less than " + str(guess))

# guess 4
guess = guessInt()
if checkGuess(number, guess, guessCount) == True:
    quit()
guessCount += 1

print("The integer was " + str(number))
print("0 points. That's disapointing.")