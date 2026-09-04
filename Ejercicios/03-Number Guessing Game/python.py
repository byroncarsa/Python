import random

level = 0

while level != '1' and level != '2' and level != '3':
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")
    print('You have 5 chances to guess the correct number.')
    print('')
    print('Please select the difficulty level:')
    print('1. Easy (10 chances)')
    print('2. Medium (5 chances)')
    print('3. Hard (3 chances)')
    print('')
    level = input('Enter your choice:')
    
if level == '1':
    print('Great! You have selected the Easy difficulty level.')
    print("Let's start the game!")
    chances = 10
elif level == '2':
    print('Great! You have selected the Medium difficulty level.')
    print("Let's start the game!")
    chances = 15
elif level == '3':
    print('Great! You have selected the Hard difficulty level.')
    print("Let's start the game!")
    chances = 3
    
number_random = random.randint(1, 100)

attempts = chances

for i in range(attempts):  
    isNotValid = True
    
    while isNotValid:
        try:
            tmp = input("Ingresa un número del 1 al 100: ")
            number = int(tmp)
            
            if number_random > number:
                isNotValid = False 
                attempts -= 1
                print(f"Incorrect! The number is mayor than {number}.")
            elif number_random < number:
                isNotValid = False
                attempts -= 1
                print(f"Incorrect! The number is less than {number}.")
            elif number_random == number:
                print(f"Congratulations! You guessed the correct number in {chances - attempts} attempts.")
                break
        except ValueError:
            isNotValid = True
            print("Error. Debes ingresar un número válido.")

if attempts == 0:
    print('Te quedaste sin intentos')