import random
import time
import sys
import getopt

def generate_random_number():
    return random.randint(1000, 9999)

def add_numbers(argv=sys.argv[1:]):
    is_repeat_mode = False

    # Declare available options
    short_options = "r"
    long_options = ["repeat"]

    # Read options from command line arguments
    try:
        arguments, values = getopt.getopt(argv, short_options, long_options)
        for current_argument, current_value in arguments:
            if current_argument in ("-r", "--repeat"):
                is_repeat_mode = True
    except getopt.error as error:
        print(error)
        sys.exit(1)

    # Prepare question
    first_number = generate_random_number()
    second_number = generate_random_number()

    question = f"{first_number} + {second_number} = "

    # Ask user for the answer and measure time
    start_time = time.time()
    user_answer = input(question)

    try:
        user_answer = int(user_answer)
    except ValueError:
        # Notify user about invalid input and start over if repeat mode is on
        print("Invalid input. Expected an integer.")
        if is_repeat_mode:
            add_numbers(argv)
        return

    end_time = time.time()
    time_passed = end_time - start_time
    
    # Copmare answer from user with the correct answer
    sum = first_number + second_number
    
    if user_answer == sum:
        print(f"Correct! It took you {time_passed:.2f} seconds.")
    else:
        print(f"Wrong! Correct answer is {sum}.")
    
    # Go from the top if repeat mode is on
    if is_repeat_mode:
        add_numbers(argv)

if __name__ == "__main__":
    add_numbers()
