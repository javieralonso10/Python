print("Welcome to the Guessing Game!")
print("Please selecte a number to guess between 1 and 100.")
print("You have 10 attempts to guess the correct number.")
print("Good luck!")
x = 42  # This is the number to guess, you can change it to any number between 1 and 100
attempts = 10
while attempts > 0:
    guess = int(input("Enter your guess: "))
    if guess < x:
        print("Too low! Try again.")
    elif guess > x:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the correct number!")
        break
    attempts -= 1
    print(f"You have {attempts} attempts left.")
if attempts == 0:
    print(f"Game over! The correct number was {x}.")
