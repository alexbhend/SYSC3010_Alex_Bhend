import string
import random

#create list of 4 chars
secret = [random.choice('ABCDEF') for item in range(4)]

#provide player with instructions
print("I've selected a 4-character secret code from the letters A, B, C, D, E and F.")
print("I may have repeated some.")
print("Now, try and guess what I chose.")

yourguess = []
while list(yourguess) != secret:
    yourguess = input("Enter a 4-letter guess: e.g. ABCD : ").upper()
    if len(yourguess) != 4:
        continue

    #turn guess into a list
    print("You guessed ", yourguess)    

    #create list of tuples comparing the secret with guess
    comparingList = zip(secret, yourguess)

    #create list of letters that match (wil be 4 when lists match exactly)
    correctList = [speg for speg, gpeg in comparingList if speg == gpeg]

    #count each of the letters in the secret and the guess and make note of fewest in each
    fewestLetters = [min(secret.count(j), yourguess.count(j)) for j in 'ABCDEF']

    print("Number of correct letters is ", len(correctList))
    print("Number of unused letters is ", sum(fewestLetters) - len(correctList))

print("YOU GOT THE ANSWER : ", secret)