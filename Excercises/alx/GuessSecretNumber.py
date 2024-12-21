import random



play_again = True

while play_again:
    random_namber = random.randint(1, 10)
    
    try:
        guess = int(input('I\'m thinking of a number between 1 and 10. Can you guess it?'))
    except:
        print('Please enter invalid number!')
        continue 

    match guess:
        case g if random_namber == guess:
            print('Congratulations, you guessed it!')
        case g if random_namber > guess:
            print('Nope, your guess is a bit low. Give it another shot!')
        case g if random_namber < guess:
            print('Oops, your guess is a bit high. Try again!')
    
    print(f'Random number was {random_namber}')

    user_input = input('Play again? (yes/no)')
    if user_input == 'no':
        play_again = False 




