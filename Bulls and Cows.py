from random import sample
from time import time


# Evaluation def
def overall_eval(clean_counter, t_time) -> str:
    if clean_counter < 5 or t_time < 20:
        result = "amazing"
    elif clean_counter < 7 and t_time < 50:
        result = "very good"
    elif clean_counter < 10 and t_time < 60:
        result = "good"
    elif clean_counter > 15:
        result = "not so good"
    else:
        result = "average"
    return result


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
clean_guess_counter = 0
wrong_input_counter = 0
total_time = 0
start_time = time()
while not guess_list:
    try:
        guess = int(guess_txt := input())
        wrong_input = False
        bulls = 0
        cows = 0
        for i, n in enumerate(str(guess)):
            guess_list.append(int(n))
            # Checking for repeating numbers
            for idx in range(0, i):
                if guess_list[idx] == guess_list[i]:
                    print("There cannot be any repeating numbers! Try again...")
                    wrong_input = True
                    break
            if wrong_input:
                wrong_input_counter += 1
                guess_list = []
                break
            # Checking for 0 at the start
            if guess_txt[0] == "0":
                print("Entered number cannot start with 0! Try again...")
                wrong_input_counter += 1
                guess_list = []
                break
            # Checking correct length
            if guess not in range(1000, 10000):
                print("The number must have 4 digits! Try again...")
                wrong_input_counter += 1
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
                end_time = time()
                total_time = end_time - start_time
                clean_guess_counter += 1
                print("Correct, you've guessed the right number!")
                if clean_guess_counter == 1:
                    print(f"It took you {clean_guess_counter} guess", end="")
                else:
                    print(f"It took you {clean_guess_counter} guesses", end="")
                if wrong_input_counter == 1:
                    print(f", {wrong_input_counter} wrong input.")
                else:
                    print(f", {wrong_input_counter} wrong inputs")
                print("and {:.2f} seconds.".format(total_time))
                print(separator * 47)
            # Informing about bulls and cows
            else:
                clean_guess_counter += 1
                print(f"{bulls} bull", end=", ") if bulls == 1 else print(f"{bulls} bulls", end=", ")
                print(f"{cows} cow") if cows == 1 else print(f"{cows} cows")
                print(separator * 47)
                guess_list = []
    # Case if non positive number or non-numeric type entered
    except ValueError:
        wrong_input_counter += 1
        print("Entered value must be a non negative number! Try again...")

# Evaluation
evaluation = overall_eval(clean_guess_counter, total_time)
print(f"That's {evaluation}.")
