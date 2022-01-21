from random import sample
from time import time


# Greeting
def greeting() -> None:
    separator = "-"
    print("Hi there!")
    print(separator * 47)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(separator * 47)
    print("Enter a number 4 digit number:")
    print(separator * 47)
    return None


# Number to guess
def to_guess() -> list:
    secret_source = list(range(0, 10))
    secret_number = [0, 0, 0, 0]
    while secret_number[0] == 0:
        secret_number = sample(secret_source, 4)
    return secret_number


# Input check
def inpt_check(inpt: str) -> bool:
    try:
        int_input = int(inpt)
        # starting with 0?
        if inpt[0] == "0":
            print("Entered number cannot start with 0! Try again...")
            return False
        # 4 digits?
        elif int_input > 9999 or int_input < 1000:
            print("The number must have 4 digits! Try again...")
            return False
        # Duplicates?
        elif len(list(inpt)) != len(set(list(inpt))):
            print("There cannot be any repeating numbers! Try again...")
            return False
        else:
            return True
        # Contains non numerical characters?
    except ValueError:
        print("Entered value must be a non negative number! Try again...")
        return False


#  Conversion of correct input to list of integers
def converter(inpt: str) -> list:
    inpt_list = list(inpt)
    list_to_guess = []
    for idx in range(0, 4):
        list_to_guess.append(int(inpt_list[idx]))
    return list_to_guess


# Bulls cows calculator
def bulls_cows(guessed_list: list, to_guess_list: list) -> tuple:
    bulls = 0
    cows = 0
    for idx in range(0, 4):
        if guessed_list[idx] == to_guess_list[idx]:
            bulls += 1
        elif guessed_list[idx] in to_guess_list:
            cows += 1
    return bulls, cows


# Printing results
def victory_result(clean_guess_counter: int, wrong_input_counter: int, total_time: float) -> None:
    separator = "-"
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
    return None


# Evaluation
def overall_eval(clean_counter: int, t_time: float) -> str:
    if clean_counter < 5 or t_time < 20:
        result = "amazing"
    elif clean_counter < 7 and 50 > t_time:
        result = "very good"
    elif clean_counter < 10 and t_time < 60:
        result = "good"
    elif clean_counter > 15:
        result = "not so good"
    else:
        result = "average"
    return result


# Main
def main() -> None:

    greeting()

    # variable initialization
    num_to_guess = to_guess()
    wrong_input_counter = 0
    bulls = 0
    clean_guess_counter = 0

    # guessing
    start_time = time()
    while bulls != 4:
        while not inpt_check(guessed_num := input()):
            wrong_input_counter += 1
        clean_guess_counter += 1
        guessed_num_list = converter(guessed_num)
        bulls, cows = bulls_cows(guessed_num_list, num_to_guess)
        print(f"{bulls} bull", end=", ") if bulls == 1 else print(f"{bulls} bulls", end=", ")
        print(f"{cows} cow") if cows == 1 else print(f"{cows} cows")
    total_time = time() - start_time

    # printing results
    victory_result(clean_guess_counter, wrong_input_counter, total_time)
    print(f"That's {overall_eval(clean_guess_counter, total_time)}.")

    return None


if __name__ == "__main__":
    main()
