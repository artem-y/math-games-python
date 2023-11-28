import random
import time

def generate_random_number():
    return random.randint(1000, 9999)

def add_numbers():
    first_number = generate_random_number()
    second_number = generate_random_number()

    question = f"{first_number} + {second_number} = "

    start_time = time.time()
    user_answer = input(question)

    try:
        user_answer = int(user_answer)
    except ValueError:
        print("Invalid input. Expected an integer.")
        return

    end_time = time.time()
    time_passed = end_time - start_time
    
    sum = first_number + second_number
    
    if user_answer == sum:
        print(f"Correct! It took you {time_passed:.2f} seconds.")
    else:
        print(f"Wrong! Correct answer is {sum}.")

if __name__ == "__main__":
    add_numbers()
