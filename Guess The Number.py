from random import randint
while True:
    num = randint(1,100)
    print("WELCOME TO 'GUESS THE NUMBER'!\nI am thinking of a number between 0 and 101")
    guesses=[0]
    while True:
        a=int(input('Take a guess: '))
        if a==num:
            print (f'GOOD JOB! It took you {len(guesses)} guesses.')
            break
        guesses.append(a)
        if guesses[-2]:
            if abs(num-a) <= abs(num-guesses[-2]):
                print('WARMER!')
            else: 
                print('COLDER!')
        else:
            if abs(num-a) <= 10:
                print ('Warm!')
            else:
                print ('Cold!')
        
    again=input('Play again? (y/n)')
    if again.lower()=='n':
        exit()
