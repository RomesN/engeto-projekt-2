from random import sample

# Greeting
separator = "-"
print("Hi there!")
print(separator * 47)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(separator * 47)
print("Enter a number 4 digit number:")
print(separator * 47)

# NumberToGuess
secret_source = list(range(0, 10))
secret_number = [0, 0, 0, 0]
while secret_number[0] == 0:
    secret_number = sample(secret_source, 4)

# Guessing
guess = int()
guess_list = []
while not guess_list:
    try:
        guess = int(input())
        wrong_input = False
        bulls = 0
        cows = 0
        # Checking for repeating numbers
        for i, n in enumerate(str(guess)):
            if guess not in range(1000, 10000):
                print("The number must have 4 digits! Try again...")
                guess_list = []
                break
            guess_list.append(int(n))
            for idx in range(0, i):
                if guess_list[idx] == guess_list[i]:
                    print("There cannot be any repeating numbers! Try again...")
                    wrong_input = True
                    break
            if wrong_input:
                guess_list = []
                break
            # Checking for 0 at the start
            if guess_list[0] == 0:
                print("Entered number cannot start with 0! Try again...")
                guess_list = []
                break
            # Checking whether the number is bull or a cow
            elif guess_list[i] == secret_number[i]:
                bulls += 1
            elif guess_list[i] in secret_number:
                cows += 1
        else:
            # Victory case
            if bulls == 4:
                print("Correct, you've guessed the right number!")
            # Lenght check
            else:
                print(f"{bulls} bull", end=",") if bulls == 1 else print(f"{bulls} bulls", end=",")
                print(f"{cows} cow") if cows == 1 else print(f"{cows} cows")
                guess_list = []
    # Case if non positive number or non-numeric type entered
    except ValueError:
        print("Entered value must be a non negative number! Try again...")
