import random
print("Welcome to the second version of the Guessing Game!")
print ("Please select the range of numbers you want to guess between.")

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

attempts = int(input("Enter the number of attempts: "))
correct_number = random.randint(first_number, second_number)

while attempts > 0:
    guess = int(input("Enter your guess: "))
    if guess < correct_number:
        print("Too low! Try again.")
    elif guess > correct_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the correct number!")
        break
    attempts -= 1
    print(f"You have {attempts} attempts left.")
if attempts == 0:
    print(f"Game over! The correct number was {correct_number}.")