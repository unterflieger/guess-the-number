import os
import random

def cls():
    _ = os.system('cls')

guess = 0
solution = 0

cls()

try:
    while True:
        def retry():    
            cls()
            solution = int(random.randint(1,100))
            print('Try to guess the number! (Range: 1-100)')
            guess = 0
            while int(guess) is not int(solution):
                guess = input()
                #if isinstance(guess, int):   #doesnt work, might look into the problem
                if True:
                    if int(guess) > int(solution):
                        print('The solution is smaller than your guess!')
                    elif int(guess) < int(solution):
                        print('The solution is larger than your guess!')
                    elif int(guess) is int(solution):
                        print('Your guess is correct!')
                        input('')
                    else:
                        print('Something broke.')
                else:
                    print('Input is not valid!')
                    input('')
                    retry()
                
        retry()


except KeyboardInterrupt:
    cls()
    print('Closed Guess the Number.')