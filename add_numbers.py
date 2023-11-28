import random
import time

def generate_random_number():
    return random.randint(1000, 9999)

def main():
    num1 = generate_random_number()
    num2 = generate_random_number()
    
    start_time = time.time()

    question = f"{num1} + {num2} = "
    user_answer = input(question)

    try:
        user_answer = int(user_answer)
    except ValueError:
        print("Invalid input. Expected an integer.")
        return

    end_time = time.time()
    elapsed_time = end_time - start_time
    
    actual_sum = num1 + num2
    
    if user_answer == actual_sum:
        print(f"Correct! It took you {elapsed_time:.2f} seconds.")
    else:
        print(f"Wrong answer! Correct answer is {actual_sum}.")

if __name__ == "__main__":
    main()
